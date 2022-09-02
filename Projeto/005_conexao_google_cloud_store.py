'''
Para conexão com Google Cloud Storage juntamente com Big Query, 
utilizamos um tutorial fornecido pelo google segue o link:

https://codelabs.developers.google.com/codelabs/cloud-bigquery-python#0

Fizemos toda parte de autentificação da maquina para estabelecer a conexão
Fizemos as modificações necessarias para integração do 
nosso arquivo .csv
'''
#importando bibliotecas necessárias
from google.cloud import bigquery
#Carregando o Objeto
client = bigquery.Client()

#Conexão com o Big Query
table_id = "nome-do-projeto.conjunto_de_dados.tabela"
file_path = r"caminho_do_arquivo.csv"

#Criação do esquema
job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("TP_FAIXA_ETARIA", "STRING"),
        bigquery.SchemaField("TP_SEXO", "STRING"),
        bigquery.SchemaField("TP_ESTADO_CIVIL", "STRING"),
        bigquery.SchemaField("TP_COR_RACA", "STRING"),
        bigquery.SchemaField("TP_NACIONALIDADE", "STRING"),
        bigquery.SchemaField("TP_ST_CONCLUSAO", "STRING"),
        bigquery.SchemaField("TP_ESCOLA", "STRING"),
        bigquery.SchemaField("IN_TREINEIRO", "STRING"),
        bigquery.SchemaField("NO_MUNICIPIO_PROVA", "STRING"),
        bigquery.SchemaField("SG_UF_PROVA", "STRING"),
        bigquery.SchemaField("TP_PRESENCA_CN", "STRING"),
        bigquery.SchemaField("TP_PRESENCA_CH", "STRING"),
        bigquery.SchemaField("TP_PRESENCA_LC", "STRING"),
        bigquery.SchemaField("TP_PRESENCA_MT", "STRING"),
        bigquery.SchemaField("NU_NOTA_CN", "FLOAT"),
        bigquery.SchemaField("NU_NOTA_CH", "FLOAT"),
        bigquery.SchemaField("NU_NOTA_LC", "FLOAT"),
        bigquery.SchemaField("NU_NOTA_MT", "FLOAT"),
        bigquery.SchemaField("TP_STATUS_REDACAO", "STRING"),
        bigquery.SchemaField("NU_NOTA_REDACAO", "FLOAT"),
        bigquery.SchemaField("Q001", "STRING"),
        bigquery.SchemaField("Q002", "STRING"),
        bigquery.SchemaField("Q003", "STRING"),
        bigquery.SchemaField("Q004", "STRING"),
        bigquery.SchemaField("Q005", "STRING"),
        bigquery.SchemaField("Q006", "STRING"),
        bigquery.SchemaField("Q024", "STRING"),
        bigquery.SchemaField("Q025", "STRING"),
        bigquery.SchemaField("MEDIA_ENEM", "FLOAT"),

    ],
    skip_leading_rows=1,
    # O formato de origem padrão é CSV, portanto, a linha abaixo é opcional.
    source_format=bigquery.SourceFormat.CSV,
)

with open(file_path, "rb") as source_file:
    job = client.load_table_from_file(
        source_file, table_id, job_config=job_config)

job.result()  # Resultado do Projeto.

table = client.get_table(table_id)  # Requisão da API.

print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)
