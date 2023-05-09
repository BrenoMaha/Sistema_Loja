import sqlite3

def create_table_if_not_exists():
    with sqlite3.connect('sistema_db.sqlite') as conn:
        cursor = conn.cursor()
        sql_query = '''
        CREATE TABLE IF NOT EXISTS funcionario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        );
        '''
        cursor.execute(sql_query)

create_table_if_not_exists()

