//
//  CocktailEngine.swift
//  Cocktail Planner Vicennole
//
//  Engine per calcoli distribuzione cocktail e ingredienti
//

import Foundation

class CocktailEngine {
    
    // MARK: - Split Integers Algorithm
    /// Distribuisce un totale intero tra più chiavi con pesi specifici
    static func splitIntegers(total: Int, keys: [String], weights: [Double]) -> [String: Int] {
        guard total > 0, !keys.isEmpty, keys.count == weights.count else {
            return keys.reduce(into: [:]) { $0[$1] = 0 }
        }
        
        var normalizedWeights = weights
        let weightSum = weights.reduce(0, +)
        
        if weightSum <= 0 {
            normalizedWeights = Array(repeating: 1.0, count: keys.count)
        } else {
            normalizedWeights = weights.map { $0 / weightSum }
        }
        
        // Calcola valori raw e floor
        let rawValues = normalizedWeights.map { Double(total) * $0 }
        var floors = rawValues.map { Int($0) }
        var remainder = total - floors.reduce(0, +)
        
        // Calcola frazioni decimali
        let fractions = zip(rawValues, floors).map { $0.0 - Double($0.1) }
        let sortedIndices = fractions.enumerated()
            .sorted { $0.element > $1.element }
            .map { $0.offset }
        
        // Distribuisci il resto
        var idx = 0
        while remainder > 0 {
            let targetIdx = sortedIndices[idx % sortedIndices.count]
            floors[targetIdx] += 1
            remainder -= 1
            idx += 1
        }
        
        return Dictionary(uniqueKeysWithValues: zip(keys, floors))
    }
    
    // MARK: - Drinks Distribution
    /// Calcola quanti drink fare per ogni cocktail
    static func drinksPerCocktail(
        selected: [String],
        main: String?,
        totalDrinks: Int,
        mainShare: Double?
    ) -> [String: Int] {
        guard !selected.isEmpty else { return [:] }
        
        // Un solo cocktail: tutti i drink
        if selected.count == 1 {
            return [selected[0]: totalDrinks]
        }
        
        // Distribuzione equa o principale non valido
        guard let main = main,
              let mainShare = mainShare,
              selected.contains(main) else {
            let weights = Array(repeating: 1.0, count: selected.count)
            return splitIntegers(total: totalDrinks, keys: selected, weights: weights)
        }
        
        // Distribuzione con principale
        let others = selected.filter { $0 != main }
        let rest = max(0.0, 1.0 - mainShare)
        let otherShare = others.isEmpty ? 0.0 : rest / Double(others.count)
        
        let weights = selected.map { $0 == main ? mainShare : otherShare }
        return splitIntegers(total: totalDrinks, keys: selected, weights: weights)
    }
    
    // MARK: - Ingredients Calculation
    /// Calcola le quantità totali di ingredienti necessari
    static func computeIngredients(drinksMap: [String: Int]) -> [String: Double] {
        var totals: [String: Double] = [:]
        
        for (cocktailName, numberOfDrinks) in drinksMap {
            guard let recipe = CocktailDatabase.getRecipe(forCocktail: cocktailName) else {
                continue
            }
            
            for (ingredient, qtyPerDrink) in recipe {
                totals[ingredient, default: 0.0] += qtyPerDrink * Double(numberOfDrinks)
            }
        }
        
        return totals
    }
    
    // MARK: - Formatting
    /// Formatta la quantità di un ingrediente
    static func formatQuantity(ingredient: String, value: Double) -> String {
        let lowercased = ingredient.lowercased()
        
        if lowercased.contains("(ml)") {
            if value >= 1000 {
                return String(format: "%.2f L", value / 1000)
            }
            return "\(Int(round(value))) ml"
        }
        
        if lowercased.contains("(g)") || lowercased.contains("(foglie)") {
            return "\(Int(round(value)))"
        }
        
        if abs(value - round(value)) < 1e-6 {
            return "\(Int(round(value)))"
        }
        
        return String(format: "%.1f", value)
    }
}
