import sqlite3
import os
import sys

def conectar():
    if getattr(sys, 'frozen', False):
        pasta_programa = os.path.dirname(sys.executable)
    else:
        pasta_programa = os.path.dirname(os.path.abspath(__file__))



    caminho_banco = os.path.join(pasta_programa, 'estoque.db')
    return sqlite3.connect(caminho_banco)



def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       codigo TEXT NOT NULL UNIQUE,    
       nome TEXT NOT NULL,
       categoria TEXT NOT NULL,
       quantidade INTEGER NOT NULL CHECK (quantidade >= 0),
       preco_compra REAL NOT NULL CHECK (preco_compra >= 0),
       preco_venda REAl NOT NULL CHECK (preco_venda >= 0),
       estoque_minimo INTEGER NOT NULL CHECK(estoque_minimo >=0)
       )
    
    ''')


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movimentacoes (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       produto_id INTEGER NOT NULL,
       tipo text NOT NULL CHECK (tipo IN ('ENTRADA', 'SAIDA')),
       quantidade INTEGER NOT NULL CHECK (quantidade > 0),
       data TEXT NOT NULL,
       FOREIGN KEY (produto_id) REFERENCES produtos (id)
       
       )
       
    
    
    
    
    
    
    ''')

    conexao.commit()
    conexao.close()
