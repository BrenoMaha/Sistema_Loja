import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table_if_not_exists(self):
        sql_query = '''
        CREATE TABLE IF NOT EXISTS funcionario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        );
        '''
        self.cursor.execute(sql_query)

    def create_cliente_database(self):
        sql_query = '''
        CREATE TABLE IF NOT EXISTS cliente (
        id integer primary key autoincrement,
        nome text not null,
        cpf text not null,
        cep text not null,
        email text not null
        );
        '''
        self.cursor.execute(sql_query)

    def create_produto_database(self):
        sql_query = '''
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        );
        '''
        self.cursor.execute(sql_query)


db = Database('sistema_db.sqlite')
db.create_table_if_not_exists()
db.create_cliente_database()
db.create_produto_database()
