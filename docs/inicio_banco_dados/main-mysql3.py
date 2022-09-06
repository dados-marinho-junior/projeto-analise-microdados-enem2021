'''
   
'''

# pip install mysql-connector-python

import mysql.connector
import pandas as pd 
import random


cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g3',
    password = 'e2122g3@16@ago',
    database = 'e2122g3'
    )

cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS CIDADES; 
""")

cur.execute("""    
    CREATE TABLE CIDADES (
            CIDADE_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            CIDADE_UF TEXT NOT NULL,
            CIDADE_NOME TEXT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS PESSOAS; 
""")

cur.execute("""
    CREATE TABLE PESSOAS(
        PESSOA_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        PESSOA_NOME TEXT NOT NULL,
        PESSOA_IDADE INTEGER, 
        PESSOA_CIDADE_ID INTEGER NOT NULL
    );
""")

#  Tabela de Cidades
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSp3N0iSajaKoFaRiiTOV1Qxm1Y6-_B1IKJsKaqjiBhJbNIrjER4Kr2YtDHn8xNsFvWhQiGBK-Q5MQN/pub?gid=0&single=true&output=csv'
colunas = list(['id','UF','Município'])

df = pd.read_csv(url_or_file)

values = []
for index,row in df.iterrows():
    uf = row.UF
    cidade = row.Município
    values.append((uf,cidade))
        
insert_values = "".join(str(values).strip('[]'))
# sql=(f"INSERT INTO CIDADE (PESSOA_NOME,PESSOA_IDADE,PESSOA_CIDADE_ID) VALUES {insert_values}")
sql=(f"INSERT INTO CIDADES (CIDADE_UF,CIDADE_NOME) VALUES {insert_values}")

# print(insert_values)
cur.execute(sql)
cnx.commit()    





# # Tabela de Pessoas
# '''
url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQrw2IJT8L_iuyYyZRehzDK89pNRRQUEVvUl1KxEJ8U182AEkUMIyWtGtQf3SHG8rxsEoni_-cqr4yo/pub?gid=945554847&single=true&output=csv'

colunas = list(['id','first_name'])

df = pd.read_csv(url_or_file, usecols=colunas)

numero_cidades = list((df.shape))[0] 
values = []
for index,row in df.iterrows():
    nome = row.first_name
    idade = random.randrange(0,120)
    cidade_id = random.randrange(1,numero_cidades)          
    values.append((nome,idade,cidade_id))
    
insert_values = "".join(str(values).strip('[]'))
sql=(f"INSERT INTO PESSOAS (PESSOA_NOME,PESSOA_IDADE,PESSOA_CIDADE_ID) VALUES {insert_values}")

# print(insert_values)
cur.execute(sql)
cnx.commit()    



