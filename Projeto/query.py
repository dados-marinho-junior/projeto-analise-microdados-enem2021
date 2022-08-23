""" 
<h4 align="center">Projeto Análise Microdados Enem 2021</h4>

 - Diogo Lindemann
 - Francisco de Assis
 - Luana Naiara
 - Marcelo Takahashi
 - Rafael Rosso
 - Sylvio Carneiro
"""
#Importar 
import mysql.connector
from re import I
from unittest import result

#Fazer conexão com banco
cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g1',
    password = 'e2122g1@16@ago',
    database = 'e2122g1'
    )
cur = cnx.cursor()

# #Tratamento de dados
# cur.execute("SELECT * FROM TB_ENEM;")
# todos= cur.fetchall()
# print(f'\nTodas: {todos}')
# print(type(todos))

# for x,y,z in todos:
#     print(f'{x}:{y}:{z}')

# #Contador
# for i in ["", ""]:
#     sql = "SELECT COUNT (*) FROM" + i
#     cur.execute(sql)
#     result = cur.fetchall()
#     print(f'{i}:{result}')

