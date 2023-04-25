import mysql.connector as mysql
from mysql.connector import MySQLConnection


try:
    conx: MySQLConnection = mysql.connect (
        host='localhost',
        port='3306',
        user='root',
        passwd='',
        db = 'sistema_db'
    )
except Exception as err:
    raise err('Não foi possivel Conectar ao Banco!')


def cursor_factory():
    return conx.cursor()