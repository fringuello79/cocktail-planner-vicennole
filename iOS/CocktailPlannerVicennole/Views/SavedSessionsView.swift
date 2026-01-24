//
//  SavedSessionsView.swift
//  Cocktail Planner Vicennole
//
//  Vista per sessioni salvate
//

import SwiftUI

struct SavedSessionsView: View {
    @ObservedObject var sessionManager: SessionManager
    @ObservedObject var viewModel: CocktailPlannerViewModel
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        NavigationView {
            Group {
                if sessionManager.savedSessions.isEmpty {
                    VStack(spacing: 20) {
                        Image(systemName: "folder")
                            .font(.system(size: 60))
                            .foregroundColor(.secondary)
                        Text("Nessuna sessione salvata")
                            .font(.headline)
                            .foregroundColor(.secondary)
                    }
                } else {
                    List {
                        ForEach(sessionManager.savedSessions) { session in
                            Button(action: {
                                viewModel.loadSession(session)
                                dismiss()
                            }) {
                                VStack(alignment: .leading, spacing: 8) {
                                    Text(session.name)
                                        .font(.headline)
                                    
                                    HStack {
                                        Label(session.category, systemImage: "calendar")
                                        Spacer()
                                        Label("\(session.people) persone", systemImage: "person.2")
                                    }
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                                    
                                    Text("Creato: \(session.createdAt)")
                                        .font(.caption)
                                        .foregroundColor(.secondary)
                                    
                                    Text("Cocktail: \(session.selected.joined(separator: ", "))")
                                        .font(.caption)
                                        .foregroundColor(.secondary)
                                        .lineLimit(2)
                                }
                                .padding(.vertical, 4)
                            }
                            .swipeActions(edge: .trailing, allowsFullSwipe: true) {
                                Button(role: .destructive) {
                                    sessionManager.deleteSession(session)
                                } label: {
                                    Label("Elimina", systemImage: "trash")
                                }
                            }
                        }
                    }
                }
            }
            .navigationTitle("Sessioni salvate")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Chiudi") {
                        dismiss()
                    }
                }
            }
        }
    }
}
