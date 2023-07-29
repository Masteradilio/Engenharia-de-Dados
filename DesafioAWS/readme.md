# Desafio AWS

## Programa de estágio em Engenharia de Dados AWS da Compass.UOL

O desafio consistiu em simular um projeto real de engenharia de dados, criando um pipeline completo que vai do ETL até a exibição de um Dashboard.
O tema do desafio era o de juntar diferentes fontes de informação de filmes e séries vindo de fontes como TMDB (The Movie Database) e de classificação
do IMDB para no final definir uma análise baseada em filmes e séries do gênero de Sci-Fi e Fantasy.

### Etapa 1: Ingestão Batch de arquivo local para a camada RAW do Data Lake

Na primeira parte, realizamos um upload de um arquivo local para um bucket S3 que passou a ser o Data Lake do projeto. 
O arquivo trata-se de informações de filmes e atores e a classificação do IMDB e é demasiado grande, acima do limite permitido pelo Github. 
Usamos um script python para subir o arquivo através de um contêiner linux em Docker com as devidas permissões do AWS S3.

![Desafio parte 1 - Ingestão Batch csv para bucket S3](https://github.com/Masteradilio/Engenharia-de-Dados/assets/122137421/14beb7bb-bea7-4b05-aa2f-dfe54c2a1e2f)


### Etapa 2: Ingestão Streaming de arquivo do TMDB via API para a camada RAW do Data Lake

Na segunda parte fizemos uma conexão via API para consumir os dados de filmes e séries do TMDB usando uma função lambda para executar o job de ingestão e 
salvar na camada RAW como arquivo JSON sem realizar nenhuma transformação, deixando o arquivo bruto, mas nessa etapa já selecionei os dados que queria
trabalhar e subi apenas dados de filmes das franquias mais famosas de Fantasy e Sci-Fi, um total de 7 franquias dando 39 filmes.

![Ingestão streaming TMDB para bucket S3.png](DesafioAWS/images/Desafio parte 2 - Ingestão streaming TMDB para bucket S3.png)


### Etapa 3: Transformação dos dados e salvamento na camada Trusted (TRT) do Data Lake

Na terceira parte começamos a fase de Transformação do processo de ETL e fizemos limpezas e criação de novas colunas e adequação de tipos de dados nos dados brutos
usando Jobs Spark do AWS Glue, salvando os arquivos em formato Parquet e criando uma nova camada no Data Lake chamada Trusted, com dados mais propícios para uso, 
mas ainda não finalizados para a análise. Após isso, usamos o AWS Athena e o Glue Catalog para criar a partir dos arquivos parquet a camada Refined (REF) com o
modelo dimensional propício para ser consumido pelo AWS Quicksight e gerar o dashboard.

![Transformação dos dados para a camada Trusted.png](DesafioAWS/images/Desafio parte 3 - Transformação dos dados para a camada Trusted.png)


### Etapa 4: Criação de visualizações e análise de insights

Nessa fase do projeto, criamos databases no AWS Quicksight com os dados do modelo dimensional criado na etapa anterior para criar as análises do dashboard.
Nessa etapa verificamos alguns problemas e erros que nos fizeram retornar à etapa anterior e criar novas views no Athena com as tabelas dimensionais e a fato
para adequar ainda mais os tipos de dados das colunas que não estavam sendo reconhecidos adequadamente pelo Quicksight e também estavam gerando erros.

![Criação do modelo dimensional na camada Refined.png](DesafioAWS/images/Modelo Dimensional.png)


### Etapa 5: Criação do Dashboard e apresentação aos stakeholders

Na fase final fizemos a criação de um dashboard no Quicksight analisando as 7 franquias de Sci-Fi e Fantasy mostrando KPIs de interesse como qual o filme que obteve 
o maior lucro financeiro e a maior taxa de retorno, qual obteve prejuízo arrecadando menos do que gastou na produção, quantos dólares retornavam para cada 1 dólar investido
qual o filme ou franquia mais popular, quais atores participaram de cada filme e em quantos participaram em toda a franquia, o marketshare da franquia em proporção comparada
às demais e um mapa de calor mostrando quais classificações de gêneros o filme ou franquia se enquadravam.

![Dashboard_Completo.pdf](DesafioAWS/images/Dashboard_Completo.pdf)


O projeto encerrou com uma apresentação gravada em vídeo explicando todas as etapas do projeto e mostrando a execução do código para os avaliadores do programa de bolsa 
da Compass.UOL.

