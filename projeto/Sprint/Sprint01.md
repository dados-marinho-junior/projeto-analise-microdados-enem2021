<h1 align="center"> Sprint Semana 01 </h1>

# Semana de 09 a 12/08/2022
 

- Reunião entre os integrantes da equipe e o professor;
- Estudo em equipe sobre os dados do arquivo-fonte e seus formatos;
- Definição inicial sobre as variáveis que serão objetos de estudos na nossa análise;
- Criação de um arquivo em csv apenas contendo as colunas que serão relevantes para o estudo, reduzindo de forma bastante significativa o tamanho do DB a ser agora utilizado;
- Feita uma primeira análise de todas as colunas do DB, em especial de forma a identificar as colunas que possuem valores vazios (NaN), sendo possível observar colunas com quantidades significativas de células sem valor, o que terá que ser objeto de cuidadosa avaliação referente ao momento em que as linhas e/ou colunas serão objetos de 'drop' antes da análise; 
- Utilizado o parâmetro 'index = False' no script TCC_II no momento da criação do DF resumido a ser utilizado. Este parâmetro não permite a criação de coluna com os índices, que gera coluna 'Unnamed: 0' nos novos DFs derivados.
- Atualizado o arquivo em csv gerado a partir do script TCC_II;
- Reunião online dos integrantes da equipe para continuação dos trabalhos iniciais referentes ao projeto de conclusão de curso;
- Feitas apresentações a respeito das primeiras análises estatísticas sobre os atributos inicialmente definidos como objetos do trabalho, momento em que verificou-se que vários das colunas inicialmente selecionadas apresentaram grande quantidade de valores vazios, a ponto de prejudicar qualquer tipo de análise com as mesmas;
- Foi feita a opção pela inserção de novas colunas em substituição às que foram eliminadas, ampliando novamente o escopo das análises futuras. Ao mesmo tempo, optou-se pela inserção de colunas que anteriormente não haviam sido consideradas, mas que se revelaram importantes para o projeto;
- Criado um diretório no Google Drive para compartilhamento de arquivos entre os membros da equipe - link de acesso em <https://drive.google.com/drive/u/1/folders/1eXWQ8HOOUxKgyQCPdjJovsSDCPuKIQSE>;
- Drop de uma linha específica e única que continha diversas colunas com valores vazios - script TCC_II; 

# Semana de 15 a 19/08/2022


- Novo tratamento dos dados do arquivo DADOS\MICRODADOS_ENEM_2021.csv, quando fizemos a conversão para tipo int64 daquelas variáveis que estavam definidas como do tipo float64, mas que, na realidade, refletiam valores inteiros - colunas TP_STATUS_REDACAO e Q005;
- A partir destas alterações, foi criada uma nova versão atualizada do arquivo Dados_Enem_2021.csv, que servirá de base para as próximas análises;
- Atualização dos arquivos das sprints no repositório Github da equipe;
- Feitas as seguintes alterações na base de dados a ser trabalhada (Dados_Enem_2021.csv):
- Preenchidos com 0 (zero) todas as notas que estavam vazias (NaN);
- Criação de uma coluna adicional para absorver as médias aritméticas simples de cada inscrito;
- Cálculo das médias de todos os candidatos e inserção no DF;
- Atualização da base de dados (Dados_Enem_2021.csv) e posterior carregamento no Google Drive;
- Informação à equipe via Telegram destas alterações para amplo conhecimento;
- Importante lição aprendida durante as tarefas do dia: após se fazer a eliminação de uma ou mais linhas do DF através do método drop(), é crucial aplicar o método reset_index() ao respectivo DF, pois os índices das linhas também são eliminados através do drop, o que fatalmente gera erro no caso de ser necessário o acesso àqueles índices que foram eliminados. Tal fato ocorreu por ocasião do cálculo das médias, resultando em erro quando o programa tentou acessar o índice de uma linha em particular que havia sido eliminada. O método reset_index() reorganiza os índices do DF, fazendo uma renumeração dos mesmos;
- Atualização da história do usuário no repositório Github da equipe;

# Semana de 22 a 26/08/2022

- Foi feito a estrutura do **conexao_banco_de_dados.py** com os CREATE e INSERT.
- Reunião online dos integrantes da equipe com o professor referente a estrutura main.py para inserção da base de dados no banco de dados, onde o mesmo envio um exemplo para tirar como base para nosso projeto;
- Após alguns erros e correções do **conexao_banco_de_dados.py**, foi feita com sucesso a integração e população da base de dados.
- Após alguns teste concluimos que não haveria viabilidade em trabalhar com banco de dados compartilhado, pela maxividade dos dados.
- Opção pelo Big Query para armazenamento dos dados atraves **conexao_google_cloud_store.py**, a fim de agilizar as transações entre o Google Data Studio e os dados;
- Trabalhos em equipe de familiarização e utilização do Google Data Studio para filtragem dos dados e criação de gráficos/dashboards do projeto;
- Daily scrum entre os integrantes da equipe e o professor orientador do projeto para alinhamento de ideias e orientações gerais sobre o projeto;

# Semana de 29/08/2022 a 02/09/2022

##  Dia 29/08/2022
- Feita análise e divulgação de dados referentes aos índices de abstenção no ENEM 2019 para fins de comparação com dados análogos do ENEM 2021;
- Apresentação feita pelo professor de uso do Django para apresentação em páginas web do trabalho de conclusão do curso. Link da vídeo-aula em <https://drive.google.com/drive/folders/1wMUxkzHx_GAPi5Ha2J7K19kuDm3r_fTH>;
- Elaboração de um questionário com perguntas relevantes sobre os dados do ENEM 2021 e possíveis cruzamentos de informações que podem gerar análises relevantes para o projeto. Formulário se encontra no diretório do Google Drive da equipe e está disponível para contribuições de todos os integrantes;
 

## Dia 30/08/2022
- Daily scrum entre os integrantes da equipe e o professor orientador do projeto para alinhamento de ideias e orientações gerais sobre o projeto;
- Atualização de documentação geral do projeto;
- Adoção do Trello/Scrum/Kanban para melhor definição das tarefas e distribuição das atividades;

## Dia 31/08/2022
- Início dos trabalhos de análise das abstenções e médias por estados das edições do ENEM de 2017, 2018, 2019 e 2020, para possibilitar comparações com a edição de 2021, tema do nosso projeto. Neste dia, os trabalhos foram focados nos scripts para gerar os resultados;

## Dia 01/09/2022
- Daily scrum entre os integrantes da equipe;
- Atualização de documentação geral do projeto;
- Continuação dos trabalhos de análise das abstenções e médias por estados das edições do ENEM de 2017, 2018, 2019 e 2020. Neste dia, os trabalhos foram focados na correção de detalhes dos scripts e na execução, que demanda várias horas de processamento. Tarefa dividida entre os membros da equipe;
- Foi finalizado o a consulta sql **query.sql** onde fizemos toda a tradução das respostas pois a maioria dos campos de do tipo CHAR, utlizamos a documentação do enem para essa tradução com o recurso CASE no sql;

## Dia 02/09/2022
- Daily scrum entre os integrantes da equipe;
- Identificada alteração na versão do arquivo original de dados do ENEM 2021, motivando a nova execução das análises anteriormente feitas e geração da nova versão do arquivo que estava sendo tratado no projeto (Dados_Enem_2021.csv). Esta nova versão encontrada na página do INEP data de 10 ago. 2022;

## Dia 05/09/2022
- Finalizado trabalho de obtenção de dados das abstenções e médias por estados das edições do ENEM de 2017, 2018, 2019 e 2020. Arquivo com os dados pode ser encontrado no google drive da equipe;

## Dia 06/09/2022
- Reunião entre os membros da equipe durante a aula de Análise de Dados. Foi identificada a necessidade de revisão das estatísticas referentes aos anos de 2017 a 2020, no sentido de serem desconsiderados os inscritos que faltaram em um dos dias ou nos dois dias de prova e se ter uma média de notas mais representativa;

## Dia 07/09/2022
- Revisão do código das análises e entrega das estatísticas dos anos de 2017 a 2020 distribuídas por Unidade da Federação, constando de uma planilha de alunos inscritos, participantes efetivos e médias das notas do ENEM de cada ano;
- Divulgação do link de acesso ao primeiro dashboard em Data Studio resultante dos trabalhos anteriores;
- Aperfeiçoamento dos códigos das primeiras análises iniciais com o arquivo de dados do ENEM 2021 (MICRODADOS_ENEM_2021.csv) e finalização das primeiras versões dos scripts main (main.py e main.ipynb). A versão main.ipynb é destinada a execução no notebook do Jupyter e é mais rica em detalhes visuais e impressões em tela que balizaram o desenvolvimento do código e primeiras análises;
- Arquivos main foram carregados no repositório Google do projeto da turma em <https://drive.google.com/drive/u/1/folders/1KDZyz2h_34nkHKrbqSJbd4-uVIkcUrmc>;
- Criação da pasta docs/analise_inicial no Github do nosso projeto, onde foram carregados os arquivos main das análises iniciais;

## Dia 08/09/2022
- Verificado que arquivo .gitignore havia sido removido do projeto, permitindo o upload do ambiente virtual no github. Foi criado novo arquivo .gitignore e removida a pasta venv do repositório github do projeto;
- Reunião entre os membros da equipe para discussões e aprimoramento do dashbord no Google Data Studio;

## Dia 09/09/2022
- Criação da primeira versão do INSTALL.MD;
- Reunião entre os membros da equipe durante a aula de Análise de Dados. Feitos em equipe alguns aprimoramentos nos códigos em Python de interface com a Google Cloud e Big Query de forma a criar a dinamização do processo do install. Realizados primeiros testes destes scripts com sucesso;

## Dia 12/09/2022
- Foi identificado que a rotina de eliminação de linhas com valores vazios referentes às colunas de indicadores socioeconômicos do script de análise inicial dos dados se mostrou ineficiente ao tratar o arquivo de dados do Enem do ano 2020. Dessa forma, esta rotina será refatorada para o caso de algum interessado usar o projeto a ser entregue (Enem 2021) para tratar dados de outras edições do Enem, em especial a edição de 2020;
- Foi feita a refatoração dos scripts main.py e main.ipynb visando maior eficiência no tratamentos dos dados socioeconômicos. Após os teste destes scripts com arquivos dos anos de 2017 até 2021, observou-se ganho de eficiência e significativa redução de linhas nos códigos. Arquivos carregados nos repositórios Github e Google Drive deste projeto;

## Dia 13/09/2022
- Elaboração do texto (ainda não concluído) com conclusões das análises obtidas a partir dos gráficos gerados no projeto;
- Elaboração do arquivo README (ainda não concluído) com breve descrição das análises iniciais do dataset original;