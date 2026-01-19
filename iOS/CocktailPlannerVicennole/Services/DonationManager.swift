//
//  DonationManager.swift
//  Cocktail Planner Vicennole
//
//  Gestione donazioni in-app (StoreKit 2)
//

import Foundation
import StoreKit

/// Manager per gestire le donazioni in-app tramite StoreKit 2
@MainActor
class DonationManager: ObservableObject {
    
    // Product IDs per le donazioni (da configurare in App Store Connect)
    static let productIDs = [
        "com.vicennole.cocktailplanner.donation.small",   // €1
        "com.vicennole.cocktailplanner.donation.medium",  // €3
        "com.vicennole.cocktailplanner.donation.large"    // €5
    ]
    
    @Published private(set) var products: [Product] = []
    @Published private(set) var purchaseState: PurchaseState = .idle
    
    enum PurchaseState {
        case idle
        case purchasing
        case success
        case failed(Error)
    }
    
    // MARK: - Load Products
    
    /// Carica i prodotti disponibili da App Store
    func loadProducts() async {
        do {
            products = try await Product.products(for: Self.productIDs)
            products.sort { $0.price < $1.price }
        } catch {
            print("Errore nel caricamento prodotti: \(error)")
            products = []
        }
    }
    
    // MARK: - Purchase
    
    /// Effettua l'acquisto di una donazione
    func purchase(_ product: Product) async {
        purchaseState = .purchasing
        
        do {
            let result = try await product.purchase()
            
            switch result {
            case .success(let verification):
                // Verifica la transazione
                let transaction = try checkVerified(verification)
                
                // La donazione è andata a buon fine
                purchaseState = .success
                
                // Completa la transazione
                await transaction.finish()
                
            case .userCancelled:
                purchaseState = .idle
                
            case .pending:
                purchaseState = .idle
                
            @unknown default:
                purchaseState = .idle
            }
        } catch {
            purchaseState = .failed(error)
        }
    }
    
    // MARK: - Verification
    
    private func checkVerified<T>(_ result: VerificationResult<T>) throws -> T {
        switch result {
        case .unverified:
            throw StoreError.failedVerification
        case .verified(let safe):
            return safe
        }
    }
    
    // MARK: - Helper Methods
    
    /// Formatta il prezzo del prodotto
    func formatPrice(_ product: Product) -> String {
        return product.displayPrice
    }
    
    /// Reset dello stato dopo un acquisto
    func resetPurchaseState() {
        purchaseState = .idle
    }
}

// MARK: - Store Error

enum StoreError: Error {
    case failedVerification
}

extension StoreError: LocalizedError {
    var errorDescription: String? {
        switch self {
        case .failedVerification:
            return "La verifica dell'acquisto è fallita"
        }
    }
}
