<h1 align="center">Linguagem de Programação - A1</h1>
<h2 align="center">Avaliação de Bandas</h2>
<p>
Este repositório foi criado por Ricael Daniel Vieira da Silva, Thiago Franke Melchiors e Thiago Poganski, alunos do 2º período de Ciência de Dados da EMAp - FGV, para armazenar a Avaliação 1 de Linguagem de Programação: Análise de uma banda ou artista.
<hr>
Para avaliar a discografia da banda Skillet, desenvolvemos os módulos que estão salvos nesse repositório. Podemos dividi-los em 3 grupos, de acordo com suas responsabilidades:
</p>

<h3>Scraping e dataframe</h3>
<p>
O módulo “<i>scraping e dataframe.py</i>” possui as funções de scraping e APIs utilizadas para coletar os dados da banda Skillet: os álbuns, o ano do seu lançamento e o número de premiações, as músicas, a sua duração, popularidade e letra. As informações obtidas por esse módulo são salvas como “<i>BD - Skillet.xlsx</i>”.
</p>

<h3>Perguntas de negócio</h3>
<p>
O módulo “<i>perguntas.py</i>” contém as funções de análise do banco de dados da banda. O conteúdo produzido pelo módulo de perguntas é organizado pela “<i>interface.py</i>” de uma forma visualmente harmônica aos olhos no console do editor de código. Essa etapa de perguntas de negócio deve ser executada a partir de “<i>main.py</i>”.
</p>

<h3>Visualização</h3>
<p>
As funções que geram as peças de visualização estão contidas no módulo “<i>graficos.py</i>”. Essa etapa é ativada por meio do arquivo “<i>executargraficos.py</i>”.
<br>
As visualizações podem ser encontradas dentro da pasta “<i>imagens</i>” ou no arquivo “<i>Visualizações.pdf</i>”.
</p>
<hr>

<h3>Requisitos</h3>
<p>
É imprescindível que os bancos de dados “<i>BD - Skillet.xlsx</i>” e “<i>Positive and Negative Word List.xlsx</i>” estejam salvos na mesma pasta que o restante dos módulos desse repositório para que a execução do código não falhe. Outrossim, instale as seguintes bibliotecas para rodar o código perfeitamente::
</p>
<ol>
<li>Requests</li>
<li>Spotipy</li>
<li>Return</li>
<li>BeautifulSoup</li>
<li>SpotifyClientCredentials</li>
<li>Numpy</li>
<li>Pandas</li>
<li>Warnings</li>
<li>matplotlib.pyplot</li>
<li>Seaborn</li>
<li>Pathlib</li>
<li>Wordcloud</li>
<li>Sys, os</li>
</ol>
