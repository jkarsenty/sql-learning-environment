import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import streamlit as st
from src.database.sample_data import load_sample_data

def app():
    st.title("Bienvenue dans l'environnement d'apprentissage SQL!")
    
    st.write("""
    Cet outil vous permet de:
    * Créer vos propres tables
    * Charger des données depuis des fichiers CSV
    * Exécuter des requêtes SQL
    * Visualiser les résultats
    """)
    
    if st.button("Charger les données d'exemple"):
        df_students, df_grades = load_sample_data()
        st.success("Données d'exemple chargées avec succès!")
        st.write("Table 'etudiants':")
        st.dataframe(df_students)
        st.write("Table 'notes':")
        st.dataframe(df_grades)