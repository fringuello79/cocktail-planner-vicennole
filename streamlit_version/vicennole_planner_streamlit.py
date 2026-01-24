"""
Cocktail Planner Vicennole - Complete Web Application
Streamlit version with all features from iOS app
"""

import streamlit as st
import pandas as pd
import json
from datetime import datetime
from zoneinfo import ZoneInfo
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Configure page
st.set_page_config(
    page_title="Cocktail Planner Vicennole",
    page_icon="🍸",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
    }
    .cocktail-category {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1f77b4;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    /* Responsive title - single line on mobile */
    h1 {
        font-size: clamp(1.2rem, 4vw, 2.5rem) !important;
    }
    h3 {
        font-size: clamp(0.8rem, 2.5vw, 1.17rem) !important;
    }
    .ingredient-list {
        overflow-x: auto;
    }
    .ingredient-list label {
        white-space: nowrap;
        display: inline-flex;
        align-items: center;
        justify-content: flex-start;
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

# Logo - reduced to 50% size
col1, col2, col3 = st.columns([3, 2, 3])
with col2:
    st.image("logovicennole.jpeg", use_container_width=True)

# Title
st.title("🍸 Cocktail Planner Vicennole")
st.markdown("### Calcola esattamente cosa comprare per la tua serata")

# Cocktail database - same as iOS app
COCKTAIL_CATALOG = {
    "Aperitivo": [
        "Aperol Spritz", "Campari Spritz", "Americano", "Negroni", 
        "Negroni Sbagliato", "Gin Tonic", "Hugo", "Vermouth Tonic", 
        "Bellini", "Prosecco"
    ],
    "Festa": [
        "Mojito", "Moscow Mule", "Margarita", "Daiquiri", 
        "Cuba Libre", "Paloma", "Gin Lemon", "Vodka Lemon"
    ],
    "Cena": [
        "Old Fashioned", "Whiskey Sour", "Boulevardier", "Martini", 
        "Manhattan", "French 75", "Sidecar"
    ],
    "Dopocena": [
        "Espresso Martini", "Black Russian", "White Russian", 
        "Amaretto Sour", "Irish Coffee"
    ]
}

RECIPES = {
    # APERITIVO
    "Aperol Spritz": {"Prosecco (ml)": 90, "Aperol (ml)": 60, "Soda (ml)": 30},
    "Campari Spritz": {"Prosecco (ml)": 90, "Campari (ml)": 60, "Soda (ml)": 30},
    "Americano": {"Bitter (ml)": 30, "Vermouth rosso (ml)": 30, "Soda (ml)": 60},
    "Negroni": {"Gin (ml)": 30, "Vermouth rosso (ml)": 30, "Bitter (ml)": 30},
    "Negroni Sbagliato": {"Prosecco (ml)": 60, "Vermouth rosso (ml)": 30, "Bitter (ml)": 30},
    "Gin Tonic": {"Gin (ml)": 50, "Acqua tonica (ml)": 100},
    "Hugo": {"Prosecco (ml)": 100, "Soda (ml)": 30, "Sciroppo sambuco (ml)": 20, "Menta (foglie)": 5},
    "Vermouth Tonic": {"Vermouth (ml)": 80, "Acqua tonica (ml)": 100},
    "Bellini": {"Prosecco (ml)": 100, "Purea di pesca (ml)": 50},
    "Prosecco": {"Prosecco (ml)": 120},
    
    # FESTA
    "Mojito": {"Rum bianco (ml)": 50, "Lime (ml)": 20, "Zucchero (g)": 10, "Soda (ml)": 100, "Menta (foglie)": 5},
    "Moscow Mule": {"Vodka (ml)": 50, "Ginger beer (ml)": 120, "Lime (ml)": 10},
    "Margarita": {"Tequila (ml)": 50, "Triple sec (ml)": 20, "Lime (ml)": 20},
    "Daiquiri": {"Rum bianco (ml)": 50, "Lime (ml)": 25, "Zucchero (g)": 10},
    "Cuba Libre": {"Rum (ml)": 50, "Cola (ml)": 120, "Lime (ml)": 10},
    "Paloma": {"Tequila (ml)": 50, "Soda al pompelmo (ml)": 120, "Lime (ml)": 10},
    "Gin Lemon": {"Gin (ml)": 50, "Limonata (ml)": 120},
    "Vodka Lemon": {"Vodka (ml)": 50, "Limonata (ml)": 120},
    
    # CENA
    "Old Fashioned": {"Whiskey (ml)": 50, "Zucchero (g)": 5},
    "Whiskey Sour": {"Whiskey (ml)": 50, "Lime (ml)": 25, "Zucchero (g)": 15},
    "Boulevardier": {"Whiskey (ml)": 30, "Vermouth rosso (ml)": 30, "Bitter (ml)": 30},
    "Martini": {"Gin (ml)": 60, "Vermouth dry (ml)": 10},
    "Manhattan": {"Whiskey (ml)": 50, "Vermouth rosso (ml)": 20},
    "French 75": {"Gin (ml)": 30, "Lime (ml)": 15, "Zucchero (g)": 10, "Prosecco (ml)": 60},
    "Sidecar": {"Cognac (ml)": 50, "Triple sec (ml)": 20, "Lime (ml)": 20},
    
    # DOPOCENA
    "Espresso Martini": {"Vodka (ml)": 40, "Caffè espresso (ml)": 30, "Liquore al caffè (ml)": 20},
    "Black Russian": {"Vodka (ml)": 50, "Liquore al caffè (ml)": 20},
    "White Russian": {"Vodka (ml)": 50, "Liquore al caffè (ml)": 20, "Panna (ml)": 30},
    "Amaretto Sour": {"Amaretto (ml)": 60, "Lime (ml)": 30},
    "Irish Coffee": {"Whiskey (ml)": 40, "Caffè (ml)": 90, "Zucchero (g)": 10, "Panna (ml)": 30}
}

TAB_LABELS = ["📝 Pianifica", "🛒 Lista Spesa", "ℹ️ Info"]
TAB_PIANIFICA, TAB_LISTA_SPESA, TAB_INFO = TAB_LABELS

# Helper function for formatting quantities
def format_quantity(ingredient, quantity):
    """Format ingredient quantity with appropriate unit."""
    unit = ingredient.split('(')[-1].replace(')', '') if '(' in ingredient else ''
    if unit in ['ml', 'g']:
        return f"{quantity:.0f} {unit}"
    elif unit == 'foglie':
        return f"{quantity:.0f} {unit}"
    else:
        return f"{quantity:.1f}"

# Initialize session state
if 'selected_cocktails' not in st.session_state:
    st.session_state.selected_cocktails = []
if 'ingredients' not in st.session_state:
    st.session_state.ingredients = {}
if 'checklist' not in st.session_state:
    st.session_state.checklist = {}
if 'notes' not in st.session_state:
    st.session_state.notes = {}
if 'calculated' not in st.session_state:
    st.session_state.calculated = False
if 'saved_sessions' not in st.session_state:
    st.session_state.saved_sessions = []
if 'distribution' not in st.session_state:
    st.session_state.distribution = {}
if 'num_people' not in st.session_state:
    st.session_state.num_people = 10
if 'drinks_per_person' not in st.session_state:
    st.session_state.drinks_per_person = 3
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = TAB_PIANIFICA

# Sidebar for saved sessions
with st.sidebar:
    st.header("📁 Sessioni Salvate")
    
    if st.session_state.saved_sessions:
        session_names = [s['name'] for s in st.session_state.saved_sessions]
        selected_session = st.selectbox("Carica una sessione:", [""] + session_names)
        
        if selected_session:
            session = next(s for s in st.session_state.saved_sessions if s['name'] == selected_session)
            if st.button("📥 Carica Sessione"):
                st.session_state.selected_cocktails = session['cocktails']
                st.session_state.calculated = False
                st.success(f"Sessione '{selected_session}' caricata!")
    else:
        st.info("Nessuna sessione salvata")
    
    st.divider()
    
    # Save current session
    if st.session_state.selected_cocktails:
        st.subheader("💾 Salva Sessione Corrente")
        session_name = st.text_input("Nome sessione:", key="save_session_name")
        if st.button("💾 Salva"):
            if session_name:
                new_session = {
                    'name': session_name,
                    'cocktails': st.session_state.selected_cocktails.copy(),
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                st.session_state.saved_sessions.append(new_session)
                st.success(f"Sessione '{session_name}' salvata!")
            else:
                st.error("Inserisci un nome per la sessione")

# Main content
active_tab = st.radio(
    "Sezione",
    TAB_LABELS,
    index=TAB_LABELS.index(st.session_state.active_tab),
    horizontal=True
)
st.session_state.active_tab = active_tab

if active_tab == TAB_PIANIFICA:
    st.header("1️⃣ Parametri Evento")
    
    col1, col2 = st.columns(2)
    with col1:
        num_people = st.number_input("👥 Numero di persone", min_value=1, value=st.session_state.num_people, step=1)
        st.session_state.num_people = num_people
    with col2:
        drinks_per_person = st.number_input("🍹 Cocktail a testa", min_value=1, value=st.session_state.drinks_per_person, step=1)
        st.session_state.drinks_per_person = drinks_per_person
    
    total_drinks = num_people * drinks_per_person
    st.info(f"**Totale cocktail da preparare: {total_drinks}**")
    
    st.divider()
    
    st.header("2️⃣ Selezione Cocktail")
    
    # Initialize selected_cocktails_set in session state if not present
    if 'selected_cocktails_set' not in st.session_state:
        st.session_state.selected_cocktails_set = set()
    
    # Distribution preset
    distribution_mode = st.radio(
        "Modalità distribuzione:",
        ["Equa tra cocktail selezionati", "Con cocktail principale"],
        horizontal=True
    )
    
    main_cocktail = None
    main_cocktail_percentage = 50
    
    st.divider()
    
    # Cocktail selection by category
    selected_cocktails = []
    
    for category, cocktails in COCKTAIL_CATALOG.items():
        st.markdown(f'<div class="cocktail-category">🍸 {category}</div>', unsafe_allow_html=True)
        cols = st.columns(min(len(cocktails), 4))
        
        for idx, cocktail in enumerate(cocktails):
            with cols[idx % len(cols)]:
                # Check if cocktail is in the set
                is_checked = cocktail in st.session_state.selected_cocktails_set
                checked = st.checkbox(cocktail, value=is_checked, key=f"cocktail_{cocktail}")
                
                # Update the set based on checkbox state
                if checked:
                    selected_cocktails.append(cocktail)
                    st.session_state.selected_cocktails_set.add(cocktail)
                else:
                    # If unchecked, remove from set
                    st.session_state.selected_cocktails_set.discard(cocktail)
    
    # Store the list of selected cocktails
    st.session_state.selected_cocktails = selected_cocktails
    
    if distribution_mode == "Con cocktail principale":
        if selected_cocktails:
            col1, col2 = st.columns(2)
            with col1:
                main_cocktail = st.selectbox("Cocktail principale:", sorted(selected_cocktails))
            with col2:
                main_cocktail_percentage = st.slider("Percentuale cocktail principale:", 30, 70, 50, 5)
        else:
            st.info("Seleziona i cocktail per scegliere quello principale.")

    # Display selected cocktails summary - show what's actually selected
    if st.session_state.selected_cocktails:
        st.markdown("**Cocktail selezionati:**")
        st.markdown(", ".join(sorted(st.session_state.selected_cocktails)))
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Calcola Ingredienti", type="primary", use_container_width=True):
        if not selected_cocktails:
            st.error("⚠️ Seleziona almeno un cocktail!")
        else:
            # Calculate distribution
            num_cocktails = len(selected_cocktails)
            distribution = {}
            
            if distribution_mode == "Equa tra cocktail selezionati":
                drinks_per_cocktail = total_drinks / num_cocktails
                distribution = {c: drinks_per_cocktail for c in selected_cocktails}
            else:
                if main_cocktail in selected_cocktails:
                    main_drinks = total_drinks * (main_cocktail_percentage / 100)
                    remaining_drinks = total_drinks - main_drinks
                    other_cocktails = [c for c in selected_cocktails if c != main_cocktail]
                    
                    distribution[main_cocktail] = main_drinks
                    if other_cocktails:
                        drinks_per_other = remaining_drinks / len(other_cocktails)
                        for c in other_cocktails:
                            distribution[c] = drinks_per_other
                else:
                    drinks_per_cocktail = total_drinks / num_cocktails
                    distribution = {c: drinks_per_cocktail for c in selected_cocktails}
            
            # Calculate ingredients
            ingredients_total = {}
            for cocktail, num_drinks in distribution.items():
                recipe = RECIPES.get(cocktail, {})
                for ingredient, quantity in recipe.items():
                    ingredients_total[ingredient] = ingredients_total.get(ingredient, 0) + (quantity * num_drinks)
            
            # Initialize checklist and notes
            st.session_state.ingredients = ingredients_total
            st.session_state.checklist = {ing: False for ing in ingredients_total.keys()}
            st.session_state.notes = {ing: "" for ing in ingredients_total.keys()}
            st.session_state.calculated = True
            st.session_state.distribution = distribution
            
            st.success("✅ Calcolo completato! Usa il pulsante qui sotto o la tab '🛒 Lista Spesa' per vedere i risultati.")

    if st.session_state.calculated:
        if st.button("🛒 Vai alla Lista Spesa", use_container_width=True):
            st.session_state.active_tab = TAB_LISTA_SPESA
            st.rerun()

if active_tab == TAB_LISTA_SPESA:
    if not st.session_state.calculated:
        st.warning("⚠️ Calcola prima gli ingredienti nella tab 'Pianifica'")
    else:
        st.header("🛒 Lista della Spesa")
        italy_now = datetime.now(ZoneInfo("Europe/Rome"))
        
        # Summary
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Ingredienti totali", len(st.session_state.ingredients))
        with col2:
            checked = sum(1 for v in st.session_state.checklist.values() if v)
            st.metric("Spuntati", f"{checked}/{len(st.session_state.checklist)}")
        with col3:
            st.metric("Cocktail selezionati", len(st.session_state.selected_cocktails))
        
        st.divider()
        
        # Display distribution
        st.subheader("📊 Distribuzione Cocktail")
        total_drinks = st.session_state.num_people * st.session_state.drinks_per_person
        dist_data = []
        for cocktail, num_drinks in st.session_state.distribution.items():
            dist_data.append({
                "Cocktail": cocktail,
                "Numero": f"{num_drinks:.1f}",
                "Percentuale": f"{(num_drinks/total_drinks*100):.1f}%"
            })
        st.dataframe(pd.DataFrame(dist_data), width='stretch', hide_index=True)
        
        st.divider()
        
        # Interactive checklist
        st.subheader("✅ Checklist Interattiva")
        
        # Reset checklist button
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("🔄 Reset Checklist"):
                st.session_state.checklist = {ing: False for ing in st.session_state.ingredients.keys()}
        
        st.markdown("---")
        
        # Display ingredients with checkboxes and notes
        st.markdown('<div class="ingredient-list">', unsafe_allow_html=True)
        for ingredient, quantity in sorted(st.session_state.ingredients.items()):
            ingredient_name = ingredient.split('(')[0].strip()
            formatted_qty = format_quantity(ingredient, quantity)
            label = f"{ingredient_name} - {formatted_qty}"
            
            checked = st.checkbox(
                label,
                value=st.session_state.checklist.get(ingredient, False),
                key=f"check_{ingredient}"
            )
            st.session_state.checklist[ingredient] = checked
            
            # Row 2: Notes on separate row, full width
            note = st.text_input(
                f"Note per {ingredient_name}",
                value=st.session_state.notes.get(ingredient, ""),
                key=f"note_{ingredient}",
                label_visibility="collapsed",
                placeholder="Note..."
            )
            st.session_state.notes[ingredient] = note
            st.markdown("---")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.divider()
        
        # Export PDF
        st.subheader("📄 Download Lista Spesa")
        
        def create_pdf():
            # Get values from session state
            num_people = st.session_state.num_people
            drinks_per_person = st.session_state.drinks_per_person
            total_drinks = num_people * drinks_per_person
            
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=A4,
                                   rightMargin=2*cm, leftMargin=2*cm,
                                   topMargin=2*cm, bottomMargin=2*cm)
            
            elements = []
            styles = getSampleStyleSheet()
            
            # Title
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#1f77b4'),
                spaceAfter=30,
                alignment=TA_CENTER
            )
            elements.append(Paragraph("🍸 Lista Spesa - Cocktail Planner Vicennole", title_style))
            elements.append(Spacer(1, 0.5*cm))
            
            # Event info
            info_style = styles['Normal']
            elements.append(Paragraph(f"<b>Data:</b> {italy_now.strftime('%d/%m/%Y %H:%M')}", info_style))
            elements.append(Paragraph(f"<b>Persone:</b> {num_people}", info_style))
            elements.append(Paragraph(f"<b>Cocktail a testa:</b> {drinks_per_person}", info_style))
            elements.append(Paragraph(f"<b>Totale cocktail:</b> {total_drinks}", info_style))
            elements.append(Spacer(1, 0.5*cm))
            
            # Cocktails selected
            elements.append(Paragraph("<b>Cocktail selezionati:</b>", info_style))
            cocktails_text = ", ".join(st.session_state.selected_cocktails)
            elements.append(Paragraph(cocktails_text, info_style))
            elements.append(Spacer(1, 1*cm))
            
            # Distribution table
            elements.append(Paragraph("<b>Distribuzione Cocktail:</b>", styles['Heading2']))
            elements.append(Spacer(1, 0.3*cm))
            
            dist_data = [['Cocktail', 'Quantità', '%']]
            for cocktail, num_drinks in st.session_state.distribution.items():
                dist_data.append([
                    cocktail,
                    f"{num_drinks:.1f}",
                    f"{(num_drinks/total_drinks*100):.1f}%"
                ])
            
            dist_table = Table(dist_data, colWidths=[8*cm, 3*cm, 2*cm])
            dist_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(dist_table)
            elements.append(Spacer(1, 1*cm))
            
            # Ingredients table
            elements.append(Paragraph("<b>Lista Ingredienti:</b>", styles['Heading2']))
            elements.append(Spacer(1, 0.3*cm))
            
            data = [['☐', 'Ingrediente', 'Quantità', 'Note']]
            
            for ingredient, quantity in sorted(st.session_state.ingredients.items()):
                # Format quantity using helper function
                formatted_qty = format_quantity(ingredient, quantity)
                
                checkbox = '☑' if st.session_state.checklist.get(ingredient, False) else '☐'
                note = st.session_state.notes.get(ingredient, "")
                
                data.append([checkbox, ingredient, formatted_qty, note])
            
            table = Table(data, colWidths=[1*cm, 7*cm, 3*cm, 5*cm])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
            ]))
            
            elements.append(table)
            elements.append(Spacer(1, 1*cm))
            
            # Footer
            footer_style = ParagraphStyle(
                'Footer',
                parent=styles['Normal'],
                fontSize=8,
                textColor=colors.grey,
                alignment=TA_CENTER
            )
            elements.append(Paragraph("Generato da Cocktail Planner Vicennole", footer_style))
            
            doc.build(elements)
            buffer.seek(0)
            return buffer
        
        pdf_buffer = create_pdf()
        
        st.download_button(
            label="📥 Scarica Lista Spesa (PDF)",
            data=pdf_buffer,
            file_name=f"lista_spesa_vicennole_{italy_now.strftime('%Y%m%d_%H%M')}.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True
        )
        
        st.divider()
        
        st.info("💡 Per modificare i parametri o cambiare cocktail, clicca sulla tab '📝 Pianifica' in alto.")

if active_tab == TAB_INFO:
    st.header("ℹ️ Informazioni")
    
    st.markdown("""
    ### 🍸 Cocktail Planner Vicennole
    
    Questa applicazione ti aiuta a pianificare eventi con cocktail calcolando automaticamente 
    tutti gli ingredienti necessari.
    
    #### ✨ Caratteristiche:
    - **30 Cocktail Classici** in 4 categorie (Aperitivo, Festa, Cena, Dopocena)
    - **Calcolo Automatico** degli ingredienti basato su numero di persone e drink
    - **Distribuzione Intelligente** con modalità equa o cocktail principale
    - **Checklist Interattiva** per spuntare gli ingredienti durante la spesa
    - **Sistema Note** per aggiungere annotazioni a ogni ingrediente
    - **Salvataggio Sessioni** per riutilizzare configurazioni
    - **Export PDF** completo con tutti i dettagli
    
    #### 📋 Cocktail Disponibili:
    """)
    
    for category, cocktails in COCKTAIL_CATALOG.items():
        st.markdown(f"**{category}** ({len(cocktails)})")
        st.markdown(", ".join(cocktails))
        st.markdown("")
    
    st.markdown("""
    #### 🚀 Come Usare:
    1. Vai alla tab **Pianifica**
    2. Inserisci numero di persone e cocktail a testa
    3. Scegli la modalità di distribuzione
    4. Seleziona i cocktail desiderati
    5. Clicca su **Calcola Ingredienti**
    6. Vai alla tab **Lista Spesa** per vedere i risultati
    7. Usa la checklist interattiva durante la spesa
    8. Aggiungi note se necessario
    9. Scarica il PDF per avere la lista stampata
    
    #### 💾 Sessioni:
    Puoi salvare la tua configurazione di cocktail nella sidebar e ricaricarla in seguito.
    
    ---
    
    *Fatto con ❤️ e 🍸 - Cocktail Planner Vicennole*
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    🍸 Cocktail Planner Vicennole | Versione Web Completa
</div>
""", unsafe_allow_html=True)
