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

def create_cliente_database():
    with sqlite3.connect('sistema_db.sqlite') as conn:
        cursor = conn.cursor()
        sql_query = '''
        CREATE TABLE IF NOT EXISTS cliente (
        id integer primary key autoincrement,
        nome text not null,
        cpf text not null,
        cep text not null,
        email text not null
        );
        '''

        cursor.execute(sql_query)

create_cliente_database()

def create_produto_database():
    with sqlite3.connect('sistema_db.sqlite') as conn:
        cursor = conn.cursor()
        sql_query = '''
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        );
        '''
        cursor.execute(sql_query)

create_produto_database()


