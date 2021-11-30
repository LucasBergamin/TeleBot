import sqlite3
from sqlite3 import Error

def criando_conexao(nome_banco):
    conexao = None
    try:
        conexao = sqlite3.connect(nome_banco, check_same_thread=False)
    except Error as e:
        print(f"ERRO: {e} 1")

    return conexao


def executando_query(conexao, query):
    cursor = conexao.cursor()
    try:
        cursor.execute(query)
        conexao.commit()
    except Error as e:
        print(f"ERRO: {e} 2")


def select_query(conexao, query):
    cursor = conexao.cursor()
    resultado = None
    try:
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado
    except Error as e:
        print(f"ERRO: {e} 3")