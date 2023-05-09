from database.conexao import *
from tkinter import messagebox



def cadastrar_funcionario(usuario: str, senha: str):
    with sqlite3.connect('sistema_db.sqlite') as conn:
        cursor = conn.cursor()
        sql_query = "INSERT INTO funcionario (usuario, senha) VALUES (?, ?)"
        cursor.execute(sql_query, (usuario, senha))
        conn.commit()
        messagebox.showinfo("Sucesso!", "Cadastro realizado com sucesso")




def listar():
    with cursor_factory() as cursor:
        sql_query = 'SELECT * FROM cliente'
        cursor.execute(sql_query)
        clientes = cursor.fetchall()
        return clientes
    
def cadastrar(nome: str, email: str, cep: str, celular: str):
    with cursor_factory() as cursor:
        sql_query = f'''
            INSERT INTO cliente (nome, email, cep, celular) 
            VALUES ('{nome}', '{email}', '{cep}', '{celular}')'''
        cursor.execute(sql_query)
    conx.commit()

def detalhar(id_registration: int):
    with cursor_factory() as cursor:
        sql_query = f'''
        SELECT * FROM cliente WHERE id_registration = %s'''
        print(sql_query)
        cursor.execute(sql_query, (id_registration,))
        cliente = cursor.fetchone()
        return cliente
    
def alterar(id_registration: int, nome: str = None, email: str = None):
    with cursor_factory() as cursor:
        sql_query = '''
        SELECT * FROM cliente WHERE id_registration = %s
        '''
        cursor.execute(sql_query, (id_registration,))
        cliente = cursor.fetchone()
        print('[1] - Alterar nome')
        print('[2] - Alterar e-mail')
        print('[3] - Alterar CEP')
        print('[4] - Alterar Celular')
        opcao = input('Digite a opcao desejada:')
        if opcao == '1':
            novo_nome = input('Digite o novo nome: ')
            sql_query_nome = f'''
            update cliente set nome = %s where id_registration = %s
            '''
            cursor.execute(sql_query_nome, (novo_nome, id_registration))
            conx.commit()
        elif opcao == '2':
            novo_email = input('Digite o novo email: ')
            sql_query_email = f'''
            update cliente set email = %s where id_registration = %s
            '''
            cursor.execute(sql_query_email, (novo_email, id_registration))
            conx.commit()
        elif opcao == '3':
            novo_cep = input('Digite o novo CEP: ')
            sql_query_cep = f'''
            update cliente set cep = %s where id_registration = %s
            '''
            cursor.execute(sql_query_cep, (novo_cep))
            conx.commit()
        elif opcao == '4':
            novo_celular = input('Digite o novo celular: ')
            sql_query_celular = f'''
            update cliente set celular = %s where id_registration = %s
            '''
            cursor.execute(sql_query_celular,(novo_celular,id_registration))
            conx.commit()

def excluir(id_registration: int):
    with cursor_factory() as cursor:
        sql_query = f'''
        delete from cliente where id_registration = %s
        '''
        print(sql_query)
        cursor.execute(sql_query,(id_registration,))
        conx.commit()
        return f'cliente com id {id_registration} deletado do sistema'
    