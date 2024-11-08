import pandas as pd
from .connection import DatabaseConnection

def load_sample_data():
    db = DatabaseConnection.get_instance()
    
    # Données étudiants
    students_data = {
        'id': range(1, 6),
        'nom': ['Dupont', 'Martin', 'Durand', 'Petit', 'Moreau'],
        'age': [20, 22, 21, 23, 19],
        'ville': ['Paris', 'Lyon', 'Paris', 'Marseille', 'Lyon']
    }
    
    # Données notes
    grades_data = {
        'etudiant_id': [1, 1, 2, 3, 4, 5],
        'matiere': ['Maths', 'Histoire', 'Maths', 'Maths', 'Histoire', 'Maths'],
        'note': [15, 12, 18, 14, 16, 13]
    }
    
    df_students = pd.DataFrame(students_data)
    df_grades = pd.DataFrame(grades_data)
    
    # Création des tables
    db.conn.execute("CREATE TABLE IF NOT EXISTS etudiants AS SELECT * FROM df_students")
    db.conn.execute("CREATE TABLE IF NOT EXISTS notes AS SELECT * FROM df_grades")
    
    return df_students, df_grades