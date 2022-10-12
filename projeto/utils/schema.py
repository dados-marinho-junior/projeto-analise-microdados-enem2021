''' 
 * @author Equipe01 
 * @versão 2.0
 * @package utils'''

from google.cloud import bigquery
from settings import *


def criar_schema(data_frame):
    '''
    Esta função recebe um objeto do tipo dataframe criado pelo pandas,
    faz as verificações, cria um schema, faz a população dos dados e
    retorna o dataset e o client em forma de uma tupla.
    ''' 
    client = bigquery.Client()
    dataset_id = (PROJETO+'.'+DATABASE)

    try:
    #confere se existe o dataset
        client.get_dataset(dataset_id) 
    except:
    #se não existe, cria um novo dataset
        dataset = client.create_dataset(DATABASE)
        print('\nBanco de dados criado.') 
    else:
    #se existe, somente carrega o dataset
        dataset = client.dataset(DATABASE)
        print('\nBanco de dados encontrado.')

#  criação da tabela
    table_id = dataset.table(TABLE)
    print('\nTabela criada.')
# Se ela existe, executa um DROP TABLE e recria a tabela
    client.delete_table(table_id, not_found_ok=True)

    print('\nCriando o Schema ...')
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
        bigquery.SchemaField("Q005", "INTEGER"),
        bigquery.SchemaField("Q006", "STRING"),
        bigquery.SchemaField("Q024", "STRING"),
        bigquery.SchemaField("Q025", "STRING"),
        bigquery.SchemaField("MEDIA_ENEM", "FLOAT"),
    ],
    source_format=bigquery.SourceFormat.CSV,
    )
    print('\nPopulando dados ...')
    job = client.load_table_from_dataframe(
    data_frame, table_id, job_config=job_config
    )

    job.result()
    table = client.get_table(table_id) 
    print('\nTabela criada com {} linhas e {} colunas para {}'.format(
        table.num_rows, len(table.schema), table_id))
    return(dataset, client)