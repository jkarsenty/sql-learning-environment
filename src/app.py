import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import streamlit as st
from src.pages import home, table_creator, data_loader, query_executor

PAGES = {
    "Accueil": home,
    "Créer une table": table_creator,
    "Charger des données": data_loader,
    "Exécuter des requêtes": query_executor
}

st.set_page_config(page_title="SQL Learning Environment")

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Aller à", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()