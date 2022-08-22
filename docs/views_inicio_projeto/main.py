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
        TP_FAIXA_ETARIA CHAR NOT NULL,
        TP_SEXO CHAR NOT NULL,
        TP_ESTADO_CIVIL CHAR NOT NULL,
        TP_COR_RACA CHAR NOT NULL,
        TP_NACIONALIDADE CHAR NOT NULL,
        TP_ST_CONCLUSAO CHAR NOT NULL,
        TP_ESCOLA CHAR NOT NULL,
        IN_TREINEIRO CHAR NOT NULL,
        NO_MUNICIPIO_PROVA TEXT NOT NULL,
        SG_UF_PROVA TEXT NOT NULL,
        TP_PRESENCA_CN CHAR NOT NULL,
        TP_PRESENCA_CH CHAR NOT NULL,
        TP_PRESENCA_LC CHAR NOT NULL,
        NU_NOTA_CN INT NOT NULL,
        NU_NOTA_CH INT NOT NULL,
        NU_NOTA_LC INT NOT NULL,
        NU_NOTA_MT INT NOT NULL,
        TP_STATUS_REDACAO CHAR NOT NULL,
        NU_NOTA_REDACAO INT NOT NULL,
        Q001 CHAR NOT NULL,
        Q002 CHAR NOT NULL,
        Q003 CHAR NOT NULL,
        Q004 CHAR NOT NULL,
        Q005 VARCHAR NOT NULL,
        Q006 CHAR NOT NULL,
        Q024 CHAR NOT NULL,
        Q025 CHAR NOT NULL,
        MEDIA_ENEM REAL NOT NULL
     );
""")

sql=("""
    INSERT INTO TB_ENEM(
        TP_FAIXA_ETARIA,
        TP_SEXO,
        TP_ESTADO_CIVIL,
        TP_COR_RACA,
        TP_NACIONALIDADE,
        TP_ST_CONCLUSAO,
        TP_ESCOLA,
        IN_TREINEIRO,
        NO_MUNICIPIO_PROVA,
        SG_UF_PROVA,
        TP_PRESENCA_CN,
        TP_PRESENCA_CH,
        TP_PRESENCA_LC,
        NU_NOTA_CN,
        NU_NOTA_CH,
        NU_NOTA_LC,
        NU_NOTA_MT,
        TP_STATUS_REDACAO,
        NU_NOTA_REDACAO,
        Q001,
        Q002,
        Q003,
        Q004,
        Q005,
        Q006,
        Q024,
        Q025,
        MEDIA_ENEM)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

for index, row in df.iterrows():
    val=(
        row.TP_FAIXA_ETARIA,
        row.TP_SEXO,
        row.TP_ESTADO_CIVIL,
        row.TP_COR_RACA,
        row.TP_NACIONALIDADE,
        row.TP_ST_CONCLUSAO,
        row.TP_ESCOLA,
        row.IN_TREINEIRO,
        row.NO_MUNICIPIO_PROVA,
        row.SG_UF_PROVA,
        row.TP_PRESENCA_CN,
        row.TP_PRESENCA_CH,
        row.TP_PRESENCA_LC,
        row.NU_NOTA_CN,
        row.NU_NOTA_CH,
        row.NU_NOTA_LC,
        row.NU_NOTA_MT,
        row.TP_STATUS_REDACAO,
        row.NU_NOTA_REDACAO,
        row.Q001,
        row.Q002,
        row.Q003,
        row.Q004,
        row.Q005,
        row.Q006,
        row.Q024,
        row.Q025,
        row.MEDIA_ENEM)  
    cur.execute(sql,val)

cnx.commit()

