//
//  CocktailModels.swift
//  Cocktail Planner Vicennole
//
//  Modelli dati per l'applicazione iOS
//

import Foundation

// MARK: - Cocktail Meta Information
struct CocktailMeta: Identifiable, Codable, Hashable {
    let id = UUID()
    let name: String
    let category: CocktailCategory
    let base: String
    let tags: [String]
    
    enum CodingKeys: String, CodingKey {
        case name, category, base, tags
    }
}

// MARK: - Categories
enum CocktailCategory: String, Codable, CaseIterable {
    case aperitivo = "Aperitivo"
    case festa = "Festa"
    case cena = "Cena"
    case dopocena = "Dopocena"
    case tutti = "Tutti"
}

// MARK: - Recipe
typealias Recipe = [String: Double]

// MARK: - Event Session
struct EventSession: Identifiable, Codable {
    let id: String
    let name: String
    let createdAt: String
    let category: String
    let selected: [String]
    let main: String?
    let presetLabel: String?
    let people: Int
    let drinksPerPerson: Int
    let drinksMap: [String: Int]
    let ingredients: [String: Double]
    let checklist: [String: Bool]
    let notes: [String: String]
    
    var totalDrinks: Int {
        people * drinksPerPerson
    }
}

// MARK: - Preset Distribution
enum DistributionPreset: String, CaseIterable {
    case veryUnbalanced = "Molto sbilanciata (80%)"
    case unbalanced = "Sbilanciata (70%)"
    case light = "Leggera (60%)"
    case almostEqual = "Quasi equa (50%)"
    
    var percentage: Double {
        switch self {
        case .veryUnbalanced: return 0.80
        case .unbalanced: return 0.70
        case .light: return 0.60
        case .almostEqual: return 0.50
        }
    }
}
