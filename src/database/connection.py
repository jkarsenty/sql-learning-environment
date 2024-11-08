import duckdb
from typing import Optional

class DatabaseConnection:
    _instance: Optional['DatabaseConnection'] = None
    
    def __init__(self):
        self.conn = duckdb.connect(database=':memory:')
    
    @classmethod
    def get_instance(cls) -> 'DatabaseConnection':
        if cls._instance is None:
            cls._instance = DatabaseConnection()
        return cls._instance
    
    def execute_query(self, query: str) -> duckdb.DuckDBPyRelation:
        try:
            return self.conn.execute(query)
        except Exception as e:
            raise DatabaseError(f"Erreur lors de l'exécution de la requête: {str(e)}")
    
    def create_table(self, table_name: str, columns: list) -> None:
        cols_def = ", ".join([f"{col[0]} {col[1]}" for col in columns])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({cols_def})"
        self.execute_query(query)
    
    def import_csv(self, file_path: str, table_name: str) -> None:
        try:
            self.execute_query(f"CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{file_path}')")
        except Exception as e:
            raise DatabaseError(f"Erreur lors de l'import du fichier CSV: {str(e)}")

class DatabaseError(Exception):
    pass