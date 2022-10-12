
# Ata 01 - Reuniões de Agosto


## Dia 09/08/2022
- Reunião entre os integrantes da equipe e o professor;
- Estudo em equipe sobre os dados do arquivo-fonte e seus formatos;
- Definição inicial sobre as variáveis que serão objetos de estudos na nossa análise;
- Criação de um arquivo em csv apenas contendo as colunas que serão relevantes para o estudo, reduzindo de forma bastante significativa o tamanho do DB a ser agora utilizado;
- Adoção do Trello/Scrum/Kanban para melhor definição das tarefas e distribuição das atividades;

## Dia 10/08/2022
- Feita uma primeira análise de todas as colunas do DB, em especial de forma a identificar as colunas que possuem valores vazios (NaN), sendo possível observar colunas com quantidades significativas de células sem valor, o que terá que ser objeto de cuidadosa avaliação referente ao momento em que as linhas e/ou colunas serão objetos de 'drop' antes da análise; 


## Dia 12/08/2022
- Utilizado o parâmetro 'index = False' no script TCC_II no momento da criação do DF resumido a ser utilizado. Este parâmetro não permite a criação de coluna com os índices, que gera coluna 'Unnamed: 0' nos novos DFs derivados.
- Atualizado o arquivo em csv gerado a partir do script TCC_II;
- Reunião online dos integrantes da equipe para continuação dos trabalhos iniciais referentes ao projeto de conclusão de curso;
- Feitas apresentações a respeito das primeiras análises estatísticas sobre os atributos inicialmente definidos como objetos do trabalho, momento em que verificou-se que vários das colunas inicialmente selecionadas apresentaram grande quantidade de valores vazios, a ponto de prejudicar qualquer tipo de análise com as mesmas;
- Foi feita a opção pela inserção de novas colunas em substituição às que foram eliminadas, ampliando novamente o escopo das análises futuras. Ao mesmo tempo, optou-se pela inserção de colunas que anteriormente não haviam sido consideradas, mas que se revelaram importantes para o projeto;
- Criado um diretório no Google Drive para compartilhamento de arquivos entre os membros da equipe - link de acesso em <https://drive.google.com/drive/u/1/folders/1eXWQ8HOOUxKgyQCPdjJovsSDCPuKIQSE>;
- Drop de uma linha específica e única que continha diversas colunas com valores vazios - script TCC_II; 

## Dia 15/08/2022
- Novo tratamento dos dados do arquivo DADOS\MICRODADOS_ENEM_2021.csv, quando fizemos a conversão para tipo int64 daquelas variáveis que estavam definidas como do tipo float64, mas que, na realidade, refletiam valores inteiros - colunas TP_STATUS_REDACAO e Q005 - script TCC_II;
- A partir destas alterações, foi criada uma nova versão atualizada do arquivo Dados_Enem_2021.csv, que servirá de base para as próximas análises;
- Atualização dos arquivos das sprints no repositório Github da equipe.
  
## Dia 16/08/2022
- Feitas as seguintes alterações na base de dados a ser trabalhada (Dados_Enem_2021.csv):
- - Preenchidos com 0 (zero) todas as notas que estavam vazias (NaN);
- - Criação de uma coluna adicional para absorver as médias aritméticas simples de cada inscrito;
- - Cálculo das médias de todos os candidatos e inserção no DF;
- Atualização da base de dados (Dados_Enem_2021.csv) e posterior carregamento no Google Drive;
- Atualização dos scripts TC_II e TC_IV e posterior carregamento no Github;
- Informação à equipe via Telegram destas alterações para amplo conhecimento;
- Importante lição aprendida durante as tarefas do dia: após se fazer a eliminação de uma ou mais linhas do DF através do método drop(), é crucial aplicar o método reset_index() ao respectivo DF, pois os índices das linhas também são eliminados através do drop, o que fatalmente gera erro no caso de ser necessário o acesso àqueles índices que foram eliminados. Tal fato ocorreu por ocasião do cálculo das médias, resultando em erro quando o programa tentou acessar o índice de uma linha em particular que havia sido eliminada. O método reset_index() reorganiza os índices do DF, fazendo uma renumeração dos mesmos;
- Atualização dos arquivos das sprints no repositório Github da equipe.

##  Dia 19/08/2022
- Atualização da história do usuário no repositório Github da equipe.

##  Dia 22/08/2022
- Foi feito a estrutura do **conexao_banco_de_dados.py** com os CREATE e INSERT.
- Reunião online dos integrantes da equipe com o professor referente a estrutura main.py para inserção da base de dados no banco de dados, onde o mesmo envio um exemplo para tirar como base para nosso projeto; ([Link da Pasta](/Projeto/Testes/main-mysql3.py))
- Após alguns erros e correções do **conexao_banco_de_dados.py**, foi feita com sucesso a integração e população da base de dados.

# Dia 24/08/2022
- Após alguns teste concluimos que não haveria viabilidade em trabalhar com banco de dados compartilhado, pela maxividade dos dados.
- Opção pelo Big Query para armazenamento dos dados atraves **conexao_google_cloud_store.py**, a fim de agilizar as transações entre o Google Data Studio e os dados;
- Trabalhos em equipe de familiarização e utilização do Google Data Studio para filtragem dos dados e criação de gráficos/dashboards do projeto.


# Dia 25/08/2022
- Trabalhos em equipe de familiarização e utilização do Google Data Studio para filtragem dos dados e criação de gráficos/dashboards do projeto.

# Dia 26/08/2022
- Trabalhos em equipe de familiarização e utilização do Google Data Studio para filtragem dos dados e criação de gráficos/dashboards do projeto;
- Daily scrum entre os integrantes da equipe e o professor orientador do projeto para alinhamento de ideias e orientações gerais sobre o projeto.

##  Dia 29/08/2022
- Feita análise e divulgação de dados referentes aos índices de abstenção no ENEM 2019 para fins de comparação com dados análogos do ENEM 2021;
- Apresentação feita pelo professor de uso do Django para apresentação em páginas web do trabalho de conclusão do curso. Link da vídeo-aula em <https://drive.google.com/drive/folders/1wMUxkzHx_GAPi5Ha2J7K19kuDm3r_fTH>;
- Elaboração de um questionário com perguntas relevantes sobre os dados do ENEM 2021 e possíveis cruzamentos de informações que podem gerar análises relevantes para o projeto. Formulário se encontra no diretório do Google Drive da equipe e está disponível para contribuições de todos os integrantes;
 

## Dia 30/08/2022
- Daily scrum entre os integrantes da equipe e o professor orientador do projeto para alinhamento de ideias e orientações gerais sobre o projeto;
- Atualização de documentação geral do projeto;


## Dia 31/08/2022
- Início dos trabalhos de análise das abstenções e médias por estados das edições do ENEM de 2017, 2018, 2019 e 2020, para possibilitar comparações com a edição de 2021, tema do nosso projeto. Neste dia, os trabalhos foram focados nos scripts para gerar os resultados;
