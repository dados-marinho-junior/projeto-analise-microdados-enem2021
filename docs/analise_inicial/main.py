# Arquivo main.py

# Esta versão executa toda a sua rotina internamente, com apenas 
# um mínimo# de exibições ao usuário. 
# Para uma visualização com mais detalhes da execução do código, 
# é possível executar a versão para o notebook Jupyter deste mesmo
# script (main.ipynb).

import pandas as pd
import numpy as np  # Usado para conversão de formato de dados com o método astype().

url_or_file = 'MICRODADOS_ENEM_2021.csv'
print('\nLeitura inicial do arquivo de dados do ENEM 2017 ...')
dados = pd.read_csv(url_or_file, sep = ';', encoding = 'ISO-8859-1')
print('\nLeitura do arquivo de dados do ENEM 2017 concluída.')

# Lista obtida a partir do método .columns:
colunas = ['NU_INSCRICAO', 'NU_ANO', 'TP_FAIXA_ETARIA', 'TP_SEXO',
       'TP_ESTADO_CIVIL', 'TP_COR_RACA', 'TP_NACIONALIDADE', 'TP_ST_CONCLUSAO',
       'TP_ANO_CONCLUIU', 'TP_ESCOLA', 'TP_ENSINO', 'IN_TREINEIRO',
       'CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC',
       'TP_DEPENDENCIA_ADM_ESC', 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC',
       'CO_MUNICIPIO_PROVA', 'NO_MUNICIPIO_PROVA', 'CO_UF_PROVA',
       'SG_UF_PROVA', 'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC',
       'TP_PRESENCA_MT', 'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC',
       'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT',
       'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH', 'TX_RESPOSTAS_LC',
       'TX_RESPOSTAS_MT', 'TP_LINGUA', 'TX_GABARITO_CN', 'TX_GABARITO_CH',
       'TX_GABARITO_LC', 'TX_GABARITO_MT', 'TP_STATUS_REDACAO',
       'NU_NOTA_COMP1', 'NU_NOTA_COMP2', 'NU_NOTA_COMP3', 'NU_NOTA_COMP4',
       'NU_NOTA_COMP5', 'NU_NOTA_REDACAO', 'Q001', 'Q002', 'Q003', 'Q004',
       'Q005', 'Q006', 'Q007', 'Q008', 'Q009', 'Q010', 'Q011', 'Q012', 'Q013',
       'Q014', 'Q015', 'Q016', 'Q017', 'Q018', 'Q019', 'Q020', 'Q021', 'Q022',
       'Q023', 'Q024', 'Q025']

colunas_socioeconomicas = ['Q001', 'Q002', 'Q003', 'Q004', 'Q005', 
                           'Q006', 'Q007', 'Q008', 'Q009', 'Q010', 
                           'Q011', 'Q012', 'Q013', 'Q014', 'Q015', 
                           'Q016', 'Q017', 'Q018', 'Q019', 'Q020', 
                           'Q021', 'Q022', 'Q023', 'Q024', 'Q025']

# Obtenção e armazenamento dos índices de linhas para limpeza (drop):
# Criação de um DF com valores vazios nas colunas de indicadores socioeconômicos já definidas:
for coluna in colunas_socioeconomicas:
    df = dados.loc[dados[coluna].isna(), coluna]

# Lista que armazenará os índices das linhas para deleção (drop):
lista_indices = []

# Criado o DF das colunas com valores vazios, a próxima iteração captura e armazena em lista
# os índices das linhas que serão eliminadas (drop):
for i in range(len(df)):
    indice = df.index[i]
    lista_indices.append(indice)

# Esta iteração elimina (drop) as linhas com vazios em alguma coluna de indicadores socioeconômicos:
print('\nEliminando linhas com indicadores socioeconômicos vazios ...')
for indice in lista_indices:
    dados = dados.drop(indice, axis = 0)

# Reorganização dos índices do DF inicial:
dados = dados.reset_index()
dados = dados.drop('index', axis = 1)

# Criar uma nova coluna no DF para a média aritmética simples das 5 notas:
dados['MEDIA_ENEM'] = 0.0

# Converter para int as colunas 'TP_STATUS_REDACAO' e 'Q005'.
# Primeiramente devem ser preenchidos com 0 onde está vazio.
# Atribuir 0 as células de notas vazias.

# Transformação de float para int o tipo da variável da coluna 'Q005':
dados['Q005'] = dados['Q005'].astype(np.int64)

# Preenchimento dos valores vazios da coluna 'TP_STATUS_REDACAO' com 
# o valor 4 (status 'em branco'), conforme critério adotado por nossa equipe:
dados['TP_STATUS_REDACAO'] = dados['TP_STATUS_REDACAO'].fillna(4)

# Conversão para int64 de todos os valores da coluna 'TP_STATUS_REDACAO':
dados['TP_STATUS_REDACAO'] = dados['TP_STATUS_REDACAO'].astype(np.int64)

# Atribuir zero para as notas NaN nas colunas 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO'.
colunas_notas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
for coluna in colunas_notas:
    dados[coluna] = dados[coluna].fillna(0)

# Cálculo e preenchimento das médias.
dados['MEDIA_ENEM'] = dados.loc[:, ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].mean(axis = 1)

# Colunas que serão consideradas no projeto após definidas em reunião da equipe:
colunas = ['TP_FAIXA_ETARIA', 
           'TP_SEXO',
           'TP_ESTADO_CIVIL', 
           'TP_COR_RACA', 
           'TP_NACIONALIDADE', 
           'TP_ST_CONCLUSAO', 
           'TP_ESCOLA',
           'IN_TREINEIRO',
           'NO_MUNICIPIO_PROVA',
           'SG_UF_PROVA',
           'TP_PRESENCA_CN', 
           'TP_PRESENCA_CH', 
           'TP_PRESENCA_LC',
           'TP_PRESENCA_MT',
           'NU_NOTA_CN', 
           'NU_NOTA_CH', 
           'NU_NOTA_LC', 
           'NU_NOTA_MT',
           'TP_STATUS_REDACAO',
           'NU_NOTA_REDACAO', 
           'Q001', 
           'Q002', 
           'Q003', 
           'Q004',
           'Q005', 
           'Q006', 
           'Q024', 
           'Q025',
           'MEDIA_ENEM']

# Criação do novo Data Frame com a estrutura do arquivo csv a ser gerado 
# para a análise do projeto:
dados_enem = dados[colunas]

try:
    dados_enem.to_csv('Dados_Enem_2021.csv', sep=',', index = False)
    # index = False não permite a criação de coluna com os índices, 
    # que gera coluna 'Unnamed: 0' nos novos DFs derivados.
    print('\nArquivo Dados_Enem_2021.csv criado com sucesso.')
except:
    print('\nErro na criação do arquivo .csv do projeto.')

