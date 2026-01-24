//
//  DonationView.swift
//  Cocktail Planner Vicennole
//
//  Vista per le donazioni opzionali
//

import SwiftUI
import StoreKit

struct DonationView: View {
    @StateObject private var donationManager = DonationManager()
    @State private var showingThankYou = false
    @State private var isExpanded = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Header con toggle per espandere
            Button(action: {
                withAnimation {
                    isExpanded.toggle()
                }
            }) {
                HStack {
                    Text("☕️ Supporta lo sviluppo")
                        .font(.headline)
                        .foregroundColor(.primary)
                    
                    Spacer()
                    
                    Image(systemName: isExpanded ? "chevron.up" : "chevron.down")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
            }
            .buttonStyle(.plain)
            
            if isExpanded {
                VStack(alignment: .leading, spacing: 16) {
                    // Descrizione
                    Text("Ti è piaciuta l'app? Supporta lo sviluppatore con una donazione volontaria!")
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                    
                    // Bottoni donazione
                    if donationManager.products.isEmpty {
                        // Loading o fallback con importi fissi
                        HStack(spacing: 12) {
                            DonationButton(
                                amount: "1€",
                                icon: "cup.and.saucer.fill",
                                isLoading: false
                            ) {
                                // Fallback: mostra messaggio
                                showSimpleThanks()
                            }
                            
                            DonationButton(
                                amount: "3€",
                                icon: "heart.fill",
                                isLoading: false
                            ) {
                                showSimpleThanks()
                            }
                            
                            DonationButton(
                                amount: "5€",
                                icon: "star.fill",
                                isLoading: false
                            ) {
                                showSimpleThanks()
                            }
                        }
                        
                        Text("Le donazioni saranno disponibili nella versione App Store")
                            .font(.caption)
                            .foregroundColor(.secondary)
                            .padding(.top, 4)
                        
                    } else {
                        // Prodotti caricati da StoreKit
                        HStack(spacing: 12) {
                            ForEach(donationManager.products, id: \.id) { product in
                                DonationProductButton(
                                    product: product,
                                    isLoading: donationManager.purchaseState == .purchasing
                                ) {
                                    Task {
                                        await donationManager.purchase(product)
                                        if case .success = donationManager.purchaseState {
                                            showingThankYou = true
                                        }
                                    }
                                }
                            }
                        }
                    }
                    
                    // Note legali
                    Text("Donazione volontaria • Nessun rimborso • Grazie per il supporto!")
                        .font(.caption2)
                        .foregroundColor(.secondary)
                        .multilineTextAlignment(.center)
                        .frame(maxWidth: .infinity)
                }
                .transition(.opacity.combined(with: .move(edge: .top)))
            }
        }
        .padding()
        .background(Color(.systemBackground))
        .cornerRadius(12)
        .overlay(
            RoundedRectangle(cornerRadius: 12)
                .stroke(Color.blue.opacity(0.3), lineWidth: 1)
        )
        .alert("Grazie! ❤️", isPresented: $showingThankYou) {
            Button("Chiudi", role: .cancel) {
                donationManager.resetPurchaseState()
            }
        } message: {
            Text("Grazie mille per il tuo supporto! Il tuo contributo aiuta a mantenere e migliorare l'app. 🍸")
        }
        .task {
            // Carica i prodotti quando la vista appare
            await donationManager.loadProducts()
        }
    }
    
    private func showSimpleThanks() {
        showingThankYou = true
    }
}

// MARK: - Donation Button (Fallback)

struct DonationButton: View {
    let amount: String
    let icon: String
    let isLoading: Bool
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            VStack(spacing: 8) {
                Image(systemName: icon)
                    .font(.title2)
                
                Text(amount)
                    .font(.headline)
            }
            .frame(maxWidth: .infinity)
            .padding(.vertical, 16)
            .background(
                LinearGradient(
                    colors: [Color.blue.opacity(0.1), Color.blue.opacity(0.2)],
                    startPoint: .top,
                    endPoint: .bottom
                )
            )
            .cornerRadius(10)
            .overlay(
                RoundedRectangle(cornerRadius: 10)
                    .stroke(Color.blue.opacity(0.5), lineWidth: 1)
            )
        }
        .disabled(isLoading)
    }
}

// MARK: - Donation Product Button (StoreKit)

struct DonationProductButton: View {
    let product: Product
    let isLoading: Bool
    let action: () -> Void
    
    private var icon: String {
        // Icone basate sul prezzo
        if product.price < 2.0 {
            return "cup.and.saucer.fill"
        } else if product.price < 4.0 {
            return "heart.fill"
        } else {
            return "star.fill"
        }
    }
    
    var body: some View {
        Button(action: action) {
            VStack(spacing: 8) {
                if isLoading {
                    ProgressView()
                        .scaleEffect(1.2)
                } else {
                    Image(systemName: icon)
                        .font(.title2)
                    
                    Text(product.displayPrice)
                        .font(.headline)
                }
            }
            .frame(maxWidth: .infinity)
            .padding(.vertical, 16)
            .background(
                LinearGradient(
                    colors: [Color.blue.opacity(0.1), Color.blue.opacity(0.2)],
                    startPoint: .top,
                    endPoint: .bottom
                )
            )
            .cornerRadius(10)
            .overlay(
                RoundedRectangle(cornerRadius: 10)
                    .stroke(Color.blue.opacity(0.5), lineWidth: 1)
            )
        }
        .disabled(isLoading)
    }
}

// MARK: - Preview

struct DonationView_Previews: PreviewProvider {
    static var previews: some View {
        VStack {
            DonationView()
            Spacer()
        }
        .padding()
    }
}
