### README - ETL do projeto.
### Os processos de leitura, análise e limpeza inicial ocorreram conforme as etapas a seguir:
- Download do arquivo MICRODADOS_ENEM_2021.csv na página https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem;
- Carregamento dos dados deste arquivo em um objeto do tipo Data Frame da biblioteca Pandas da linguagem Python;
- Análise preliminar deste conjunto de dados, verificando adequação dos atributos ao dicionário do ENEM 2021, tipos dos dados, verificação de possível existência de registros duplicados, estatísticas de colunas com valores vazios e seleção das colunas e variáveis que farão parte do contexto da análise posterior;
- Trabalhos de limpeza e tratamento dos dados, consistindo em:
  - eliminação de linhas com indicadores socioeconômicos vazios;
  - análise da condição de treineiro no Enem 2021 e verificação de sua aplicabilidade nas análises;
  - criação de uma coluna adicional para as médias dos candidatos;
  - mudança de tipo float da variável “Q005” para int;
  - preenchimento de valores da variável “TP_STATUS_REDACAO” vazias com o valor 4;
  - mudança de tipo float da variável “TP_STATUS_REDACAO” para int;
  - preenchimento com 0 (zero) das células de notas vazias;
  - cálculo e preenchimento das médias de cada inscrito;
  - Criação de um Data Frame apenas com as variáveis de interesse para o projeto;
Todas estas etapas podem ser conferidas no script main.ipynb em Jupyter Notebook na pasta docs.

### Populando base de dados:
No arquivo schema.py são coletados dinamicamente os atributos e valores gerados pelo script analise.py e executa a população em uma tabela no conjunto de dados da BigQuery;

### Criação da VIEWS:
Acessando o projeto, é feita a criação e tradução de novos atributos e valores que serão utilizados nos painéis através do comando em SQL-CASE.

Para melhor compreensão e traduções adicionais, pode ser consultado o arquivo microdados_enem_2021.zip dentro da pasta Dicionário/Dicionário Microdados Enem 2021.xlsx.
