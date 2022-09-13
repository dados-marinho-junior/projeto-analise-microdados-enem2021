'''
Através deste arquivo você deve configurar todo o projeto.
Important seguir todas as orientações do INSTALL.md  
'''
#Colocar o caminho do seu arquivo CSV.
ARQUIVO = r"caminho/nome_do_aquivo.csv"

#Aqui vai o nome do seu projeto no Google Cloud.
# Exemplo: new-project-204050
PROJETO = "nome-do-projeto"

#Aqui você Cria um novo conjunto de dados (DATABASE)
#Se ele já existir o programa segue na execução
DATABASE = "nome_conjunto_de_dados"

#Aqui ele cria uma nova TABLE
#Se existir, ele executara um DROP TABLE, recriando a TABLE
TABLE = "nome_tabela"

#Aqui ele cria uma nova VIEW
#Se existir, ele executara um DROP TABLE, recriando a VIEW
VIEW = "nome_view"