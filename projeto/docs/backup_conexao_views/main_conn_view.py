from google.cloud import bigquery

client = bigquery.Client()

#essa parte vai para um arquivo de config
caminho="aqui"
projeto = "projeto-rafael-360600"
conjunto_de_dados = "goku3"
tabela = "dbz2"
view = "view"
#até aqui

dataset_id = (projeto+'.'+conjunto_de_dados)


try:
    #aqui confere se existe
    client.get_dataset(dataset_id) 
except:
    #se não existe cria um novo
    dataset = client.create_dataset(conjunto_de_dados)
   
else:
    # se existe,  somente carrega o dataset
    dataset = client.dataset(conjunto_de_dados)

#aqui cria a tabela
table_id = dataset.table(tabela)
#se ela existe dropa e recria novamente
client.delete_table(table_id, not_found_ok=True)

#essa parte vai ser eliminada
file_path = r"/Users/rafaelrosso/entra21/dados-e21-22-curso/google_cloud/projeto/Dados_Enem_2021.csv"


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
        bigquery.SchemaField("Q005", "FLOAT"),
        bigquery.SchemaField("Q006", "STRING"),
        bigquery.SchemaField("Q024", "STRING"),
        bigquery.SchemaField("Q025", "STRING"),
        bigquery.SchemaField("MEDIA_ENEM", "FLOAT"),

    ],
    skip_leading_rows=1,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)

with open(file_path, "rb") as source_file:
    job = client.load_table_from_file(
        source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)
#eliminada até aqui

#AQUI ENTRA A PARTE DE SCHEMA DO DATAFRAME

#aqui cria o view
view_id = dataset.table(view)
#se ele existe dropa e cria novamente
client.delete_table(view_id, not_found_ok=True)

#aqui carrega o url do projeto
source_id = (projeto+'.'+conjunto_de_dados+'.'+tabela)
view = bigquery.Table(view_id)

view.view_query = f'''SELECT
  CASE
    WHEN TP_FAIXA_ETARIA = "1" THEN 'Menor que 17 anos'
    WHEN TP_FAIXA_ETARIA IN ("2", "3", "4", "5") THEN "Entre 17 e 20 anos"
    WHEN TP_FAIXA_ETARIA IN ("6", "7", "8", "9", "10") THEN "Entre 21 e 25 anos"
    WHEN TP_FAIXA_ETARIA = "11" THEN "Entre 26 e 30 anos"
    WHEN TP_FAIXA_ETARIA = "12" THEN "Entre 31 e 35 anos"
    WHEN TP_FAIXA_ETARIA = "13" THEN "Entre 36 e 40 anos"
    WHEN TP_FAIXA_ETARIA = "14" THEN "Entre 41 e 45 anos"
    WHEN TP_FAIXA_ETARIA = "15" THEN "Entre 46 e 50 anos"
    WHEN TP_FAIXA_ETARIA = "16" THEN "Entre 51 e 55 anos"
    WHEN TP_FAIXA_ETARIA = "17" THEN "Entre 56 e 60 anos"
    WHEN TP_FAIXA_ETARIA = "18" THEN "Entre 61 e 65 anos"
    WHEN TP_FAIXA_ETARIA = "19" THEN "Entre 66 e 70 anos"
    WHEN TP_FAIXA_ETARIA = "20" THEN "Acima de 70 anos"
END
  AS Faixa_Etaria,
  CASE
    WHEN TP_SEXO ='M'THEN 'Masculino'
    WHEN TP_SEXO ='F'THEN 'Feminino'
END
  AS Genero,
  CASE
    WHEN MEDIA_ENEM = 0 THEN "Nota Anulada (igual a 0)"
    WHEN MEDIA_ENEM < 400 THEN "Nota abaixo de 400 (não qualificado*) "
    WHEN MEDIA_ENEM >= 400 AND MEDIA_ENEM < 500 THEN "Nota acima de 400 até 499"
    WHEN MEDIA_ENEM >= 500 AND MEDIA_ENEM < 600 THEN "Nota acima de 500 até 599"
    WHEN MEDIA_ENEM >= 600 AND MEDIA_ENEM < 700 THEN "Nota acima de 600 até 699"
    WHEN MEDIA_ENEM >= 700 AND MEDIA_ENEM < 800 THEN "Nota acima de 700 até 799"
    WHEN MEDIA_ENEM >= 800 THEN "Nota acima de 800"
END
  AS Classificacao,
  CASE
    WHEN TP_ESTADO_CIVIL = "0" THEN "Não informado"
    WHEN TP_ESTADO_CIVIL = "1" THEN "Solteiro(a)"
    WHEN TP_ESTADO_CIVIL = "2" THEN "Casado(a) - Mora com companheiro(a)"
    WHEN TP_ESTADO_CIVIL = "3" THEN "Divorciado(a)/Desquitado(a)/Separado(a)"
    WHEN TP_ESTADO_CIVIL = "4" THEN "Viúvo(a)"
END
  AS Estado_civil,
  CASE
    WHEN TP_COR_RACA IN ("0", "6") THEN "Não Declarado(a)"
    WHEN TP_COR_RACA = "1" THEN "Branco(a)"
    WHEN TP_COR_RACA = "2" THEN "Preto(a)"
    WHEN TP_COR_RACA = "3" THEN "Pardo(a)"
    WHEN TP_COR_RACA = "4" THEN "Amarelo(a)"
    WHEN TP_COR_RACA = "5" THEN "Indígena(a)"
END
  AS Etnias,
  CASE
    WHEN TP_NACIONALIDADE = "0" THEN "Não informado"
    WHEN TP_NACIONALIDADE = "1" THEN "Brasileiro(a)"
    WHEN TP_NACIONALIDADE = "2" THEN "Brasileiro(a) Naturalizado(a)"
    WHEN TP_NACIONALIDADE = "3" THEN "Estrangeiro(a)"
    WHEN TP_NACIONALIDADE = "4" THEN "Brasileiro(a) Nato(a), nascido(a) no exterior"
END
  AS Nacionalidade,
  CASE
    WHEN TP_ST_CONCLUSAO = "1" THEN "Já concluí o Ensino Médio"
    WHEN TP_ST_CONCLUSAO = "2" THEN "Estou cursando e concluirei o Ensino Médio em 2021"
    WHEN TP_ST_CONCLUSAO = "3" THEN "Estou cursando e concluirei o Ensino Médio após 2021"
    WHEN TP_ST_CONCLUSAO = "4" THEN "Não concluí e não estou cursando o Ensino Médio"
END
  AS Situacao_de_Conclusao,
  CASE
    WHEN TP_ESCOLA = "1" THEN "Não Respondeu"
    WHEN TP_ESCOLA = "2" THEN "Pública"
    WHEN TP_ESCOLA = "3" THEN "Privada"
END
  AS Tipo_Escola,
  CASE
    WHEN IN_TREINEIRO = "0" THEN "estudante"
    WHEN IN_TREINEIRO = "1" THEN "treineiro"
END
  AS Treineiro,
  NO_MUNICIPIO_PROVA AS Cidades,
  CASE
    WHEN SG_UF_PROVA = "AC" THEN "Acre"
    WHEN SG_UF_PROVA = "AL" THEN "Alagoas"
    WHEN SG_UF_PROVA = "AP" THEN "Amapá"
    WHEN SG_UF_PROVA = "AM" THEN "Amazonas"
    WHEN SG_UF_PROVA = "BA" THEN "Bahia"
    WHEN SG_UF_PROVA = "CE" THEN "Ceará"
    WHEN SG_UF_PROVA = "DF" THEN "Distrito Federal"
    WHEN SG_UF_PROVA = "ES" THEN "Espírito Santo"
    WHEN SG_UF_PROVA = "GO" THEN "Goiás"
    WHEN SG_UF_PROVA = "MA" THEN "Maranhão"
    WHEN SG_UF_PROVA = "MT" THEN "Mato Grosso"
    WHEN SG_UF_PROVA = "MS" THEN "Mato Grosso do Sul"
    WHEN SG_UF_PROVA = "MG" THEN "Minas Gerais"
    WHEN SG_UF_PROVA = "PA" THEN "Pará"
    WHEN SG_UF_PROVA = "PB" THEN "Paraíba"
    WHEN SG_UF_PROVA = "PR" THEN "Paraná"
    WHEN SG_UF_PROVA = "PE" THEN "Pernambuco"
    WHEN SG_UF_PROVA = "PI" THEN "Piauí"
    WHEN SG_UF_PROVA = "RJ" THEN "Rio de Janeiro"
    WHEN SG_UF_PROVA = "RN" THEN "Rio Grande do Norte"
    WHEN SG_UF_PROVA = "RS" THEN "Rio Grande do Sul"
    WHEN SG_UF_PROVA = "RO" THEN "Rondônia"
    WHEN SG_UF_PROVA = "RR" THEN "Roraima"
    WHEN SG_UF_PROVA = "SC" THEN "Santa Catarina"
    WHEN SG_UF_PROVA = "SP" THEN "São Paulo"
    WHEN SG_UF_PROVA = "SE" THEN "Sergipe"
    WHEN SG_UF_PROVA = "TO" THEN "Tocantins"
END
  AS Estados,
  CASE
    WHEN SG_UF_PROVA IN ("AC", "AP", "AM", "PA", "RO", "RR", "TO") THEN "NORTE"
    WHEN SG_UF_PROVA IN ("AL", "BA", "CE", "MA", "PB", "PI", "PE", "RN", "SE") THEN "NORDESTE"
    WHEN SG_UF_PROVA IN ("DF", "GO", "MT", "MS") THEN "CENTRO-OESTE"
    WHEN SG_UF_PROVA IN ("ES", "MG", "RJ", "SP") THEN "SUDESTE"
    WHEN SG_UF_PROVA IN ("PR", "RS", "SC") THEN "SUL"
END
  AS Regioes,
  CASE
    WHEN TP_PRESENCA_CN = "0" THEN "Faltou à prova"
    WHEN TP_PRESENCA_CN = "1" THEN "Presente na prova"
    WHEN TP_PRESENCA_CN = "2" THEN "Eliminado na prova"
END
  AS Ciencias_da_Natureza,
  CASE
    WHEN TP_PRESENCA_CH = "0" THEN "Faltou à prova"
    WHEN TP_PRESENCA_CH = "1" THEN "Presente na prova"
    WHEN TP_PRESENCA_CH = "2" THEN "Eliminado na prova"
END
  AS Ciencias_Humanas,
  CASE
    WHEN TP_PRESENCA_LC = "0" THEN "Faltou à prova"
    WHEN TP_PRESENCA_LC = "1" THEN "Presente na prova"
    WHEN TP_PRESENCA_LC = "2" THEN "Eliminado na prova"
END
  AS Linguagens_e_Codigos,
  CASE
    WHEN TP_PRESENCA_MT = "0" THEN "Faltou à prova"
    WHEN TP_PRESENCA_MT = "1" THEN "Presente na prova"
    WHEN TP_PRESENCA_MT = "2" THEN "Eliminado na prova"
END
  AS Matematica,
  NU_NOTA_CN AS Nota_Ciencias_da_Natureza,
  NU_NOTA_CH AS Nota_Ciencias_Humanas,
  NU_NOTA_LC AS Nota_Linguagens_e_Codigos,
  NU_NOTA_MT AS Nota_Matematica,
  CASE
    WHEN TP_STATUS_REDACAO = "1" THEN "Sem problemas"
    WHEN TP_STATUS_REDACAO = "2" THEN "Anulada"
    WHEN TP_STATUS_REDACAO = "3" THEN "Cópia Texto Motivador"
    WHEN TP_STATUS_REDACAO = "4" THEN "Em Branco"
    WHEN TP_STATUS_REDACAO = "6" THEN "Fuga ao tema"
    WHEN TP_STATUS_REDACAO = "7" THEN "Não atendimento ao tipo textual"
    WHEN TP_STATUS_REDACAO = "8" THEN "Texto insuficiente"
    WHEN TP_STATUS_REDACAO = "9" THEN "Parte desconectada"
END
  AS Status_Redacao,
  NU_NOTA_REDACAO AS Nota_Redacao,
  CASE
    WHEN Q001 = "A" THEN "01. Nunca estudou."
    WHEN Q001 = "B" THEN "02. Não completou a 4ª série/5º ano do Ensino Fundamental."
    WHEN Q001 = "C" THEN "03. Completou a 4ª série/5º ano, mas não completou o Ensino Fundamental."
    WHEN Q001 = "D" THEN "04. Completou o Ensino Fundamental, mas não completou o Ensino Médio."
    WHEN Q001 = "E" THEN "05. Completou o Ensino Médio, mas não completou a Faculdade."
    WHEN Q001 = "F" THEN "06. Completou a Faculdade, mas não completou a Pós-graduação."
    WHEN Q001 = "G" THEN "07. Completou a Pós-graduação."
    WHEN Q001 = "H" THEN "08. Não sei."
END
  AS Q1,
  CASE
    WHEN Q002 = "A" THEN "01. Nunca estudou."
    WHEN Q002 = "B" THEN "02. Não completou a 4ª série/5º ano do Ensino Fundamental."
    WHEN Q002 = "C" THEN "03. Completou a 4ª série/5º ano, mas não completou o Ensino Fundamental."
    WHEN Q002 = "D" THEN "04. Completou o Ensino Fundamental, mas não completou o Ensino Médio."
    WHEN Q002 = "E" THEN "05. Completou o Ensino Médio, mas não completou a Faculdade."
    WHEN Q002 = "F" THEN "06. Completou a Faculdade, mas não completou a Pós-graduação."
    WHEN Q002 = "G" THEN "07. Completou a Pós-graduação."
    WHEN Q002 = "H" THEN "08. Não sei."
END
  AS Q2,
  Q005 AS Q5,
  CASE
    WHEN Q006 IN ("A") THEN "01. Nenhuma Renda."
    WHEN Q006 IN ("B") THEN "02. Até R$ 1.100,00"
    WHEN Q006 IN ("C", "D") THEN "03. De R$ 1.100,01 até R$ 2.200,00"
    WHEN Q006 IN ("E", "F") THEN "04. De R$ 2.200,01 até R$ 3.300,00"
    WHEN Q006 IN ("G", "H") THEN "05. De R$ 3.300,01 até R$ 5.500,00"
    WHEN Q006 IN ("I", "J") THEN "06. De R$ 5.500,01 até R$ 7.700,00"
    WHEN Q006 IN ("K", "L") THEN "07. De R$ 7.700,01 até R$ 9.900,00"
    WHEN Q006 IN ("M", "N") THEN "08. De R$ 9.900,01 até R$ 13.200,00"
    WHEN Q006 IN ("O", "P") THEN "09. De R$ 13.200,01 até R$ 22.000,00"
    WHEN Q006 IN ("Q") THEN "10. Acima de R$ 22.000,00"
END
  AS Q6,
  CASE
    WHEN Q024 = "A" THEN "01. Não"
    WHEN Q024 = "B" THEN "02. Sim, um."
    WHEN Q024 = "C" THEN "03. Sim, dois."
    WHEN Q024 = "D" THEN "04. Sim, três."
    WHEN Q024 = "E" THEN "05. Sim, quatro ou mais."
END
  AS Q24,
  CASE
    WHEN Q025 = "A" THEN "Não."
    WHEN Q025 = "B" THEN "Sim."
END
  AS Q25,
  MEDIA_ENEM AS Media_Enen FROM {source_id} '''

# Make an API request to create the view.
view = client.create_table(view)
print(f"Created {view.table_type}: {str(view.reference)}")
