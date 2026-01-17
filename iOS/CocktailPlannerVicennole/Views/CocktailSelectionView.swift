//
//  CocktailSelectionView.swift
//  Cocktail Planner Vicennole
//
//  Vista per selezione cocktail
//

import SwiftUI

struct CocktailSelectionView: View {
    let availableCocktails: [CocktailMeta]
    @Binding var selectedCocktails: Set<String>
    @State private var showDetails = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            ForEach(availableCocktails, id: \.name) { cocktail in
                Toggle(isOn: Binding(
                    get: { selectedCocktails.contains(cocktail.name) },
                    set: { isSelected in
                        if isSelected {
                            selectedCocktails.insert(cocktail.name)
                        } else {
                            selectedCocktails.remove(cocktail.name)
                        }
                    }
                )) {
                    VStack(alignment: .leading, spacing: 4) {
                        Text(cocktail.name)
                            .font(.body)
                        if showDetails {
                            Text("Base: \(cocktail.base) • \(cocktail.tags.joined(separator: ", "))")
                                .font(.caption)
                                .foregroundColor(.secondary)
                        }
                    }
                }
            }
            
            Button(action: { showDetails.toggle() }) {
                Label(showDetails ? "Nascondi dettagli" : "Mostra dettagli", 
                      systemImage: showDetails ? "chevron.up" : "chevron.down")
                    .font(.caption)
            }
            .buttonStyle(.plain)
        }
        .padding(.vertical, 8)
    }
}
