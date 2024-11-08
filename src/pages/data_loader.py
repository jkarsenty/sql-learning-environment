import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import streamlit as st
from src.database.connection import DatabaseConnection

def app():
    st.header("Charger des données")
    
    uploaded_file = st.file_uploader("Choisir un fichier CSV", type="csv")
    if uploaded_file is not None:
        table_name = st.text_input("Nom de la table à créer")
        
        if st.button("Charger les données") and table_name:
            try:
                db = DatabaseConnection.get_instance()
                db.import_csv(uploaded_file.name, table_name)
                st.success(f"Données chargées dans la table {table_name}")
            except Exception as e:
                st.error(f"Erreur lors du chargement des données: {str(e)}")