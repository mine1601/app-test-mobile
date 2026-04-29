import streamlit as st
import pandas as pd
import json
from datetime import datetime
import os

# Configuration de la page optimisée pour mobile
st.set_page_config(
    page_title="Santé App",
    page_icon="🏥",
    layout="centered", # Centré pour une meilleure apparence mobile
    initial_sidebar_state="collapsed" # Fermé par défaut sur mobile
)

# CSS personnalisé pour un look "Application Mobile"
st.markdown("""
    <style>
    /* Style global pour mobile */
    .stApp {
        max-width: 500px;
        margin: 0 auto;
    }
    
    /* Titre style App */
    .app-header {
        background-color: #1f77b4;
        color: white;
        padding: 20px;
        border-radius: 0 0 20px 20px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Boutons de navigation larges */
    .nav-button {
        display: block;
        width: 100%;
        padding: 15px;
        margin-bottom: 10px;
        background-color: #f0f2f6;
        border-radius: 12px;
        text-align: left;
        border: none;
        font-weight: bold;
        color: #262730;
    }
    
    /* Amélioration des champs de saisie pour le tactile */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        padding: 12px !important;
        font-size: 16px !important;
        border-radius: 10px !important;
    }
    
    /* Bouton valider style mobile */
    div.stButton > button:first-child {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        padding: 15px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        margin-top: 20px;
    }
    
    /* Cartes pour les sections */
    .mobile-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border: 1px solid #eee;
    }
    </style>
""", unsafe_allow_html=True)

# Initialisation
if 'data_list' not in st.session_state:
    st.session_state.data_list = []
if 'file_path' not in st.session_state:
    st.session_state.file_path = 'patient_data.json'
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Menu"

# En-tête de l'application
st.markdown("<div class='app-header'><h1>🏥 Santé App</h1><p>Collecte & Analyse</p></div>", unsafe_allow_html=True)

# Fonction pour changer de page
def navigate_to(page_name):
    st.session_state.current_page = page_name

# ==================== MENU PRINCIPAL (Look App) ====================
if st.session_state.current_page == "Menu":
    st.markdown("### 📱 Menu Principal")
    
    if st.button("📝 Nouveau Formulaire", use_container_width=True):
        navigate_to("Collecte")
        st.rerun()
        
    if st.button("📊 Consulter les Données", use_container_width=True):
        navigate_to("Analyse")
        st.rerun()
        
    if st.button("✏️ Modifier une Entrée", use_container_width=True):
        navigate_to("Modifier")
        st.rerun()

# ==================== PAGE : COLLECTE ====================
elif st.session_state.current_page == "Collecte":
    if st.button("⬅️ Retour au Menu"):
        navigate_to("Menu")
        st.rerun()
        
    st.markdown("### 📝 Saisie Patient")
    
    with st.form("mobile_form"):
        st.markdown("<div class='mobile-card'>", unsafe_allow_html=True)
        st.subheader("👤 Identité")
        nom = st.text_input("Nom complet")
        age = st.number_input("Âge", min_value=0, max_value=120, value=25)
        sexe = st.selectbox("Sexe", ["Masculin", "Féminin", "Autre"])
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='mobile-card'>", unsafe_allow_html=True)
        st.subheader("💓 Constantes")
        col1, col2 = st.columns(2)
        with col1:
            sys = st.number_input("Tension Sys.", value=120)
        with col2:
            dia = st.number_input("Tension Dia.", value=80)
        temp = st.number_input("Température (°C)", value=37.0, step=0.1)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='mobile-card'>", unsafe_allow_html=True)
        st.subheader("📋 Observations")
        symptomes = st.text_area("Symptômes")
        st.markdown("</div>", unsafe_allow_html=True)
        
        submit = st.form_submit_button("ENREGISTRER")
        
        if submit:
            if not nom:
                st.error("Le nom est obligatoire")
            else:
                # Sauvegarde simplifiée
                new_data = {
                    "id": datetime.now().strftime("%H%M%S"),
                    "nom_complet": nom,
                    "age": age,
                    "sexe": sexe,
                    "tension": f"{sys}/{dia}",
                    "temp": temp,
                    "symptomes": symptomes,
                    "date": datetime.now().strftime("%Y-%m-%d")
                }
                
                # Charger et Sauvegarder
                data = []
                if os.path.exists(st.session_state.file_path):
                    with open(st.session_state.file_path, 'r') as f:
                        data = json.load(f)
                data.append(new_data)
                with open(st.session_state.file_path, 'w') as f:
                    json.dump(data, f, indent=2)
                
                st.success("✅ Données enregistrées !")
                if st.button("Saisir un autre patient"):
                    st.rerun()

# ==================== PAGE : ANALYSE ====================
elif st.session_state.current_page == "Analyse":
    if st.button("⬅️ Retour au Menu"):
        navigate_to("Menu")
        st.rerun()
        
    st.markdown("### 📊 Données")
    
    if os.path.exists(st.session_state.file_path):
        with open(st.session_state.file_path, 'r') as f:
            data = json.load(f)
        
        if data:
            df = pd.DataFrame(data)
            st.metric("Total Patients", len(df))
            st.dataframe(df[['nom_complet', 'age', 'tension', 'date']], use_container_width=True)
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Télécharger CSV", csv, "donnees.csv", "text/csv", use_container_width=True)
        else:
            st.info("Aucune donnée")
    else:
        st.info("Aucune donnée")

# ==================== PAGE : MODIFIER ====================
elif st.session_state.current_page == "Modifier":
    if st.button("⬅️ Retour au Menu"):
        navigate_to("Menu")
        st.rerun()
    st.info("Sélectionnez une entrée dans la liste pour la modifier (Fonctionnalité en cours)")

# Pied de page style mobile
st.markdown("---")
st.markdown("<p style='text-align: center; color: #999; font-size: 12px;'>Santé App v1.0 • 2026</p>", unsafe_allow_html=True)
