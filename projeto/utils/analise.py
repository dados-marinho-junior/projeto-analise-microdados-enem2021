''' 
 * @author Equipe01 
 * @versão 2.0.0
 * @package utils'''

import pandas as pd
import numpy as np

colunas_socioeconomicas = ['Q001', 'Q002', 'Q003', 'Q004', 'Q005', 
                           'Q006', 'Q007', 'Q008', 'Q009', 'Q010', 
                           'Q011', 'Q012', 'Q013', 'Q014', 'Q015', 
                           'Q016', 'Q017', 'Q018', 'Q019', 'Q020', 
                           'Q021', 'Q022', 'Q023', 'Q024', 'Q025']

colunas_notas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']

colunas_df = ['TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_ESTADO_CIVIL', 'TP_COR_RACA',
              'TP_NACIONALIDADE','TP_ST_CONCLUSAO', 'TP_ESCOLA', 'IN_TREINEIRO',
              'NO_MUNICIPIO_PROVA', 'SG_UF_PROVA', 'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 
              'TP_PRESENCA_LC', 'TP_PRESENCA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 
              'NU_NOTA_LC', 'NU_NOTA_MT', 'TP_STATUS_REDACAO', 'NU_NOTA_REDACAO', 
              'Q001', 'Q002', 'Q003', 'Q004', 'Q005', 'Q006', 'Q024', 'Q025','MEDIA_ENEM']

def analisar(nome_do_arquivo):
    print('\nLeitura inicial do arquivo de dados do ENEM 2021 ...')
    dados = pd.read_csv(nome_do_arquivo, sep = ';', encoding = 'ISO-8859-1')
    print('\nLeitura do arquivo de dados do ENEM 2021 concluída.')   

    print('\nEliminando linhas com indicadores socioeconômicos vazios ...')
    dados.dropna(axis = 0, how = 'any', subset = colunas_socioeconomicas, inplace = True)
    dados = dados.reset_index()

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
    
    for coluna in colunas_notas:
        dados[coluna] = dados[coluna].fillna(0)

    # Cálculo e preenchimento das médias.
    print('\nCalculando a média de cada inscrito ...')
    dados['MEDIA_ENEM'] = dados.loc[:, colunas_notas].mean(axis = 1)
    print('\nMédias calculadas.')
    data_frame = dados[colunas_df]
    print('Data Frame criado.')
    return(data_frame)