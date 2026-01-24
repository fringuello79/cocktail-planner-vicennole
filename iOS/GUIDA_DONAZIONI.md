# Guida Setup Donazioni In-App

## Funzionalità Donazioni

L'app include un sistema di donazioni opzionali che permette agli utenti di supportare lo sviluppatore con contributi volontari di €1, €3 o €5.

### Caratteristiche

- ✅ **Completamente opzionale**: Gli utenti possono ignorare o chiudere la sezione
- ✅ **Collapsabile**: La sezione può essere espansa/compressa con un tap
- ✅ **Tre livelli**: €1 (caffè), €3 (cuore), €5 (stella)
- ✅ **StoreKit 2**: Integrazione nativa con sistema acquisti Apple
- ✅ **Fallback graceful**: Funziona anche senza configurazione StoreKit
- ✅ **Posizionamento strategico**: Appare dopo la lista ingredienti nel ResultsView

### Posizione nell'App

La sezione donazioni appare nella schermata "Risultato" (ResultsView), subito dopo la lista "Ingredienti totali" e prima della "Checklist spesa". Questo è il momento ideale perché:
- L'utente ha appena ottenuto il valore principale dell'app (lista ingredienti)
- È in uno stato positivo dopo aver visto risultati utili
- Non interrompe il flusso principale dell'app

## Setup In-App Purchases (Obbligatorio per App Store)

### 1. Configurazione App Store Connect

#### Step 1: Crea l'Agreement
1. Vai su [App Store Connect](https://appstoreconnect.apple.com)
2. Agreements, Tax, and Banking
3. Completa tutti i campi richiesti:
   - Informazioni bancarie
   - Informazioni fiscali
   - Contratto Paid Applications

#### Step 2: Crea i Prodotti In-App
1. App Store Connect > My Apps > [Tua App]
2. Features > In-App Purchases
3. Click "+" per creare nuovo prodotto

**Prodotto 1: Donazione Piccola**
```
Product Type: Consumable
Reference Name: Donazione Piccola
Product ID: com.vicennole.cocktailplanner.donation.small
Price: €0.99 o €1.09 (Tier 1)
Description (IT): Offri un caffè allo sviluppatore
Description (EN): Buy the developer a coffee
```

**Prodotto 2: Donazione Media**
```
Product Type: Consumable
Reference Name: Donazione Media
Product ID: com.vicennole.cocktailplanner.donation.medium
Price: €2.99 (Tier 3)
Description (IT): Supporta lo sviluppo dell'app
Description (EN): Support app development
```

**Prodotto 3: Donazione Grande**
```
Product Type: Consumable
Reference Name: Donazione Grande
Product ID: com.vicennole.cocktailplanner.donation.large
Price: €4.99 (Tier 5)
Description (IT): Grazie per il tuo generoso supporto!
Description (EN): Thanks for your generous support!
```

#### Step 3: Screenshot per Review
Per ogni prodotto, carica uno screenshot che mostra:
- La sezione donazioni nell'app
- Il bottone specifico evidenziato
- Usa il simulatore iPhone per gli screenshot

### 2. Configurazione Xcode

#### Step 1: Aggiungi Capability
1. Apri il progetto in Xcode
2. Seleziona target "Cocktail Planner Vicennole"
3. Tab "Signing & Capabilities"
4. Click "+" > "In-App Purchase"

#### Step 2: StoreKit Configuration (Test Locale)
1. File > New > File
2. Seleziona "StoreKit Configuration File"
3. Nome: `DonationProducts.storekit`
4. Aggiungi i 3 prodotti con gli stessi ID di App Store Connect

**Esempio configurazione:**
```json
{
  "identifier" : "com.vicennole.cocktailplanner.donation.small",
  "type" : "Consumable",
  "displayName" : "Donazione Piccola",
  "price" : 0.99
}
```

#### Step 3: Schema Configuration per Test
1. Product > Scheme > Edit Scheme
2. Run > Options
3. StoreKit Configuration: Seleziona `DonationProducts.storekit`

### 3. Test delle Donazioni

#### Test in Simulatore (Senza Transazioni Reali)
1. Usa lo StoreKit Configuration file
2. Le donazioni funzioneranno ma non ci saranno transazioni reali
3. Debug > StoreKit > Manage Transactions per vedere acquisti test

#### Test su Device (Sandbox)
1. Crea un Sandbox Test Account:
   - App Store Connect > Users and Access > Sandbox Testers
   - Aggiungi nuovo tester con email dedicata
2. Sul device iOS:
   - Settings > App Store > Sandbox Account
   - Login con account sandbox
3. Build e test l'app
4. Le donazioni useranno account sandbox (no soldi reali)

#### Verifica Funzionamento
```swift
// Nel simulatore, verifica che:
✅ La sezione "Supporta lo sviluppo" appare
✅ Clicking espande/comprime la sezione
✅ I 3 bottoni sono visibili
✅ Clicking mostra alert di ringraziamento
✅ Prezzi corretti vengono mostrati (se configurato)
```

### 4. Fallback Graceful

L'app include un fallback per quando StoreKit non è disponibile:
- Mostra bottoni con importi fissi (1€, 3€, 5€)
- Clicking mostra un messaggio di ringraziamento
- Include nota: "Le donazioni saranno disponibili nella versione App Store"

Questo permette di:
- ✅ Testare l'UI senza configurare StoreKit
- ✅ Funzionare in ambienti dove StoreKit non è disponibile
- ✅ Non bloccare l'app se la configurazione StoreKit fallisce

## Codice Implementato

### File Creati

1. **DonationManager.swift** (`Services/`)
   - Gestisce il caricamento prodotti da StoreKit
   - Gestisce il processo di acquisto
   - Verifica le transazioni
   - Gestisce gli stati (idle, purchasing, success, failed)

2. **DonationView.swift** (`Views/`)
   - UI collapsabile per le donazioni
   - 3 bottoni con icone distintive
   - Alert di ringraziamento post-donazione
   - Fallback quando StoreKit non è disponibile

3. **ResultsView.swift** (modificato)
   - Integra DonationView dopo "Ingredienti totali"
   - Posizionamento strategico per massimizzare conversioni

### Product IDs Utilizzati

```swift
static let productIDs = [
    "com.vicennole.cocktailplanner.donation.small",   // €1
    "com.vicennole.cocktailplanner.donation.medium",  // €3
    "com.vicennole.cocktailplanner.donation.large"    // €5
]
```

**IMPORTANTE**: Questi ID devono corrispondere esattamente a quelli creati in App Store Connect!

## Best Practices

### Design
- ✅ Sezione collassata di default (non invadente)
- ✅ Colori soft (blu chiaro) per non distrarre
- ✅ Icone intuitive (caffè, cuore, stella)
- ✅ Messaggio positivo e ringraziamento

### UX
- ✅ Mai obbligatorio o bloccante
- ✅ Facilmente ignorabile
- ✅ Feedback immediato (alert ringraziamento)
- ✅ Non richiesto ripetutamente

### Legale
- ✅ Descrizione chiara: "donazione volontaria"
- ✅ No rimborsi (standard per donazioni)
- ✅ Conforme alle linee guida Apple per donazioni in-app

## Checklist Pre-Release

Prima di pubblicare su App Store:

- [ ] Tutti i 3 prodotti creati in App Store Connect
- [ ] Product IDs corrispondono al codice
- [ ] Screenshot caricati per ogni prodotto
- [ ] Prezzi configurati correttamente (€0.99, €2.99, €4.99)
- [ ] Descrizioni in italiano e inglese complete
- [ ] In-App Purchase capability aggiunta in Xcode
- [ ] Agreement bancario completato in App Store Connect
- [ ] Testato con account Sandbox
- [ ] Alert di ringraziamento funziona
- [ ] UI testata su iPhone/iPad di diverse dimensioni

## Troubleshooting

### "Unable to complete purchase"
- Verifica che il Sandbox Account sia configurato
- Logout/login dall'account sandbox sul device
- Controlla che i Product IDs siano corretti

### "Products array is empty"
- Verifica connessione internet
- Controlla che i prodotti siano "Ready to Submit" in App Store Connect
- Attendi qualche minuto (propagazione può richiedere tempo)
- Usa StoreKit Configuration file per test locale

### "Invalid Product ID"
- Verifica che gli ID in DonationManager corrispondano ad App Store Connect
- Controlla che il Bundle ID dell'app sia corretto
- Verifica che In-App Purchase capability sia attiva

### Donazioni non appaiono nell'app
- Verifica che DonationView sia importato in ResultsView
- Controlla che non ci siano errori di compilazione
- Usa Debug > View Hierarchy per verificare che la view sia presente

## Monitoraggio Post-Launch

Dopo il lancio, monitora:
1. **Sales and Trends** in App Store Connect
   - Quante donazioni vengono effettuate
   - Quale importo è più popolare

2. **Crash Reports**
   - Verifica che non ci siano crash legati a StoreKit
   - Controlla i log per errori di caricamento prodotti

3. **User Reviews**
   - Feedback sulla feature di donazione
   - Richieste per altri importi o opzioni

## Miglioramenti Futuri

Possibili aggiunte:
- 💡 Importi personalizzati
- 💡 Donazioni ricorrenti (subscription)
- 💡 Unlock di feature premium con donazioni
- 💡 Badge o riconoscimenti per donatori
- 💡 Statistiche donazioni totali (privacy-preserving)

---

**Nota:** Le donazioni sono completamente opzionali e non influenzano le funzionalità core dell'app. Tutti gli utenti hanno accesso completo a tutte le features, indipendentemente dalle donazioni.
