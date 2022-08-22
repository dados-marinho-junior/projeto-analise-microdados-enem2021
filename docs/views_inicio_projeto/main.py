import mysql.connector
import pandas as pd 
import random


cnx = mysql.connector.connect(
    host = '3.89.36.150',
    user = 'e2122g1',
    password = 'e2122g1@16@ago',
    database = 'e2122g1'
    )
cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS TB_ENEM; 
""")

cur.execute("""
    CREATE TABLE TB_ENEM (
        TB_ENEM_ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        TP_FAIXA_ETARIA INT NOT NULL,
        TP_SEXO_ CHAR NOT NULL,
        TP_ESTADO_CIVIL INT NOT NULL,
        TP_COR_RACA INT NOT NULL,
        TP_NACIONALIDADE INT NOT NULL,
        TP_ST_CONCLUSAO INT NOT NULL,
        TP_ESCOLA INT NOT NULL,
        IN_TREINEIRO INT NOT NULL,
        NO_MUNICIPIO_PROVA TEXT NOT NULL,
        SG_UF_PROVA TEXT NOT NULL,
        TP_PRESENCA_CN INT NOT NULL,
        TP_PRESENCA_CH INT NOT NULL,
        TP_PRESENCA_LC INT NOT NULL,
        NU_NOTA_CN REAL NOT NULL,
        NU_NOTA_CH REAL NOT NULL,
        NU_NOTA_LC REAL NOT NULL,
        NU_NOTA_MT REAL NOT NULL,
        TP_STATUS_REDACAO INT NOT NULL,
        NU_NOTA_REDACAO REAL NOT NULL,
        Q001 CHAR NOT NULL,
        Q002 CHAR NOT NULL,
        Q003 CHAR NOT NULL,
        Q004 CHAR NOT NULL,
        Q005 INT NOT NULL,
        Q006 CHAR NOT NULL,
        Q024 CHAR NOT NULL,
        Q025 CHAR NOT NULL,
        MEDIA_ENEM REAL NOT NULL
     );
""")