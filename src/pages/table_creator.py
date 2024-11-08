import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import streamlit as st
from src.database.connection import DatabaseConnection

def app():
    st.header("Créer une nouvelle table")
    
    table_name = st.text_input("Nom de la table")
    col_specs = st.text_area(
        "Spécifications des colonnes (une par ligne, format: nom_colonne type)",
        help="Exemple:\nid INTEGER\nnom VARCHAR\nage INTEGER"
    )
    
    if st.button("Créer la table") and table_name and col_specs:
        try:
            db = DatabaseConnection.get_instance()
            cols = [line.strip().split() for line in col_specs.strip().split('\n')]
            db.create_table(table_name, cols)
            st.success(f"Table {table_name} créée avec succès!")
        except Exception as e:
            st.error(f"Erreur lors de la création de la table: {str(e)}")