''' 
 * @author Equipe01 
 * @versão 2.0.0
 * @package utils'''

# Importação da função analise.py ...
from analise import analisar  
from schema import criar_schema 
from app1.views import criar_view
from settings import ARQUIVO

# Análise inicial e limpeza do conjunto de dados:
dados_enem = analisar(ARQUIVO)

# Criação do schema:
tupla = criar_schema(dados_enem)

# Criação da views:
dataset, client = tupla
criar_view(dataset, client)

