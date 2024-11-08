import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import streamlit as st
from src.database.connection import DatabaseConnection

def app():
    st.header("Exécuter des requêtes SQL")
    
    # Afficher les tables disponibles
    db = DatabaseConnection.get_instance()
    tables = db.execute_query("SHOW TABLES").fetchall()
    if tables:
        st.write("Tables disponibles:")
        for table in tables:
            st.code(f"Table: {table[0]}")
            # Afficher la structure de la table
            st.code(db.execute_query(f"DESCRIBE {table[0]}").df())
    
    # Zone de requête
    query = st.text_area("Entrez votre requête SQL ici")
    
    if st.button("Exécuter") and query:
        try:
            result = db.execute_query(query).df()
            st.success("Requête exécutée avec succès!")
            st.dataframe(result)
        except Exception as e:
            st.error(f"Erreur dans la requête: {str(e)}")