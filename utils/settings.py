'''
Através deste arquivo você deve configurar todo o projeto.
Important seguir todas as orientações do INSTALL.md  
'''
#Colocar o caminho do seu arquivo CSV.
ARQUIVO = r'MICRODADOS_ENEM_2021.csv'

#Aqui vai o nome do seu projeto no Google Cloud.
# Exemplo: new-project-204050
PROJETO = "enem-2021"

#Aqui você Cria um novo conjunto de dados (DATABASE)
#Se ele já existir o programa segue na execução
DATABASE = "base_teste15"

#Aqui ele cria uma nova TABLE
#Se existir, ele executara um DROP TABLE, recriando a TABLE
TABLE = "tabela_teste15"

#Aqui ele cria uma nova VIEW
#Se existir, ele executara um DROP TABLE, recriando a VIEW
VIEW = "view_teste15"