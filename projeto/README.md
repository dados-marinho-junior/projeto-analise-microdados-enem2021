## Histórico de Desenvolvimento

Neste arquivo pontuaremos o desenvolvimento do projeto.

### 1ª Etapa:
- Definição do Projeto, decidimos analisar os dados do ENEM de 2021;
- Obtenção do arquivo no site do INEP em formato CSV;
- Estudo da documentação;
- Criado um quadro no **Trello** para aplicação das metodologias ágeis (**SCRUM**, **KANBAN**).

### 2ª Etapa:
- Definição das variáveis que serão utilizadas no projeto;
- Análise inicial utilizando o **Pandas** no **Jupyter Notebook**;
- Aplicação de ETL no projeto (Extração, Tratamento e Carregamento).

### 3ª Etapa:
- Criação de um script para conexão com banco de dados Mysql;
- Feita a integração e população de dados em uma base de dados compartilhada;
   - Essa opção se mostrou ineficaz pela massividade dos dados(descontinuado);
   - Optamos pelo uso do **BigQuery**, base de dados permanente em Cloud.

### 4ª Etapa:
- Feita a integração e autorização de máquina para uso do **BigQuery**;
- Convertemos o script de conexão para o uso do **BigQuery**;
- Teste iniciais na construção e no uso de gráficos no **Google Data Studio**.

### 5ª Etapa:
- Elaboração de um questionário com perguntas relevantes sobre os dados do 
ENEM 2021 e possíveis cruzamentos de informações que podem gerar análises
relevantes para o projeto;
- Criação de um script VIEWS para tradução do atributos oriundos da
base de dados;
- Criação e formalização dos gráficos nas dashboards no
**Google Data Studio**.

### 6ª Etapa:
- Automatização dos processos:
   - Criação do script **settings.py** que configura o app;
   - Criação do script **analise.py** que executa a ETL do projeto;
   - Criação do script **schema.py** que recebe o DataFrame do script 
   **analise.py** e faz a criação e população de dados em uma tabela
   no **BigQuery**;
   - Criação do script **views.py** que acessa o **BigQuery** e
   faz a tradução do conteúdo;
   - Criação do script **main.py** que executa o app.

### 7ª Etapa:
- Instalação e configuração do framework web **Django**;
- Estilização do framework;
- Criação de um video tutorial, FAQ e conteúdo para o projeto;
- Analise dos dados de 2017 a 2021 para comparativos;
    - Criação de gráficos com o uso **HighCharts** para visualização.

### 8ª Etapa:
- Utilização do **Heroku** para hospedagem e publicação do app.
- Configuração do **PostgreSql** para população de dados de 2017 até 2021;
- Criação da  estrutura **JSON** para o result_set do **HighCharts**;
- Deploy do projeto.
















