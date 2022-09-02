'''
Nesta parte fizemos a conexão do nosso arquivo CSV com o banco de dados compartilhado,
Utilizando o rescurso do pandas Skiprows, para inputar 1000 dados por vez, 
Transformando o dataframe em uma lista inserir o dados em lote

'''

# Bibliotecas Utilizadas
import mysql.connector
import pandas as pd

# Conexão com Servidor
cnx = mysql.connector.connect(
    # host='',
    # user='',
    # password='',
    # database=''
)
cur = cnx.cursor()

#Deleta a tabela se existir
cur.execute("""
    DROP TABLE IF EXISTS NOVA_TB_ENEM; 
""")
#cria o Schema da tabela
cur.execute("""
    CREATE TABLE NOVA_TB_ENEM (
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
        TP_PRESENCA_MT CHAR NOT NULL,
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
        Q005 INT NOT NULL,
        Q006 CHAR NOT NULL,
        Q024 CHAR NOT NULL,
        Q025 CHAR NOT NULL,
        MEDIA_ENEM REAL NOT NULL
     );
""")

# Criando o Data Frame chamando a função Conecta
def conecta(valor):
    url_or_file = r'caminho_do_arquivo.csv'
    dados = pd.read_csv(url_or_file, sep=',',
                        encoding='utf-8',
                        nrows=1000,
                        skiprows=range(1, valor)
                        )
    # Transformando em lista
    values = []
    for index, row in dados.iterrows():
        TP_FAIXA_ETARIA = row.TP_FAIXA_ETARIA
        TP_SEXO = row.TP_SEXO
        TP_ESTADO_CIVIL = row.TP_ESTADO_CIVIL
        TP_COR_RACA = row.TP_COR_RACA
        TP_NACIONALIDADE = row.TP_NACIONALIDADE
        TP_ST_CONCLUSAO = row.TP_ST_CONCLUSAO
        TP_ESCOLA = row.TP_ESCOLA
        IN_TREINEIRO = row.IN_TREINEIRO
        NO_MUNICIPIO_PROVA = row.NO_MUNICIPIO_PROVA
        SG_UF_PROVA = row.SG_UF_PROVA
        TP_PRESENCA_CN = row.TP_PRESENCA_CN
        TP_PRESENCA_CH = row.TP_PRESENCA_CH
        TP_PRESENCA_LC = row.TP_PRESENCA_LC
        TP_PRESENCA_MT = row.TP_PRESENCA_MT
        NU_NOTA_CN = row.NU_NOTA_CN
        NU_NOTA_CH = row.NU_NOTA_CH
        NU_NOTA_LC = row.NU_NOTA_LC
        NU_NOTA_MT = row.NU_NOTA_MT
        TP_STATUS_REDACAO = row.TP_STATUS_REDACAO
        NU_NOTA_REDACAO = row.NU_NOTA_REDACAO
        Q001 = row.Q001
        Q002 = row.Q002
        Q003 = row.Q003
        Q004 = row.Q004
        Q005 = row.Q005
        Q006 = row.Q006
        Q024 = row.Q024
        Q025 = row.Q025
        MEDIA_ENEM = row.MEDIA_ENEM
        values.append((
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
            TP_PRESENCA_MT,
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
            MEDIA_ENEM))
    insert_values = "".join(str(values).strip('[]'))
    #Inputando os valores
    sql = (f"""
        INSERT INTO NOVA_TB_ENEM(
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
            TP_PRESENCA_MT,
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
        VALUES {insert_values}
    """)

    cur.execute(sql)
    cnx.commit()

# Executando um laço na funçao Conecta
for i in range(1, 2685052, 1000):
    conecta(i)
cur.close()
