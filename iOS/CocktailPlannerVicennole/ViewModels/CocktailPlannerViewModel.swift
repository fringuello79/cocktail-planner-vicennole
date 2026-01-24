//
//  CocktailPlannerViewModel.swift
//  Cocktail Planner Vicennole
//
//  ViewModel principale per la logica dell'applicazione
//

import Foundation
import SwiftUI

class CocktailPlannerViewModel: ObservableObject {
    
    // MARK: - Published Properties
    @Published var selectedCategory: CocktailCategory = .aperitivo
    @Published var selectedCocktails: Set<String> = []
    @Published var mainCocktail: String? = nil
    @Published var distributionPreset: DistributionPreset = .unbalanced
    @Published var numberOfPeople: Int = 8
    @Published var drinksPerPerson: Int = 2
    
    // Results
    @Published var drinksMap: [String: Int] = [:]
    @Published var ingredients: [String: Double] = [:]
    @Published var checklist: [String: Bool] = [:]
    @Published var notes: [String: String] = [:]
    
    @Published var hasCalculated: Bool = false
    @Published var eventName: String = ""
    
    // MARK: - Computed Properties
    var totalDrinks: Int {
        numberOfPeople * drinksPerPerson
    }
    
    var availableCocktails: [CocktailMeta] {
        CocktailDatabase.getCocktails(for: selectedCategory)
    }
    
    var sortedIngredients: [(key: String, value: Double)] {
        ingredients.sorted { $0.key.lowercased() < $1.key.lowercased() }
    }
    
    var checkedItemsCount: Int {
        checklist.values.filter { $0 }.count
    }
    
    var totalItemsCount: Int {
        ingredients.count
    }
    
    // MARK: - Methods
    
    /// Calcola la distribuzione dei drink e gli ingredienti
    func calculate() {
        let selected = Array(selectedCocktails).sorted()
        
        guard !selected.isEmpty else {
            return
        }
        
        // Calcola distribuzione drink
        let mainShare = (mainCocktail != nil && selected.count > 1) ? distributionPreset.percentage : nil
        drinksMap = CocktailEngine.drinksPerCocktail(
            selected: selected,
            main: mainCocktail,
            totalDrinks: totalDrinks,
            mainShare: mainShare
        )
        
        // Calcola ingredienti
        ingredients = CocktailEngine.computeIngredients(drinksMap: drinksMap)
        
        // Inizializza checklist se necessario
        for ingredient in ingredients.keys {
            if checklist[ingredient] == nil {
                checklist[ingredient] = false
            }
        }
        
        hasCalculated = true
    }
    
    /// Resetta le spunte della checklist
    func resetChecklist() {
        for key in checklist.keys {
            checklist[key] = false
        }
    }
    
    /// Crea una sessione da salvare
    func createSession() -> EventSession {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "yyyy-MM-dd HH:mm"
        
        return EventSession(
            id: "\(Int(Date().timeIntervalSince1970))-\(abs(eventName.hashValue % 100000))",
            name: eventName.isEmpty ? "Evento senza nome" : eventName,
            createdAt: dateFormatter.string(from: Date()),
            category: selectedCategory.rawValue,
            selected: Array(selectedCocktails).sorted(),
            main: mainCocktail,
            presetLabel: mainCocktail != nil ? distributionPreset.rawValue : nil,
            people: numberOfPeople,
            drinksPerPerson: drinksPerPerson,
            drinksMap: drinksMap,
            ingredients: ingredients,
            checklist: checklist,
            notes: notes
        )
    }
    
    /// Carica una sessione salvata
    func loadSession(_ session: EventSession) {
        eventName = session.name
        selectedCategory = CocktailCategory(rawValue: session.category) ?? .aperitivo
        selectedCocktails = Set(session.selected)
        mainCocktail = session.main
        
        if let presetLabel = session.presetLabel {
            distributionPreset = DistributionPreset(rawValue: presetLabel) ?? .unbalanced
        }
        
        numberOfPeople = session.people
        drinksPerPerson = session.drinksPerPerson
        drinksMap = session.drinksMap
        ingredients = session.ingredients
        checklist = session.checklist
        notes = session.notes
        
        hasCalculated = true
    }
    
    /// Verifica se ci sono cocktail con poche porzioni
    func getLowPortionCocktails() -> [(name: String, drinks: Int)] {
        guard selectedCocktails.count >= 4 else { return [] }
        return drinksMap.filter { $0.value < 2 }
            .map { (name: $0.key, drinks: $0.value) }
            .sorted { $0.name < $1.name }
    }
}
