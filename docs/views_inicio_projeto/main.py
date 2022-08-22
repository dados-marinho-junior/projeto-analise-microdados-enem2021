import sqlite3
import pandas as pd

cnx = sqlite3.connect('projeto_enem21.sqlite3')
cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS TB_ENEM; 
""")

cur.execute("""
    CREATE TABLE TB_ENEM (
        TB_ENEM_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TP_FAIXA_ETARIA INT NULL,
        TP_SEXO_SEXO OBJECT NULL,
        TP_ESTADO_CIVIL INT NULL,
        TP_COR_RACA INT NULL,
        TP_NACIONALIDADE INT NULL,
        TP_ST_CONCLUSAO INT NULL,
        TP_ESCOLA INT NULL,
        IN_TREINEIRO INT NULL,
        NO_MUNICIPIO_PROVA OBJECT NULL,
        SG_UF_PROVA OBJECT NULL,
        TP_PRESENCA_CN INT NULL,
        TP_PRESENCA_CH INT NULL,
        TP_PRESENCA_LC INT NULL,
        NU_NOTA_CN FLOAT NULL,
        NU_NOTA_CH FLOAT NULL,
        NU_NOTA_LC FLOAT NULL,
        NU_NOTA_MT FLOAT NULL,
        TP_STATUS_REDACAO INT NULL,
        NU_NOTA_REDACAO FLOAT NULL,
        Q001 OBJECT NULL,
        Q002 OBJECT NULL,
        Q003 OBJECT NULL,
        Q004 OBJECT NULL,
        Q005 OBJECT NULL,
        Q006 OBJECT NULL,
        Q024 OBJECT NULL,
        Q025 OBJECT NULL,
        MEDIA_ENEM OBJECT NULL
     );
""")