# 🍸 Cocktail Planner Vicennole

**Da Streamlit a iOS: La tua app di pianificazione cocktail ora disponibile per iPhone!**

[![iOS](https://img.shields.io/badge/iOS-15.0+-blue.svg)](https://www.apple.com/ios/)
[![Swift](https://img.shields.io/badge/Swift-5.7-orange.svg)](https://swift.org/)
[![SwiftUI](https://img.shields.io/badge/SwiftUI-3.0-green.svg)](https://developer.apple.com/xcode/swiftui/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow.svg)](https://www.python.org/)

## 📱 Cosa fa questa App?

Cocktail Planner Vicennole è il tuo assistente personale per organizzare eventi perfetti! Inserisci il numero di persone, scegli i cocktail che vuoi servire, e l'app calcola automaticamente tutti gli ingredienti necessari con una lista spesa pronta per il supermercato.

### ✨ Caratteristiche Principali

- 🍹 **30 Cocktail Classici**: Aperitivo, Festa, Cena, Dopocena
- 🧮 **Calcolo Automatico**: Ingredienti precisi basati su persone e drink
- 🎯 **Distribuzione Intelligente**: Equa o con cocktail principale
- ✅ **Checklist Spesa**: Spunta gli ingredienti mentre fai shopping
- 📝 **Note Personalizzate**: Aggiungi note per ogni ingrediente
- 💾 **Salvataggio Sessioni**: Riutilizza configurazioni per eventi ricorrenti
- 📄 **Export PDF**: Porta la lista stampata (Streamlit version)

## 🚀 Due Versioni Disponibili

### 📱 iOS (Nativa - CONSIGLIATA)

**Vantaggi:**
- ✅ Performance native del dispositivo
- ✅ Esperienza utente ottimizzata per iPhone/iPad
- ✅ Funziona completamente offline
- ✅ Distribuzione via App Store
- ✅ Integrazione con ecosystem Apple
- ✅ Nessun server richiesto

**Percorso:** `/iOS/CocktailPlannerVicennole/`

**Guida Completa:** [GUIDA_CONVERSIONE_iOS.md](GUIDA_CONVERSIONE_iOS.md)

### 🌐 Streamlit (Web)

**Vantaggi:**
- ✅ Funziona su qualsiasi piattaforma (Windows, Mac, Linux)
- ✅ Nessuna installazione per utenti finali (browser-based)
- ✅ Export PDF completo già implementato
- ✅ Facile da hostare e condividere

**Percorso:** `/streamlit_version/`

**Avvio rapido:**
```bash
pip install streamlit reportlab
streamlit run streamlit_version/vicennole_planner_streamlit.py
```

## 📊 Confronto Versioni

| Caratteristica | iOS (Swift) | Streamlit (Python) |
|----------------|-------------|-------------------|
| **Piattaforma** | iPhone/iPad | Web (qualsiasi OS) |
| **Deployment** | App Store | Server web/locale |
| **Offline** | ✅ Completo | ❌ Richiede server |
| **Performance** | ⚡ Nativa | 🐌 Dipende da browser |
| **UI/UX** | 🎨 Native iOS | 📄 Web-based |
| **PDF Export** | 🔄 In sviluppo | ✅ Completo |
| **Costo** | $99/anno (Dev) | Gratuito |
| **Manutenzione** | Xcode updates | Pip packages |

## 🎯 Per Chi Vuole Creare l'App iOS

### Quick Start (5 minuti)

1. **Prerequisiti:**
   - Mac con macOS 12.0+
   - Xcode 14.0+ (App Store gratuito)
   - Apple Developer Account ($99/anno per App Store)

2. **Setup Progetto:**
   ```bash
   # Apri Xcode
   # File > New > Project
   # Seleziona: iOS > App
   # Nome: Cocktail Planner Vicennole
   # Interface: SwiftUI
   # Language: Swift
   ```

3. **Importa File:**
   - Trascina le cartelle da `iOS/CocktailPlannerVicennole/` nel progetto Xcode
   - Assicurati "Copy items if needed" sia selezionato

4. **Build e Test:**
   - Seleziona simulatore iPhone
   - Click Play (▶) o Cmd+R
   - L'app si apre nel simulatore!

### Guida Completa

Per istruzioni dettagliate passo-passo dalla creazione al deployment su App Store:

👉 **[LEGGI LA GUIDA COMPLETA](GUIDA_CONVERSIONE_iOS.md)**

Include:
- Setup ambiente di sviluppo
- Creazione icone e screenshot
- Configurazione App Store Connect
- Processo di submission
- Troubleshooting comune
- Best practices

## 📖 Documentazione

- **[GUIDA_CONVERSIONE_iOS.md](GUIDA_CONVERSIONE_iOS.md)**: Guida completa conversione e deployment iOS
- **[iOS/README_iOS.md](iOS/README_iOS.md)**: Documentazione tecnica iOS
- **[PRIVACY.md](PRIVACY.md)**: Privacy Policy (richiesta per App Store)
- **[streamlit_version/README.md](streamlit_version/README.md)**: Documentazione Streamlit

## 🏗️ Struttura del Repository

```
cocktail-planner-vicennole/
├── iOS/                                    # 📱 Versione iOS nativa
│   ├── CocktailPlannerVicennole/
│   │   ├── Models/                         # Modelli dati
│   │   │   ├── CocktailModels.swift
│   │   │   └── CocktailDatabase.swift
│   │   ├── Views/                          # Interfacce SwiftUI
│   │   │   ├── ContentView.swift
│   │   │   ├── CocktailSelectionView.swift
│   │   │   ├── MainCocktailSelectionView.swift
│   │   │   ├── ResultsView.swift
│   │   │   └── SavedSessionsView.swift
│   │   ├── ViewModels/                     # Logica business
│   │   │   └── CocktailPlannerViewModel.swift
│   │   ├── Services/                       # Servizi e engine
│   │   │   ├── CocktailEngine.swift
│   │   │   └── SessionManager.swift
│   │   └── CocktailPlannerVicennoleApp.swift
│   └── README_iOS.md
│
├── streamlit_version/                      # 🌐 Versione Streamlit web
│   ├── vicennole_planner_streamlit.py
│   └── README.md
│
├── cocktail_app.py                         # Versione originale semplice
├── GUIDA_CONVERSIONE_iOS.md                # 📚 Guida completa
├── PRIVACY.md                              # Privacy Policy
└── README.md                               # Questo file
```

## 🍹 Cocktail Disponibili

### Aperitivo (10)
Aperol Spritz • Campari Spritz • Americano • Negroni • Negroni Sbagliato • Gin Tonic • Hugo • Vermouth Tonic • Bellini • Prosecco

### Festa (8)
Mojito • Moscow Mule • Margarita • Daiquiri • Cuba Libre • Paloma • Gin Lemon • Vodka Lemon

### Cena (7)
Old Fashioned • Whiskey Sour • Boulevardier • Martini • Manhattan • French 75 • Sidecar

### Dopocena (5)
Espresso Martini • Black Russian • White Russian • Amaretto Sour • Irish Coffee

## 🎨 Screenshot (Versione iOS)

*(Gli screenshot verranno aggiunti dopo la build della prima versione)*

## 🔮 Roadmap Futuro

### Versione iOS
- [ ] Export PDF nativo con PDFKit
- [ ] Widget iOS per quick access
- [ ] Sync iCloud tra dispositivi
- [ ] Apple Watch companion app
- [ ] Cocktail personalizzati dall'utente
- [ ] Ricerca cocktail per ingrediente

### Versione Streamlit
- [ ] Calcolo bottiglie da acquistare
- [ ] Categorizzazione ingredienti (alcolici, mixer, garnish)
- [ ] Database cocktail espandibile
- [ ] Multi-lingua (EN, ES, FR)

## 🤝 Contribuire

Contributi, issue e feature request sono benvenuti!

1. Fork del progetto
2. Crea il tuo Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit delle modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Push al Branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📝 Note sulla Conversione

### Cosa è Stato Convertito

| Streamlit | iOS |
|-----------|-----|
| Python dataclass | Swift struct (Codable) |
| session_state | @Published properties |
| JSON file storage | UserDefaults |
| st.multiselect | Toggle + Set |
| st.button | Button + action |
| st.checkbox | Toggle |
| reportlab PDF | PDFKit (todo) |

### Pattern Architetturali

**Streamlit:** Lineare, stateful
```python
if st.button("Calcola"):
    result = calculate()
    st.session_state["result"] = result
```

**iOS:** MVVM, reactive
```swift
Button("Calcola") {
    viewModel.calculate()
}
// Auto-update via @Published
```

## 🛠️ Tecnologie Utilizzate

### iOS
- Swift 5.7+
- SwiftUI 3.0
- Foundation (UserDefaults)
- Combine (reactive programming)

### Streamlit
- Python 3.8+
- Streamlit 1.x
- ReportLab (PDF generation)

## 📜 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

## 👤 Autore

**fringuello79**
- GitHub: [@fringuello79](https://github.com/fringuello79)

## 🙏 Ringraziamenti

- Ispirato dalla necessità di pianificare eventi cocktail perfetti
- Grazie alla community Streamlit per il framework Python
- Grazie ad Apple per gli strumenti di sviluppo iOS

## 📞 Supporto

Hai domande? Problemi? Suggerimenti?

- 📧 Email: [Inserisci tua email]
- 🐛 Issue: [GitHub Issues](https://github.com/fringuello79/cocktail-planner-vicennole/issues)
- 💬 Discussioni: [GitHub Discussions](https://github.com/fringuello79/cocktail-planner-vicennole/discussions)

---

**⭐ Se questo progetto ti è utile, lascia una stella su GitHub!**

*Fatto con ❤️ e 🍸*
