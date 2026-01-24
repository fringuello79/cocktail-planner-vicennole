//
//  MainCocktailSelectionView.swift
//  Cocktail Planner Vicennole
//
//  Vista per selezione cocktail principale
//

import SwiftUI

struct MainCocktailSelectionView: View {
    let selectedCocktails: Set<String>
    @Binding var mainCocktail: String?
    @Binding var distributionPreset: DistributionPreset
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("Vuoi un cocktail protagonista?")
                .font(.subheadline)
                .foregroundColor(.secondary)
            
            Picker("Cocktail principale", selection: $mainCocktail) {
                Text("Nessun principale (equa)").tag(nil as String?)
                ForEach(Array(selectedCocktails).sorted(), id: \.self) { cocktail in
                    Text(cocktail).tag(cocktail as String?)
                }
            }
            .pickerStyle(.menu)
            
            if mainCocktail != nil && selectedCocktails.count > 1 {
                VStack(alignment: .leading, spacing: 8) {
                    Text("5) Preset sbilanciamento")
                        .font(.headline)
                    
                    Picker("Quanto vuoi spingere il principale?", selection: $distributionPreset) {
                        ForEach(DistributionPreset.allCases, id: \.self) { preset in
                            Text(preset.rawValue).tag(preset)
                        }
                    }
                    .pickerStyle(.menu)
                    
                    Text("Il resto viene diviso equamente tra gli altri cocktail")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
            }
        }
    }
}
