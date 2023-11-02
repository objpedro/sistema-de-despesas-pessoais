import sys
import sqlite3 as lite
from datetime import datetime

# importing pandas
import pandas as pd

# Criando conexão
con = lite.connect('dados.db')

# Inserir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)

# Inserir receitas
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# Inserir gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)
       
# Deletar receitas
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)

# Deletar gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)

# Ver Categorias
def ver_categorias():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

# Ver Receitas
def ver_Receitas():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

# Ver Gastos
def ver_gastos():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens