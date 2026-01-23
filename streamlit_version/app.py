# Cocktail Planner Vicennole - Streamlit Version
# Complete application with PDF export capability

import streamlit as st
import json
import os
from datetime import datetime
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Page configuration
st.set_page_config(
    page_title="🍸 Cocktail Planner Vicennole",
    page_icon="🍸",
    layout="wide"
)

# Initialize session state
if 'calculated' not in st.session_state:
    st.session_state.calculated = False
if 'ingredients_total' not in st.session_state:
    st.session_state.ingredients_total = {}
if 'distribution' not in st.session_state:
    st.session_state.distribution = {}
if 'checklist' not in st.session_state:
    st.session_state.checklist = {}
if 'notes' not in st.session_state:
    st.session_state.notes = {}
if 'selected_cocktails' not in st.session_state:
    st.session_state.selected_cocktails = set()

# Cocktail Database
COCKTAIL_CATEGORIES = {
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
        "Old Fashioned", "Whiskey Sour", "Boulevardier", 
        "Martini", "Manhattan", "French 75", "Sidecar"
    ],
    "Dopocena": [
        "Espresso Martini", "Black Russian", "White Russian", 
        "Amaretto Sour", "Irish Coffee"
    ]
}

# Recipes
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

def format_quantity(value):
    """Format quantity for display"""
    if value >= 1000:
        liters = value / 1000
        if liters == int(liters):
            return f"{int(liters)} L"
        else:
            return f"{liters:.2f} L"
    elif value == int(value):
        return f"{int(value)}"
    else:
        return f"{value:.1f}"

def calculate_ingredients(people, drinks_per_person, selected_cocktails, distribution_mode, main_cocktail=None):
    """Calculate total ingredients needed"""
    total_drinks = people * drinks_per_person
    n_cocktails = len(selected_cocktails)
    
    if n_cocktails == 0:
        return {}, {}
    
    # Calculate distribution
    distribution = {}
    if distribution_mode == "Equa":
        drinks_per_cocktail = total_drinks / n_cocktails
        for cocktail in selected_cocktails:
            distribution[cocktail] = drinks_per_cocktail
    else:  # "Con cocktail principale"
        if main_cocktail and main_cocktail in selected_cocktails:
            main_drinks = total_drinks * 0.5
            distribution[main_cocktail] = main_drinks
            
            remaining_drinks = total_drinks - main_drinks
            other_cocktails = [c for c in selected_cocktails if c != main_cocktail]
            if other_cocktails:
                drinks_per_other = remaining_drinks / len(other_cocktails)
                for cocktail in other_cocktails:
                    distribution[cocktail] = drinks_per_other
        else:
            drinks_per_cocktail = total_drinks / n_cocktails
            for cocktail in selected_cocktails:
                distribution[cocktail] = drinks_per_cocktail
    
    # Calculate ingredients
    ingredients_total = {}
    for cocktail, n_drinks in distribution.items():
        recipe = RECIPES.get(cocktail, {})
        for ingredient, quantity in recipe.items():
            ingredients_total[ingredient] = ingredients_total.get(ingredient, 0) + quantity * n_drinks
    
    return ingredients_total, distribution

def generate_pdf(people, drinks_per_person, ingredients_total, distribution, checklist, notes):
    """Generate PDF shopping list"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm,
                          topMargin=2*cm, bottomMargin=2*cm)
    
    elements = []
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#FF6B35'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    # Add title
    title = Paragraph("🍸 Lista Spesa Cocktail Vicennole", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.5*cm))
    
    # Event info
    info_style = styles['Normal']
    info_style.alignment = TA_LEFT
    elements.append(Paragraph(f"<b>Data:</b> {datetime.now().strftime('%d/%m/%Y %H:%M')}", info_style))
    elements.append(Paragraph(f"<b>Persone:</b> {people}", info_style))
    elements.append(Paragraph(f"<b>Cocktail a testa:</b> {drinks_per_person}", info_style))
    elements.append(Paragraph(f"<b>Totale drink:</b> {people * drinks_per_person}", info_style))
    elements.append(Spacer(1, 0.5*cm))
    
    # Distribution
    elements.append(Paragraph("<b>Distribuzione Cocktail:</b>", styles['Heading2']))
    dist_data = [['Cocktail', 'Numero Drink']]
    for cocktail, n_drinks in sorted(distribution.items()):
        dist_data.append([cocktail, format_quantity(n_drinks)])
    
    dist_table = Table(dist_data, colWidths=[10*cm, 4*cm])
    dist_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF6B35')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(dist_table)
    elements.append(Spacer(1, 0.8*cm))
    
    # Ingredients
    elements.append(Paragraph("<b>Lista Spesa - Ingredienti:</b>", styles['Heading2']))
    
    ing_data = [['✓', 'Ingrediente', 'Quantità', 'Note']]
    for ingredient, quantity in sorted(ingredients_total.items()):
        checked = '☑' if checklist.get(ingredient, False) else '☐'
        note = notes.get(ingredient, '')
        ing_data.append([checked, ingredient, format_quantity(quantity), note])
    
    ing_table = Table(ing_data, colWidths=[1*cm, 7*cm, 3*cm, 5*cm])
    ing_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF6B35')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 9)
    ]))
    elements.append(ing_table)
    
    # Build PDF
    doc.build(elements)
    buffer.seek(0)
    return buffer

def save_session(name, data):
    """Save session to JSON file"""
    sessions_file = 'cocktail_sessions.json'
    sessions = {}
    
    if os.path.exists(sessions_file):
        with open(sessions_file, 'r') as f:
            sessions = json.load(f)
    
    sessions[name] = {
        'date': datetime.now().isoformat(),
        'data': data
    }
    
    with open(sessions_file, 'w') as f:
        json.dump(sessions, f, indent=2)

def load_sessions():
    """Load sessions from JSON file"""
    sessions_file = 'cocktail_sessions.json'
    if os.path.exists(sessions_file):
        with open(sessions_file, 'r') as f:
            return json.load(f)
    return {}

# Main App
st.title("🍸 Cocktail Planner Vicennole")
st.markdown("### Calcola esattamente cosa comprare per la tua serata")

# Sidebar for saved sessions
with st.sidebar:
    st.header("💾 Sessioni Salvate")
    sessions = load_sessions()
    
    if sessions:
        session_names = list(sessions.keys())
        selected_session = st.selectbox("Carica una sessione", [""] + session_names)
        
        if selected_session and st.button("Carica"):
            session_data = sessions[selected_session]['data']
            loaded_cocktails = set(session_data.get('selected_cocktails', []))
            st.session_state.selected_cocktails = loaded_cocktails
            
            # Sync all checkbox states with loaded cocktails (both category and search checkboxes)
            for category, cocktails in COCKTAIL_CATEGORIES.items():
                for cocktail in cocktails:
                    checkbox_key = f"checkbox_{cocktail}"
                    search_checkbox_key = f"search_checkbox_{cocktail}"
                    st.session_state[checkbox_key] = cocktail in loaded_cocktails
                    st.session_state[search_checkbox_key] = cocktail in loaded_cocktails
            
            st.rerun()
    else:
        st.info("Nessuna sessione salvata")

# Main content
tab1, tab2, tab3 = st.tabs(["📋 Pianificazione", "🛒 Risultati", "ℹ️ Info"])

with tab1:
    st.subheader("Configurazione Evento")
    
    col1, col2 = st.columns(2)
    with col1:
        people = st.number_input("👥 Numero di persone", min_value=1, value=10, step=1)
    with col2:
        drinks_per_person = st.number_input("🍹 Cocktail a testa", min_value=1, value=3, step=1)
    
    st.info(f"📊 Totale drink da preparare: **{people * drinks_per_person}**")
    
    st.markdown("---")
    st.subheader("🍸 Selezione Cocktail")
    
    # Search field with autocomplete
    st.markdown("#### 🔍 Cerca Cocktail")
    all_cocktails = []
    for cocktails in COCKTAIL_CATEGORIES.values():
        all_cocktails.extend(cocktails)
    
    search_query = st.text_input("Cerca per nome...", key="search_cocktail", placeholder="Es: Mojito, Negroni...")
    
    # Filter and show matching cocktails when user types
    if search_query:
        filtered_cocktails = [c for c in all_cocktails if search_query.lower() in c.lower()]
        if filtered_cocktails:
            st.markdown("**Risultati ricerca:**")
            search_cols = st.columns(3)
            for idx, cocktail in enumerate(filtered_cocktails):
                with search_cols[idx % 3]:
                    search_checkbox_key = f"search_checkbox_{cocktail}"
                    # Initialize based on selected_cocktails
                    if search_checkbox_key not in st.session_state:
                        st.session_state[search_checkbox_key] = cocktail in st.session_state.selected_cocktails
                    
                    is_checked = st.checkbox(cocktail, key=search_checkbox_key)
                    
                    # Sync with selected_cocktails
                    if is_checked:
                        st.session_state.selected_cocktails.add(cocktail)
                    else:
                        st.session_state.selected_cocktails.discard(cocktail)
        else:
            st.info("Nessun cocktail trovato")
    
    st.markdown("---")
    
    # Show selected cocktails
    if st.session_state.selected_cocktails:
        st.markdown("#### ✅ Cocktail Selezionati")
        selected_cols = st.columns(4)
        selected_list = sorted(list(st.session_state.selected_cocktails))
        for idx, cocktail in enumerate(selected_list):
            with selected_cols[idx % 4]:
                if st.button(f"❌ {cocktail}", key=f"remove_{cocktail}", use_container_width=True):
                    st.session_state.selected_cocktails.discard(cocktail)
                    # Clear both checkbox keys
                    checkbox_key = f"checkbox_{cocktail}"
                    search_checkbox_key = f"search_checkbox_{cocktail}"
                    if checkbox_key in st.session_state:
                        st.session_state[checkbox_key] = False
                    if search_checkbox_key in st.session_state:
                        st.session_state[search_checkbox_key] = False
                    st.rerun()
        st.markdown("---")
    
    # Cocktail selection by category
    st.markdown("#### 📚 Sfoglia per Categoria")
    for category, cocktails in COCKTAIL_CATEGORIES.items():
        with st.expander(f"**{category}** ({len(cocktails)} cocktail)", expanded=False):
            cols = st.columns(2)
            for idx, cocktail in enumerate(cocktails):
                with cols[idx % 2]:
                    # Initialize checkbox state from selected_cocktails on first run
                    checkbox_key = f"checkbox_{cocktail}"
                    if checkbox_key not in st.session_state:
                        st.session_state[checkbox_key] = cocktail in st.session_state.selected_cocktails
                    
                    # Create checkbox - it will maintain its own state via the key
                    is_checked = st.checkbox(cocktail, key=checkbox_key)
                    
                    # Sync the checkbox state with selected_cocktails
                    if is_checked:
                        st.session_state.selected_cocktails.add(cocktail)
                    else:
                        st.session_state.selected_cocktails.discard(cocktail)
    
    st.markdown("---")
    st.subheader("⚖️ Distribuzione")
    
    distribution_mode = st.radio(
        "Modalità distribuzione:",
        ["Equa", "Con cocktail principale"],
        help="Equa: stessa quantità per tutti. Con principale: un cocktail al 50%, altri divisi equamente"
    )
    
    main_cocktail = None
    if distribution_mode == "Con cocktail principale":
        selected_list = sorted(list(st.session_state.selected_cocktails))
        if selected_list:
            main_cocktail = st.selectbox("Seleziona cocktail principale:", selected_list)
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🧮 Calcola Ingredienti", type="primary", use_container_width=True):
        if len(st.session_state.selected_cocktails) == 0:
            st.error("⚠️ Seleziona almeno un cocktail!")
        else:
            ingredients_total, distribution = calculate_ingredients(
                people, drinks_per_person, 
                st.session_state.selected_cocktails,
                distribution_mode, main_cocktail
            )
            st.session_state.ingredients_total = ingredients_total
            st.session_state.distribution = distribution
            st.session_state.calculated = True
            
            # Initialize checklist for new ingredients
            for ingredient in ingredients_total.keys():
                if ingredient not in st.session_state.checklist:
                    st.session_state.checklist[ingredient] = False
                if ingredient not in st.session_state.notes:
                    st.session_state.notes[ingredient] = ""
            
            st.success("✅ Calcolo completato! Vai alla tab 'Risultati'")
            st.markdown("---")
            st.markdown("""
                <div style='text-align: center; padding: 20px; background-color: #f0f2f6; border-radius: 10px;'>
                    <h3 style='color: #FF6B35;'>👆 Clicca sulla tab '🛒 Risultati' in alto per vedere la lista spesa</h3>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    if st.session_state.calculated:
        st.subheader("📊 Distribuzione Cocktail")
        
        # Display distribution
        dist_cols = st.columns(3)
        for idx, (cocktail, n_drinks) in enumerate(sorted(st.session_state.distribution.items())):
            with dist_cols[idx % 3]:
                st.metric(cocktail, format_quantity(n_drinks) + " drink")
        
        st.markdown("---")
        st.subheader("🛒 Lista Spesa")
        
        # Ingredients table with checklist and notes
        for ingredient, quantity in sorted(st.session_state.ingredients_total.items()):
            col1, col2, col3 = st.columns([0.5, 3, 2])
            
            with col1:
                checked = st.checkbox("", 
                                    key=f"check_{ingredient}",
                                    value=st.session_state.checklist.get(ingredient, False))
                st.session_state.checklist[ingredient] = checked
            
            with col2:
                display_text = f"**{ingredient}**: {format_quantity(quantity)}"
                if checked:
                    st.markdown(f"~~{display_text}~~")
                else:
                    st.markdown(display_text)
            
            with col3:
                note = st.text_input("Note", 
                                   key=f"note_{ingredient}",
                                   value=st.session_state.notes.get(ingredient, ""),
                                   label_visibility="collapsed",
                                   placeholder="Aggiungi nota...")
                st.session_state.notes[ingredient] = note
        
        st.markdown("---")
        
        # Actions
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Generate PDF
            pdf_buffer = generate_pdf(
                people, drinks_per_person,
                st.session_state.ingredients_total,
                st.session_state.distribution,
                st.session_state.checklist,
                st.session_state.notes
            )
            
            st.download_button(
                label="📄 Scarica PDF Lista Spesa",
                data=pdf_buffer,
                file_name=f"lista_spesa_cocktail_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                mime="application/pdf",
                type="primary",
                use_container_width=True
            )
        
        with col2:
            # Save session
            session_name = st.text_input("Nome sessione", key="session_name_input")
            if st.button("💾 Salva Sessione", use_container_width=True):
                if session_name:
                    save_session(session_name, {
                        'people': people,
                        'drinks_per_person': drinks_per_person,
                        'selected_cocktails': list(st.session_state.selected_cocktails),
                        'distribution_mode': distribution_mode,
                        'main_cocktail': main_cocktail
                    })
                    st.success(f"✅ Sessione '{session_name}' salvata!")
                else:
                    st.error("⚠️ Inserisci un nome per la sessione")
        
        with col3:
            # Reset checklist
            if st.button("🔄 Reset Checklist", use_container_width=True):
                st.session_state.checklist = {k: False for k in st.session_state.checklist.keys()}
                st.rerun()
    else:
        st.info("👈 Vai alla tab 'Pianificazione' per configurare il tuo evento e calcolare gli ingredienti")

with tab3:
    st.subheader("ℹ️ Informazioni")
    
    st.markdown("""
    ### 🍸 Cocktail Planner Vicennole
    
    **Versione Streamlit con Export PDF**
    
    Questa applicazione ti aiuta a pianificare eventi cocktail calcolando automaticamente 
    tutti gli ingredienti necessari in base al numero di ospiti e ai cocktail scelti.
    
    #### ✨ Funzionalità:
    - 📚 **30 cocktail** in 4 categorie (Aperitivo, Festa, Cena, Dopocena)
    - 🧮 **Calcolo automatico** ingredienti precisi
    - ⚖️ **Distribuzione intelligente** (equa o con cocktail principale)
    - ✅ **Checklist spesa** interattiva
    - 📝 **Note personalizzate** per ogni ingrediente
    - 💾 **Salvataggio sessioni** in formato JSON locale
    - 📄 **Export PDF** lista spesa scaricabile
    
    #### 🎯 Come usare:
    1. Inserisci numero persone e cocktail a testa
    2. Seleziona i cocktail desiderati
    3. Scegli la modalità di distribuzione
    4. Clicca "Calcola Ingredienti"
    5. Vai alla tab "Risultati" per vedere la lista spesa
    6. Scarica il PDF o salva la sessione per riutilizzarla
    
    #### 📦 Cocktail Disponibili:
    """)
    
    for category, cocktails in COCKTAIL_CATEGORIES.items():
        st.markdown(f"**{category}** ({len(cocktails)}): {', '.join(cocktails)}")
    
    st.markdown("---")
    st.markdown("*Fatto con ❤️ e 🍸 | GitHub: @fringuello79*")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "🍸 Cocktail Planner Vicennole | Streamlit Version with PDF Export"
    "</div>",
    unsafe_allow_html=True
)
