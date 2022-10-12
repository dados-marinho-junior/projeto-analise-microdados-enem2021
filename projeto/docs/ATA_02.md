
# Ata 02 - Reuniões de Setembro

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

## Dia 15/09/2022
- Testes para a população **BigQuery**
## Dia 16/09/2022
- O professor orientou o grupo sobre a instalação do Heroku

## Dia 20/09/2022

## Dia 22/09/2022

## Dia 23/09/2022

## Dia 27/09/2022

## Dia 29/09/2022

## Dia 30/09/2022
