//
//  ContentView.swift
//  Cocktail Planner Vicennole
//
//  Vista principale dell'applicazione
//

import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = CocktailPlannerViewModel()
    @StateObject private var sessionManager = SessionManager()
    @State private var showingSavedSessions = false
    @State private var showingResults = false
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(alignment: .leading, spacing: 20) {
                    // Header
                    VStack(alignment: .leading, spacing: 8) {
                        Text("🍸 Cocktail Planner Vicennole")
                            .font(.largeTitle)
                            .fontWeight(.bold)
                        
                        Text("Calcola esattamente cosa comprare per la tua serata")
                            .font(.subheadline)
                            .foregroundColor(.secondary)
                    }
                    .padding(.bottom, 10)
                    
                    // Saved Sessions Button
                    Button(action: { showingSavedSessions = true }) {
                        Label("Sessioni salvate", systemImage: "folder.fill")
                            .frame(maxWidth: .infinity)
                    }
                    .buttonStyle(.bordered)
                    
                    Divider()
                    
                    // Step 1: Context
                    VStack(alignment: .leading, spacing: 12) {
                        Text("1) Contesto")
                            .font(.headline)
                        
                        Picker("Che serata è?", selection: $viewModel.selectedCategory) {
                            ForEach(CocktailCategory.allCases, id: \.self) { category in
                                Text(category.rawValue).tag(category)
                            }
                        }
                        .pickerStyle(.segmented)
                    }
                    
                    Divider()
                    
                    // Step 2: Select Cocktails
                    VStack(alignment: .leading, spacing: 12) {
                        Text("2) Seleziona i cocktail")
                            .font(.headline)
                        
                        CocktailSelectionView(
                            availableCocktails: viewModel.availableCocktails,
                            selectedCocktails: $viewModel.selectedCocktails
                        )
                    }
                    
                    if !viewModel.selectedCocktails.isEmpty {
                        Divider()
                        
                        // Step 3: Main Cocktail (Optional)
                        VStack(alignment: .leading, spacing: 12) {
                            Text("3) Cocktail principale (opzionale)")
                                .font(.headline)
                            
                            MainCocktailSelectionView(
                                selectedCocktails: viewModel.selectedCocktails,
                                mainCocktail: $viewModel.mainCocktail,
                                distributionPreset: $viewModel.distributionPreset
                            )
                        }
                        
                        Divider()
                        
                        // Step 4: Event Details
                        VStack(alignment: .leading, spacing: 12) {
                            Text("4) Dettagli evento")
                                .font(.headline)
                            
                            HStack(spacing: 20) {
                                VStack(alignment: .leading) {
                                    Text("Persone")
                                        .font(.subheadline)
                                    Stepper("\(viewModel.numberOfPeople)", value: $viewModel.numberOfPeople, in: 1...200)
                                }
                                
                                VStack(alignment: .leading) {
                                    Text("Drink a testa")
                                        .font(.subheadline)
                                    Stepper("\(viewModel.drinksPerPerson)", value: $viewModel.drinksPerPerson, in: 1...10)
                                }
                            }
                            
                            Text("Totale drink stimati: **\(viewModel.totalDrinks)**")
                                .font(.caption)
                                .foregroundColor(.secondary)
                        }
                        
                        Divider()
                        
                        // Calculate Button
                        Button(action: {
                            viewModel.calculate()
                            showingResults = true
                        }) {
                            Label("Calcola", systemImage: "checkmark.circle.fill")
                                .frame(maxWidth: .infinity)
                        }
                        .buttonStyle(.borderedProminent)
                        .controlSize(.large)
                    }
                }
                .padding()
            }
            .navigationBarTitleDisplayMode(.inline)
            .sheet(isPresented: $showingSavedSessions) {
                SavedSessionsView(
                    sessionManager: sessionManager,
                    viewModel: viewModel
                )
            }
            .sheet(isPresented: $showingResults) {
                if viewModel.hasCalculated {
                    ResultsView(
                        viewModel: viewModel,
                        sessionManager: sessionManager
                    )
                }
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
