
# cocktail_planner_vicennole.py
# Revisione 1.0 - Creatore: ChatGPT x [Utente]

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cocktail Planner Vicennole", layout="centered")

st.title("🍸 Cocktail Planner Vicennole")
st.subheader("Calcola esattamente cosa comprare per la tua serata")

st.markdown("Inserisci il numero di persone e il numero di cocktail a testa, poi scegli le percentuali per ciascun cocktail.")

# Input principali
persone = st.number_input("Numero di persone", min_value=1, value=5)
cocktail_per_persona = st.number_input("Cocktail a testa", min_value=1, value=3)

# Scelte cocktail
st.markdown("### Percentuale cocktail preferiti (%)")
col1, col2 = st.columns(2)
with col1:
    perc_gt = st.slider("Gin Tonic", 0, 100, 20)
    perc_mojito = st.slider("Mojito", 0, 100, 20)
    perc_spritz = st.slider("Spritz", 0, 100, 20)
with col2:
    perc_negroni = st.slider("Negroni", 0, 100, 20)
    perc_margarita = st.slider("Margarita", 0, 100, 10)
    perc_hugo = st.slider("Hugo", 0, 100, 10)

# Verifica percentuali
tot_perc = perc_gt + perc_mojito + perc_spritz + perc_negroni + perc_margarita + perc_hugo
if tot_perc != 100:
    st.error("⚠️ La somma delle percentuali deve essere 100%. Attualmente è: {}%".format(tot_perc))
    st.stop()

# Ricette cocktail
ricette = {
    "Gin Tonic": {"Gin (ml)": 50, "Acqua tonica (ml)": 100},
    "Mojito": {"Rum (ml)": 50, "Lime (ml)": 20, "Zucchero (g)": 10, "Soda (ml)": 100, "Menta (foglie)": 5},
    "Spritz": {"Prosecco (ml)": 60, "Aperol (ml)": 40, "Soda (ml)": 20},
    "Negroni": {"Gin (ml)": 30, "Vermouth rosso (ml)": 30, "Bitter (ml)": 30},
    "Margarita": {"Tequila (ml)": 50, "Triple sec (ml)": 20, "Lime (ml)": 20},
    "Hugo": {"Prosecco (ml)": 100, "Soda (ml)": 30, "Sciroppo sambuco (ml)": 20, "Menta (foglie)": 5}
}

percentuali = {
    "Gin Tonic": perc_gt,
    "Mojito": perc_mojito,
    "Spritz": perc_spritz,
    "Negroni": perc_negroni,
    "Margarita": perc_margarita,
    "Hugo": perc_hugo
}

# Calcolo totale ingredienti
totale_cocktail = persone * cocktail_per_persona
ingredienti_totali = {}

for nome, percent in percentuali.items():
    n_drink = totale_cocktail * (percent / 100)
    for ingrediente, quantita in ricette[nome].items():
        ingredienti_totali[ingrediente] = ingredienti_totali.get(ingrediente, 0) + quantita * n_drink

# Mostra risultati
st.markdown("## 🧾 Ingredienti Totali da Comprare")
df = pd.DataFrame(list(ingredienti_totali.items()), columns=["Ingrediente", "Quantità Totale"])
st.dataframe(df)

st.success("Calcolo completato con successo! 🍹")
