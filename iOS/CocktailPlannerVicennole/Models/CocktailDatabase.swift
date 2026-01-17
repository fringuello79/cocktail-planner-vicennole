//
//  CocktailDatabase.swift
//  Cocktail Planner Vicennole
//
//  Database di cocktail e ricette
//

import Foundation

struct CocktailDatabase {
    
    // MARK: - Catalog
    static let catalog: [CocktailMeta] = [
        // APERITIVO (10)
        CocktailMeta(name: "Aperol Spritz", category: .aperitivo, base: "Prosecco", tags: ["Frizzante", "Dolce"]),
        CocktailMeta(name: "Campari Spritz", category: .aperitivo, base: "Prosecco", tags: ["Frizzante", "Amaro"]),
        CocktailMeta(name: "Americano", category: .aperitivo, base: "Bitter/Vermouth", tags: ["Amaro", "Frizzante"]),
        CocktailMeta(name: "Negroni", category: .aperitivo, base: "Gin", tags: ["Amaro"]),
        CocktailMeta(name: "Negroni Sbagliato", category: .aperitivo, base: "Prosecco", tags: ["Amaro", "Frizzante"]),
        CocktailMeta(name: "Gin Tonic", category: .aperitivo, base: "Gin", tags: ["Fresco", "Frizzante"]),
        CocktailMeta(name: "Hugo", category: .aperitivo, base: "Prosecco", tags: ["Fresco", "Frizzante", "Dolce"]),
        CocktailMeta(name: "Vermouth Tonic", category: .aperitivo, base: "Vermouth", tags: ["Amaro", "Frizzante"]),
        CocktailMeta(name: "Bellini", category: .aperitivo, base: "Prosecco", tags: ["Dolce", "Frizzante"]),
        CocktailMeta(name: "Prosecco", category: .aperitivo, base: "Prosecco", tags: ["Frizzante"]),
        
        // FESTA / EASY (8)
        CocktailMeta(name: "Mojito", category: .festa, base: "Rum", tags: ["Fresco", "Agrumato"]),
        CocktailMeta(name: "Moscow Mule", category: .festa, base: "Vodka", tags: ["Fresco", "Agrumato", "Frizzante"]),
        CocktailMeta(name: "Margarita", category: .festa, base: "Tequila", tags: ["Agrumato"]),
        CocktailMeta(name: "Daiquiri", category: .festa, base: "Rum", tags: ["Agrumato"]),
        CocktailMeta(name: "Cuba Libre", category: .festa, base: "Rum", tags: ["Dolce", "Frizzante"]),
        CocktailMeta(name: "Paloma", category: .festa, base: "Tequila", tags: ["Agrumato", "Frizzante"]),
        CocktailMeta(name: "Gin Lemon", category: .festa, base: "Gin", tags: ["Agrumato", "Frizzante"]),
        CocktailMeta(name: "Vodka Lemon", category: .festa, base: "Vodka", tags: ["Agrumato", "Frizzante"]),
        
        // CENA / CLASSICI (7)
        CocktailMeta(name: "Old Fashioned", category: .cena, base: "Whiskey", tags: ["Dolce"]),
        CocktailMeta(name: "Whiskey Sour", category: .cena, base: "Whiskey", tags: ["Agrumato"]),
        CocktailMeta(name: "Boulevardier", category: .cena, base: "Whiskey", tags: ["Amaro"]),
        CocktailMeta(name: "Martini", category: .cena, base: "Gin", tags: ["Amaro"]),
        CocktailMeta(name: "Manhattan", category: .cena, base: "Whiskey", tags: ["Dolce"]),
        CocktailMeta(name: "French 75", category: .cena, base: "Gin", tags: ["Agrumato", "Frizzante"]),
        CocktailMeta(name: "Sidecar", category: .cena, base: "Cognac", tags: ["Agrumato"]),
        
        // DOPOCENA (5)
        CocktailMeta(name: "Espresso Martini", category: .dopocena, base: "Coffee/Vodka", tags: ["Caffè", "Dolce"]),
        CocktailMeta(name: "Black Russian", category: .dopocena, base: "Coffee/Vodka", tags: ["Caffè"]),
        CocktailMeta(name: "White Russian", category: .dopocena, base: "Coffee/Vodka", tags: ["Caffè", "Cremoso"]),
        CocktailMeta(name: "Amaretto Sour", category: .dopocena, base: "Amaretto", tags: ["Dolce", "Agrumato"]),
        CocktailMeta(name: "Irish Coffee", category: .dopocena, base: "Coffee/Whiskey", tags: ["Caffè", "Cremoso"])
    ]
    
    // MARK: - Recipes
    static let recipes: [String: Recipe] = [
        // APERITIVO
        "Aperol Spritz": ["Prosecco (ml)": 90, "Aperol (ml)": 60, "Soda (ml)": 30],
        "Campari Spritz": ["Prosecco (ml)": 90, "Campari (ml)": 60, "Soda (ml)": 30],
        "Americano": ["Bitter (ml)": 30, "Vermouth rosso (ml)": 30, "Soda (ml)": 60],
        "Negroni": ["Gin (ml)": 30, "Vermouth rosso (ml)": 30, "Bitter (ml)": 30],
        "Negroni Sbagliato": ["Prosecco (ml)": 60, "Vermouth rosso (ml)": 30, "Bitter (ml)": 30],
        "Gin Tonic": ["Gin (ml)": 50, "Acqua tonica (ml)": 100],
        "Hugo": ["Prosecco (ml)": 100, "Soda (ml)": 30, "Sciroppo sambuco (ml)": 20, "Menta (foglie)": 5],
        "Vermouth Tonic": ["Vermouth (ml)": 80, "Acqua tonica (ml)": 100],
        "Bellini": ["Prosecco (ml)": 100, "Purea di pesca (ml)": 50],
        "Prosecco": ["Prosecco (ml)": 120],
        
        // FESTA / EASY
        "Mojito": ["Rum bianco (ml)": 50, "Lime (ml)": 20, "Zucchero (g)": 10, "Soda (ml)": 100, "Menta (foglie)": 5],
        "Moscow Mule": ["Vodka (ml)": 50, "Ginger beer (ml)": 120, "Lime (ml)": 10],
        "Margarita": ["Tequila (ml)": 50, "Triple sec (ml)": 20, "Lime (ml)": 20],
        "Daiquiri": ["Rum bianco (ml)": 50, "Lime (ml)": 25, "Zucchero (g)": 10],
        "Cuba Libre": ["Rum (ml)": 50, "Cola (ml)": 120, "Lime (ml)": 10],
        "Paloma": ["Tequila (ml)": 50, "Soda al pompelmo (ml)": 120, "Lime (ml)": 10],
        "Gin Lemon": ["Gin (ml)": 50, "Limonata (ml)": 120],
        "Vodka Lemon": ["Vodka (ml)": 50, "Limonata (ml)": 120],
        
        // CENA / CLASSICI
        "Old Fashioned": ["Whiskey (ml)": 50, "Zucchero (g)": 5],
        "Whiskey Sour": ["Whiskey (ml)": 50, "Lime (ml)": 25, "Zucchero (g)": 15],
        "Boulevardier": ["Whiskey (ml)": 30, "Vermouth rosso (ml)": 30, "Bitter (ml)": 30],
        "Martini": ["Gin (ml)": 60, "Vermouth dry (ml)": 10],
        "Manhattan": ["Whiskey (ml)": 50, "Vermouth rosso (ml)": 20],
        "French 75": ["Gin (ml)": 30, "Lime (ml)": 15, "Zucchero (g)": 10, "Prosecco (ml)": 60],
        "Sidecar": ["Cognac (ml)": 50, "Triple sec (ml)": 20, "Lime (ml)": 20],
        
        // DOPOCENA
        "Espresso Martini": ["Vodka (ml)": 40, "Caffè espresso (ml)": 30, "Liquore al caffè (ml)": 20],
        "Black Russian": ["Vodka (ml)": 50, "Liquore al caffè (ml)": 20],
        "White Russian": ["Vodka (ml)": 50, "Liquore al caffè (ml)": 20, "Panna (ml)": 30],
        "Amaretto Sour": ["Amaretto (ml)": 60, "Lime (ml)": 30],
        "Irish Coffee": ["Whiskey (ml)": 40, "Caffè (ml)": 90, "Zucchero (g)": 10, "Panna (ml)": 30]
    ]
    
    // MARK: - Helper Methods
    static func getCocktails(for category: CocktailCategory) -> [CocktailMeta] {
        if category == .tutti {
            return catalog
        }
        return catalog.filter { $0.category == category }
    }
    
    static func getCocktail(byName name: String) -> CocktailMeta? {
        return catalog.first { $0.name == name }
    }
    
    static func getRecipe(forCocktail name: String) -> Recipe? {
        return recipes[name]
    }
}
