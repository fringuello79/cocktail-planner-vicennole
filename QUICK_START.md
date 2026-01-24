# 🚀 Quick Start - Italiano

## Hai la versione Streamlit e vuoi passare a iOS?

**Perfetto! Ecco i passi da seguire:**

### Opzione 1: Voglio solo testare l'app (GRATIS)

1. **Scarica Xcode** (gratis dall'App Store del Mac)
2. **Crea nuovo progetto:**
   - Apri Xcode
   - File > New > Project
   - iOS > App
   - Nome: "Cocktail Planner Vicennole"
   - Interface: SwiftUI
   - Language: Swift

3. **Importa i file:**
   - Trascina la cartella `iOS/CocktailPlannerVicennole/Models/` nel progetto
   - Trascina la cartella `iOS/CocktailPlannerVicennole/Views/` nel progetto
   - Trascina la cartella `iOS/CocktailPlannerVicennole/ViewModels/` nel progetto
   - Trascina la cartella `iOS/CocktailPlannerVicennole/Services/` nel progetto
   - Trascina il file `iOS/CocktailPlannerVicennole/CocktailPlannerVicennoleApp.swift`
   - Quando chiede, seleziona "Copy items if needed"

4. **Testa sul simulatore:**
   - In alto a sinistra, seleziona "iPhone 14 Pro" (o simile)
   - Clicca il bottone Play ▶
   - L'app si avvia nel simulatore!

5. **Testa sul tuo iPhone (ancora GRATIS):**
   - Collega il tuo iPhone al Mac
   - Seleziona il tuo iPhone invece del simulatore
   - In Xcode: Signing & Capabilities > Team > Seleziona il tuo Apple ID
   - Clicca Play ▶
   - Sul tuo iPhone: Impostazioni > Generali > Gestione dispositivo > Autorizza il tuo account
   - Riapri l'app sul telefono

**Costo totale: 0€** (puoi testare su dispositivi personali gratuitamente)

---

### Opzione 2: Voglio pubblicarla su App Store

**Costo: $99/anno per Apple Developer Program**

1. **Completa tutti i passi dell'Opzione 1** (per assicurarti che funzioni)

2. **Iscriviti ad Apple Developer:**
   - Vai su https://developer.apple.com/programs/
   - Click "Enroll"
   - Scegli "Individual" (se sei tu personalmente) o "Organization" (se hai un'azienda)
   - Paga $99/anno
   - Attendi verifica (24-48 ore)

3. **Prepara gli asset:**
   - **Icona app:** 1024x1024 pixel
     - Puoi usare https://appicon.co per generare tutte le dimensioni
     - Suggerimento: usa emoji 🍸 o crea un design semplice
   - **Screenshot:** Avvia l'app nel simulatore e premi Cmd+S
     - Fai screenshot di: home, selezione cocktail, risultati, checklist

4. **Configura App Store Connect:**
   - Vai su https://appstoreconnect.apple.com
   - My Apps > "+" > New App
   - Compila tutti i campi (usa le informazioni da README_iOS.md)
   - Carica screenshot
   - Privacy Policy URL: usa il file PRIVACY.md da questo repo
     - Puoi hostarlo gratis su GitHub Pages

5. **Upload app:**
   - In Xcode: Product > Archive
   - Attendi la build (2-5 minuti)
   - Quando finisce: Window > Organizer
   - Click "Distribute App" > "App Store Connect"
   - Segui il wizard (tutto automatico)

6. **Submit for Review:**
   - Torna su App Store Connect
   - Compila tutti i campi rimanenti
   - Click "Submit for Review"
   - Attendi 1-3 giorni

7. **🎉 La tua app è live!**

---

## ⏱️ Quanto tempo ci vuole?

| Fase | Tempo | Note |
|------|-------|------|
| Setup Xcode + Import | 15 min | Una volta sola |
| Test locale | 5 min | Ogni build |
| Test su device | 10 min | Prima volta |
| Preparazione asset | 1-2 ore | Screenshot, icona |
| Apple Developer signup | 2-3 giorni | Verifica account |
| Upload + Submit | 30 min | + 1-3 giorni review |
| **TOTALE** | **~5 giorni** | Dal nulla all'App Store |

---

## 💡 Consigli Pratici

### Non hai un Mac?
❌ Purtroppo **serve un Mac** per sviluppare app iOS native.

Alternative:
- Continua con Streamlit (funziona su Windows/Linux)
- Usa un servizio cloud (es. MacStadium, MacInCloud)
- React Native (ma richiede più lavoro di conversione)

### Non hai un iPhone?
✅ Puoi testare completamente nel **simulatore** (gratis, incluso in Xcode)

### Non vuoi pagare $99/anno?
✅ Puoi:
- Testare su dispositivi personali gratuitamente (senza pubblicare)
- Condividere con amici tramite TestFlight (fino a 100 tester)
- Hostare la versione Streamlit su un server (Heroku, Railway, ecc.)

### Voglio modificare l'app?
✅ Tutti i file Swift sono commentati in italiano!
- `Models/` → Dati (cocktail, ricette)
- `Views/` → Interfaccia utente
- `ViewModels/` → Logica dell'app
- `Services/` → Calcoli e salvataggio

---

## 🆘 Problemi Comuni

### "No signing certificate"
**Soluzione:**
```
Xcode > Preferences > Accounts > Download Manual Profiles
Signing & Capabilities > Automatic signing ✓
```

### "App not opening on iPhone"
**Soluzione:**
```
iPhone: Impostazioni > Generali > VPN e gestione dispositivo
Trust developer: [Tuo Apple ID]
```

### "Archive is grayed out"
**Soluzione:**
```
In alto a sinistra, seleziona "Any iOS Device (arm64)" invece di simulatore
Product > Clean Build Folder
Product > Archive
```

---

## 📚 Dove Trovare Aiuto?

1. **Leggi la guida completa:** [GUIDA_CONVERSIONE_iOS.md](GUIDA_CONVERSIONE_iOS.md)
2. **Documentazione tecnica:** [iOS/README_iOS.md](iOS/README_iOS.md)
3. **Apri un issue:** [GitHub Issues](https://github.com/fringuello79/cocktail-planner-vicennole/issues)
4. **Tutorial Apple:** https://developer.apple.com/tutorials/swiftui

---

## ✅ Checklist Finale (Prima di Submit)

- [ ] App testata su simulatore
- [ ] App testata su device fisico
- [ ] Nessun crash o bug evidenti
- [ ] Icona app creata (1024x1024)
- [ ] Screenshot preparati (almeno 3)
- [ ] Privacy Policy pubblicata
- [ ] Apple Developer account attivo
- [ ] Tutti i campi App Store Connect compilati
- [ ] Age rating corretto (17+ per alcolici)
- [ ] Build caricata e processata

---

**Hai domande? Apri una Issue su GitHub!** 🚀

Buona fortuna! 🍸📱
