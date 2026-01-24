# Cocktail Planner Vicennole - iOS App

Applicazione iOS per pianificare cocktail ed eventi, con calcolo automatico degli ingredienti necessari.

## 🎯 Caratteristiche

- ✅ 30 cocktail pre-configurati (Aperitivo, Festa, Cena, Dopocena)
- ✅ Calcolo automatico ingredienti basato su numero persone e drink
- ✅ Distribuzione equa o con cocktail principale
- ✅ Checklist spesa interattiva con note
- ✅ Salvataggio e caricamento sessioni
- ✅ Interfaccia nativa iOS in SwiftUI
- ✅ Sistema donazioni opzionali (StoreKit 2)
- 🔄 Export PDF (in sviluppo)

## 📱 Requisiti

- iOS 15.0+
- Xcode 14.0+
- Swift 5.7+

## 🚀 Setup e Build

### 1. Crea il Progetto Xcode

```bash
# Naviga nella cartella iOS
cd iOS/CocktailPlannerVicennole

# Apri Xcode e crea un nuovo progetto:
# File > New > Project
# Seleziona: iOS > App
# Nome: Cocktail Planner Vicennole
# Bundle Identifier: com.tuonome.CocktailPlannerVicennole
# Interface: SwiftUI
# Language: Swift
```

### 2. Importa i File

Aggiungi tutti i file Swift dalla struttura:
- Models/
- Views/
- ViewModels/
- Services/
- CocktailPlannerVicennoleApp.swift

### 3. Configurazione Info.plist

Nessuna configurazione speciale richiesta per la versione base.

## 🏗️ Struttura del Progetto

```
CocktailPlannerVicennole/
├── CocktailPlannerVicennoleApp.swift  # Entry point
├── Models/
│   ├── CocktailModels.swift           # Strutture dati
│   └── CocktailDatabase.swift         # Database cocktail e ricette
├── Views/
│   ├── ContentView.swift              # Vista principale
│   ├── CocktailSelectionView.swift    # Selezione cocktail
│   ├── MainCocktailSelectionView.swift # Cocktail principale
│   ├── ResultsView.swift              # Risultati e checklist
│   ├── SavedSessionsView.swift        # Gestione sessioni
│   └── DonationView.swift             # Donazioni opzionali
├── ViewModels/
│   └── CocktailPlannerViewModel.swift # Logica business
└── Services/
    ├── CocktailEngine.swift           # Engine calcoli
    ├── SessionManager.swift           # Persistenza dati
    └── DonationManager.swift          # Gestione donazioni (StoreKit)
```

## 💰 Sistema Donazioni

L'app include un sistema di donazioni opzionali che permette agli utenti di supportare lo sviluppatore:
- ☕️ €1 - Offri un caffè
- ❤️ €3 - Supporta lo sviluppo
- ⭐ €5 - Grazie per il supporto!

**Setup richiesto:** Vedi [GUIDA_DONAZIONI.md](GUIDA_DONAZIONI.md) per istruzioni complete su come configurare i prodotti in-app in App Store Connect.

## 📦 Preparazione per App Store

### 1. Configurazione Base

Nel tuo progetto Xcode:

**General Tab:**
- Display Name: `Cocktail Planner Vicennole`
- Bundle Identifier: `com.tuonome.CocktailPlannerVicennole` (deve essere unico)
- Version: `1.0`
- Build: `1`
- Deployment Target: iOS 15.0

**Signing & Capabilities:**
- Team: Seleziona il tuo Apple Developer Team
- Signing Certificate: Automatic signing (consigliato)

### 2. Assets Required

Crea in `Assets.xcassets`:

#### App Icon (AppIcon)
Dimensioni richieste (tutte in PNG):
- iPhone: 
  - 20pt (2x, 3x): 40x40, 60x60
  - 29pt (2x, 3x): 58x58, 87x87
  - 40pt (2x, 3x): 80x80, 120x120
  - 60pt (2x, 3x): 120x120, 180x180
- iPad:
  - 20pt (1x, 2x): 20x20, 40x40
  - 29pt (1x, 2x): 29x29, 58x58
  - 40pt (1x, 2x): 40x40, 80x80
  - 76pt (1x, 2x): 76x76, 152x152
  - 83.5pt (2x): 167x167
- App Store: 1024x1024 (senza alpha channel)

**Suggerimento Icona:** Usa un'emoji cocktail 🍸 o crea un design con colori vivaci.

### 3. Screenshot per App Store

Dimensioni richieste:
- iPhone 6.7" (iPhone 14 Pro Max): 1290 x 2796
- iPhone 6.5" (iPhone 11 Pro Max): 1242 x 2688
- iPhone 5.5" (opzionale): 1242 x 2208
- iPad Pro 12.9" (3rd gen): 2048 x 2732

**Come creare screenshot:**
```bash
# Avvia il simulatore dal target desiderato
# Usa: Cmd + S per salvare screenshot
# Oppure: Features > Screenshot
```

### 4. Metadati App Store Connect

Prepara questi contenuti:

**Descrizione (max 4000 caratteri):**
```
Cocktail Planner Vicennole - Il tuo assistente personale per eventi perfetti!

Organizza serate indimenticabili con il calcolo preciso di tutti gli ingredienti necessari per i tuoi cocktail preferiti.

✨ CARATTERISTICHE PRINCIPALI:
• 30 cocktail classici pre-configurati
• Categorie: Aperitivo, Festa, Cena, Dopocena
• Calcolo automatico ingredienti
• Distribuzione personalizzabile dei drink
• Checklist spesa interattiva
• Sistema di note per ogni ingrediente
• Salvataggio sessioni per eventi ricorrenti

🍸 COME FUNZIONA:
1. Scegli il contesto della serata
2. Seleziona i cocktail che vuoi servire
3. Indica numero di persone e drink a testa
4. Ottieni la lista spesa completa!

📝 CHECKLIST SMART:
Porta il tuo iPhone al supermercato e spunta gli ingredienti mentre fai shopping. Aggiungi note personalizzate per ricordare marche preferite o formati da acquistare.

💾 SESSIONI SALVATE:
Organizzi spesso lo stesso tipo di evento? Salva la configurazione e riutilizzala con un tap!

Perfetto per: aperitivi in casa, feste tra amici, cene eleganti, eventi aziendali.
```

**Keywords (max 100 caratteri):**
```
cocktail,drink,party,ricette,aperitivo,festa,shopping,ingredienti
```

**Promotional Text (max 170 caratteri):**
```
Organizza eventi perfetti! Calcola automaticamente tutti gli ingredienti per i tuoi cocktail. 30+ ricette classiche incluse. 🍸
```

**Support URL:**
```
https://github.com/fringuello79/cocktail-planner-vicennole
```

**Privacy Policy URL:**
```
https://github.com/fringuello79/cocktail-planner-vicennole/blob/main/PRIVACY.md
```

### 5. Categorie App Store

- Primary: Food & Drink
- Secondary: Lifestyle

### 6. Age Rating

- Rating: 17+ (Frequent/Intense Alcohol, Tobacco, or Drug Use or References)
  - L'app tratta di bevande alcoliche

## 🚀 Processo di Submission

### Step 1: Apple Developer Program

1. Iscriviti a [Apple Developer Program](https://developer.apple.com/programs/) ($99/anno)
2. Completa il processo di verifica (può richiedere 24-48 ore)

### Step 2: Certificati e Provisioning

1. Apri Xcode
2. Preferences > Accounts
3. Aggiungi il tuo Apple ID
4. Seleziona il tuo team
5. Manage Certificates > "+" > Apple Distribution

### Step 3: App Store Connect Setup

1. Vai su [App Store Connect](https://appstoreconnect.apple.com)
2. My Apps > "+" > New App
3. Compila:
   - Platform: iOS
   - Name: Cocktail Planner Vicennole
   - Primary Language: Italian
   - Bundle ID: (seleziona quello creato)
   - SKU: CocktailPlannerVicennole001

### Step 4: Build e Archive

```bash
# In Xcode:
1. Seleziona "Any iOS Device (arm64)" come target
2. Product > Archive
3. Attendi completamento build
4. Window > Organizer
5. Seleziona l'archive
6. Click "Distribute App"
7. Seleziona "App Store Connect"
8. Upload
```

### Step 5: TestFlight (Opzionale ma consigliato)

1. In App Store Connect, vai alla tab TestFlight
2. Aggiungi tester interni (fino a 100)
3. I tester riceveranno invito via email
4. Testa l'app per 1-2 settimane

### Step 6: Submit for Review

1. In App Store Connect, completa tutti i campi richiesti:
   - Screenshots
   - Description
   - Keywords
   - Support URL
   - Privacy Policy
   - Age Rating
2. Seleziona il build da TestFlight
3. Submit for Review

### Step 7: Review Process

- **Timeline:** 1-3 giorni (media: 24 ore)
- **Possibili esiti:**
  - ✅ Approved: L'app è live!
  - ❌ Rejected: Leggi i feedback e correggi
  - ⚠️ Metadata Rejected: Correggi solo descrizione/screenshot

### Common Rejection Reasons da Evitare

1. **Design minimalista:** ✅ La nostra app è ben strutturata
2. **Incomplete information:** ✅ Compila TUTTI i campi
3. **Mancanza Privacy Policy:** ⚠️ CREA IL FILE (vedi sotto)
4. **Bug o crash:** ✅ Testa bene prima di submit
5. **Screenshot non rappresentativi:** ✅ Usa screenshot reali

## 📄 Privacy Policy (OBBLIGATORIA)

Crea file `PRIVACY.md` nella root del repo GitHub:

```markdown
# Privacy Policy - Cocktail Planner Vicennole

**Ultima modifica:** [DATA]

## Raccolta Dati

Cocktail Planner Vicennole NON raccoglie, trasmette o condivide alcun dato personale.

## Dati Locali

- Tutte le sessioni salvate sono memorizzate localmente sul tuo dispositivo
- I dati non vengono trasmessi a server esterni
- Nessun tracking o analytics implementato

## Modifiche

Eventuali modifiche a questa policy saranno comunicate tramite aggiornamento app.

## Contatti

Per domande: [TUO EMAIL]
```

## 🔧 Post-Launch

### Aggiornamenti Futuri

- Export PDF completo
- Widget iOS
- Watchlist ingredienti comuni
- Ricerca cocktail per ingrediente
- Cocktail personalizzati
- Sync iCloud

### Monitoring

1. App Store Connect Analytics
2. Crash Reports in Xcode Organizer
3. User Reviews & Ratings

### Update Process

```bash
# Per ogni update:
1. Incrementa version/build number
2. Product > Archive
3. Upload to App Store Connect
4. Submit new version for review
```

## 📞 Support

- GitHub Issues: [Repository](https://github.com/fringuello79/cocktail-planner-vicennole/issues)
- Email: [TUO EMAIL]

## 📜 License

[Specifica la tua licenza]

---

**Nota:** Questo README copre tutto il processo da sviluppo locale a App Store. Segui i passi nell'ordine per il miglior risultato!
