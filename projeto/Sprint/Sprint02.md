<h1 align="center"> Sprint Semana 02 </h1>

# Semana de 15 a 19/08/2022

## Dia 15/08/2022
- Novo tratamento dos dados do arquivo DADOS\MICRODADOS_ENEM_2021.csv, quando fizemos a conversão para tipo int64 daquelas variáveis que estavam definidas como do tipo float64, mas que, na realidade, refletiam valores inteiros - colunas TP_STATUS_REDACAO e Q005 - script TCC_II;
- A partir destas alterações, foi criada uma nova versão atualizada do arquivo Dados_Enem_2021.csv, que servirá de base para as próximas análises;
- Atualização dos arquivos das sprints no repositório Github da equipe;
  
## Dia 16/08/2022
- Feitas as seguintes alterações na base de dados a ser trabalhada (Dados_Enem_2021.csv):
- - Preenchidos com 0 (zero) todas as notas que estavam vazias (NaN);
- - Criação de uma coluna adicional para absorver as médias aritméticas simples de cada inscrito;
- - Cálculo das médias de todos os candidatos e inserção no DF;
- Atualização da base de dados (Dados_Enem_2021.csv) e posterior carregamento no Google Drive;
- Atualização dos scripts TC_II e TC_IV e posterior carregamento no Github;
- Informação à equipe via Telegram destas alterações para amplo conhecimento;
- Importante lição aprendida durante as tarefas do dia: após se fazer a eliminação de uma ou mais linhas do DF através do método drop(), é crucial aplicar o método reset_index() ao respectivo DF, pois os índices das linhas também são eliminados através do drop, o que fatalmente gera erro no caso de ser necessário o acesso àqueles índices que foram eliminados. Tal fato ocorreu por ocasião do cálculo das médias, resultando em erro quando o programa tentou acessar o índice de uma linha em particular que havia sido eliminada. O método reset_index() reorganiza os índices do DF, fazendo uma renumeração dos mesmos;
- Atualização dos arquivos das sprints no repositório Github da equipe;

##  Dia 19/08/2022
- Atualização da história do usuário no repositório Github da equipe;

## Continuação na Sprint 03
([Sprint da semana 03](/Sprint/Sprint03.md))
