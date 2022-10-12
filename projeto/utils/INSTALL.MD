 1) Acessar portal do INEP em <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem> e clicar em Microdados do Enem 2021 ou ano que preferir entre 2017 a 2021, pois seguem o mesmo padrão de colunas;

1.1) Alternativamente acessar o link <https://download.inep.gov.br/microdados/microdados_enem_2021.zip> caso opte por trabalhar com os dados de 2021;

2) Extrair o arquivo MICRODADOS_ENEM_2021.csv. Se optar por manter o arquivo no repositório do projeto, importante referenciar o mesmo no .gitignore;

3) Na pasta projeto/settings.py inserir as informações solicitadas;
3.1) Neste ponto, seu equipamento deve estar autorizado para uso do projeto do BigQuery. Maiores informações, acesse ([Link do Arquivo](../README.MD "README.MD"))

4) Executar o script main.py e aguardar todo o processo;

5) Nesta etapa do projeto já terá a VIEWS montada, estão você pode usar a SQL
para qualquer seguimento como **TABLEAU, POWER BI** entre outros. Nós utilizamos
o **DATA STUDIO** para análise, você pode copiar o modelo neste link
<https://datastudio.google.com/reporting/c8a3e394-759a-4082-84d9-e7d59e22d525>
Clicando no **( ⋮ )** e selecionar, fazer uma cópia referenciando sua fonte de dados do BigQuery.

5.1)Para consulta de atualizações de campos você pode consultar o arquivo baixado microdados_enem_2021.zip dentro da pasta Dicionário/Dicionário_Microdados_Enem_2021.xlsx;
