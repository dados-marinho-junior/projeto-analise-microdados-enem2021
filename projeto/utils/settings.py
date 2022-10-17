

''' 
 * @author Equipe01 
 * @versão 2.0.0
 * @package utils
 
Através deste arquivo você deve configurar todo o projeto.
Importante seguir todas as orientações do INSTALL.md  
'''
#Colocar o caminho do seu arquivo CSV.
ARQUIVO = r'MICRODADOS_ENEM_2021.csv'

#Aqui vai o nome do seu projeto no Google Cloud.
# Exemplo: new-project-204050
PROJETO = "nome-projeto"

#Aqui você Cria um novo conjunto de dados (DATABASE)
#Se ele já existir o programa segue na execução
DATABASE = "nome-database"

#Aqui ele cria uma nova TABLE
#Se existir, ele executara um DROP TABLE, recriando a TABLE
TABLE = "nome-tabela"

#Aqui ele cria uma nova VIEW
#Se existir, ele executara um DROP TABLE, recriando a VIEWS
VIEW = "nome-views"