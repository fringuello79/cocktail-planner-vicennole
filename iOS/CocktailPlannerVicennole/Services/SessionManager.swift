//
//  SessionManager.swift
//  Cocktail Planner Vicennole
//
//  Gestione salvataggio e caricamento sessioni
//

import Foundation

class SessionManager: ObservableObject {
    
    @Published var savedSessions: [EventSession] = []
    
    private let userDefaultsKey = "savedSessions"
    
    init() {
        loadSessions()
    }
    
    // MARK: - Load Sessions
    func loadSessions() {
        guard let data = UserDefaults.standard.data(forKey: userDefaultsKey) else {
            savedSessions = []
            return
        }
        
        do {
            let decoder = JSONDecoder()
            savedSessions = try decoder.decode([EventSession].self, from: data)
        } catch {
            print("Error loading sessions: \(error)")
            savedSessions = []
        }
    }
    
    // MARK: - Save Sessions
    func saveSessions() {
        do {
            let encoder = JSONEncoder()
            encoder.outputFormatting = .prettyPrinted
            let data = try encoder.encode(savedSessions)
            UserDefaults.standard.set(data, forKey: userDefaultsKey)
        } catch {
            print("Error saving sessions: \(error)")
        }
    }
    
    // MARK: - Add Session
    func addSession(_ session: EventSession) {
        savedSessions.insert(session, at: 0) // Aggiungi in cima
        saveSessions()
    }
    
    // MARK: - Delete Session
    func deleteSession(_ session: EventSession) {
        savedSessions.removeAll { $0.id == session.id }
        saveSessions()
    }
    
    // MARK: - Find Session
    func findSession(byId id: String) -> EventSession? {
        return savedSessions.first { $0.id == id }
    }
}
