### INSTALL EM PRODUÇÃO:

1) Acessar portal do INEP em <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem> e clicar em Microdados do Enem 2021 ou Ano que preferir entre 2017 à 2021 que seguem o mesmo padrão de colunas;

    1.1) Se decidir utilizar outro anos verificar o arquivo "pasta/nome do arquivo" 
    para efetuar novo tramento se necessario. Atualizando o arquivo setup.py

2) Alternativamente acessar diretamente o link <https://download.inep.gov.br/microdados/microdados_enem_2021.zip>;

3) Extrair o arquivo MICRODADOS_ENEM_2021.csv, se quiser manter o arquivo no repositorio do projeto, importante referenciar o mesmo no .gitignore;

4) na pasta projeto/settings.py inserir a informações solicitadas;

5) Executar o script main.py, aquardar todo o processo

6) Nesta etapa do projeto ja terá o VIEWS montada, estão voce pode a SQL
para qualquer seguimento como TABLEU, POWER BI entre outros. Nos utilizamos
o DATA STUDIO para análize, voce pode copiar o modelo neste link
<https://datastudio.google.com/reporting/c8a3e394-759a-4082-84d9-e7d59e22d525>
Cliando no (⋮) e selecionar, Fazer uma Cópia referenciando sua fonte de dados do BIG QUERY
 