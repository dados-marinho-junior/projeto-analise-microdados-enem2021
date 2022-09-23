# Importação da função analise.py ...
from analise import analisar  # Ainda é apenas uma função
from schema import criar_schema # Ainda é apenas uma função
from app1.views import criar_view # Ainda é apenas uma função
from settings import ARQUIVO

arquivo = ARQUIVO

# Análise inicial e limpeza do conjunto de dados:
dados_enem = analisar(arquivo)

# Criação do schema:
tupla = criar_schema(dados_enem)

# Criação da view:
ds, cl = tupla
criar_view(ds, cl)

