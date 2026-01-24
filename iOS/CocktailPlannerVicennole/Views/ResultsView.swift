//
//  ResultsView.swift
//  Cocktail Planner Vicennole
//
//  Vista risultati con checklist
//

import SwiftUI

struct ResultsView: View {
    @ObservedObject var viewModel: CocktailPlannerViewModel
    @ObservedObject var sessionManager: SessionManager
    @Environment(\.dismiss) var dismiss
    @State private var showingSaveAlert = false
    @State private var showingPDFShare = false
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(alignment: .leading, spacing: 20) {
                    // Distribution Summary
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Distribuzione drink (totali)")
                            .font(.headline)
                        
                        ForEach(Array(viewModel.selectedCocktails).sorted(), id: \.self) { cocktail in
                            HStack {
                                Text("• \(cocktail)")
                                Spacer()
                                Text("\(viewModel.drinksMap[cocktail] ?? 0)")
                                    .fontWeight(.semibold)
                            }
                        }
                        
                        // Warning for low portions
                        let lowPortions = viewModel.getLowPortionCocktails()
                        if !lowPortions.isEmpty {
                            HStack(alignment: .top, spacing: 8) {
                                Image(systemName: "exclamationmark.triangle.fill")
                                    .foregroundColor(.orange)
                                VStack(alignment: .leading, spacing: 4) {
                                    Text("Alcuni cocktail hanno pochissime porzioni:")
                                        .font(.caption)
                                        .fontWeight(.semibold)
                                    ForEach(lowPortions, id: \.name) { item in
                                        Text("\(item.name) (\(item.drinks))")
                                            .font(.caption)
                                    }
                                }
                            }
                            .padding()
                            .background(Color.orange.opacity(0.1))
                            .cornerRadius(8)
                        }
                    }
                    
                    Divider()
                    
                    // Ingredients Total
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Ingredienti totali")
                            .font(.headline)
                        
                        ForEach(viewModel.sortedIngredients, id: \.key) { ingredient, quantity in
                            HStack {
                                Text("• \(ingredient)")
                                Spacer()
                                Text(CocktailEngine.formatQuantity(ingredient: ingredient, value: quantity))
                                    .fontWeight(.semibold)
                            }
                        }
                    }
                    
                    // Donation Section (Optional)
                    DonationView()
                    
                    Divider()
                    
                    // Shopping Checklist
                    VStack(alignment: .leading, spacing: 12) {
                        HStack {
                            Text("🛒 Checklist spesa")
                                .font(.headline)
                            Spacer()
                            Button("Reset spunte") {
                                viewModel.resetChecklist()
                            }
                            .font(.caption)
                            .buttonStyle(.bordered)
                            .controlSize(.small)
                        }
                        
                        Text("Progresso: **\(viewModel.checkedItemsCount)/\(viewModel.totalItemsCount)** ingredienti")
                            .font(.caption)
                            .foregroundColor(.secondary)
                        
                        ForEach(viewModel.sortedIngredients, id: \.key) { ingredient, quantity in
                            VStack(alignment: .leading, spacing: 8) {
                                Toggle(isOn: Binding(
                                    get: { viewModel.checklist[ingredient] ?? false },
                                    set: { viewModel.checklist[ingredient] = $0 }
                                )) {
                                    VStack(alignment: .leading, spacing: 4) {
                                        Text("\(ingredient) — \(CocktailEngine.formatQuantity(ingredient: ingredient, value: quantity))")
                                    }
                                }
                                
                                TextField("Nota (facoltativa)", text: Binding(
                                    get: { viewModel.notes[ingredient] ?? "" },
                                    set: { viewModel.notes[ingredient] = $0 }
                                ))
                                .textFieldStyle(.roundedBorder)
                                .font(.caption)
                            }
                            .padding(.vertical, 4)
                        }
                    }
                    
                    Divider()
                    
                    // Save Session
                    VStack(alignment: .leading, spacing: 12) {
                        Text("💾 Salva sessione")
                            .font(.headline)
                        
                        TextField("Nome evento", text: $viewModel.eventName)
                            .textFieldStyle(.roundedBorder)
                        
                        Button(action: {
                            if viewModel.eventName.isEmpty {
                                showingSaveAlert = true
                            } else {
                                let session = viewModel.createSession()
                                sessionManager.addSession(session)
                                showingSaveAlert = true
                            }
                        }) {
                            Label("Salva", systemImage: "square.and.arrow.down")
                                .frame(maxWidth: .infinity)
                        }
                        .buttonStyle(.borderedProminent)
                    }
                    
                    Divider()
                    
                    // Export PDF placeholder
                    VStack(alignment: .leading, spacing: 12) {
                        Text("📄 Export PDF")
                            .font(.headline)
                        
                        Text("Funzionalità in arrivo: esporta la lista spesa in PDF")
                            .font(.caption)
                            .foregroundColor(.secondary)
                        
                        Button(action: {
                            // TODO: Implement PDF export
                            showingPDFShare = true
                        }) {
                            Label("Condividi lista", systemImage: "square.and.arrow.up")
                                .frame(maxWidth: .infinity)
                        }
                        .buttonStyle(.bordered)
                        .disabled(true) // Enable when PDF is implemented
                    }
                }
                .padding()
            }
            .navigationTitle("Risultato")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Chiudi") {
                        dismiss()
                    }
                }
            }
            .alert("Salvataggio", isPresented: $showingSaveAlert) {
                Button("OK", role: .cancel) { }
            } message: {
                Text(viewModel.eventName.isEmpty ? "Inserisci un nome evento" : "Sessione salvata con successo!")
            }
        }
    }
}
