import requests
from bs4 import BeautifulSoup
import pandas as pd


# Função scrapping que vai pegar os títulos dos álbuns, nome das músicas e ano 
# de lançamento dos álbuns e colocalos em uma lista
titulo_dos_albuns = []
titulo_das_musicas = []
ano_lancamento_albuns = []
num_faixas = []

def AlbumsInfo(url):
    
    # Pegando todo o código da página.
    site = requests.get(url).content
    soup = BeautifulSoup(site, 'html.parser')
    
    # Pegando apenas as partes do código que queremos, títulos dos albuns e músicas e ano de lançamento do álbum.
    classes_album_titles= soup.find_all("h3",attrs={"class": "albumTitle"})
    classes_name_of_musics = soup.find_all("a", attrs={"class": "nameMusic"})
    classes_year_of_releases = soup.find_all("p",attrs={"class": "albumYear"})
    quantidade_de_faixas = soup.find_all("p",attrs={"class": "track"})
    
    # Pegando agora os TEXTOS que nos interessa e adicionando nas listas.
    
    for titulo_de_album in classes_album_titles:
        titulo_dos_albuns.append(titulo_de_album.text)
    
    for titulo_de_musica in classes_name_of_musics:
        titulo_das_musicas.append(titulo_de_musica.text)            
    
    for ano_de_lancamento in classes_year_of_releases:
        ano_lancamento_albuns.append(ano_de_lancamento.text[0:4])
    
    for quantidade in quantidade_de_faixas:
        num_faixas.append(quantidade.text[2:4])

AlbumsInfo("https://www.vagalume.com.br/skillet/discografia/")            


# Repetindo o nome de cada álbum a quantidade de músicas que temos naquele álbum.

titulo_dos_albuns_repetidos = []    
for posicao, nome in enumerate(titulo_dos_albuns[::]):
    vezes = int(num_faixas[posicao])
    for quantidade in range(0, vezes):
        titulo_dos_albuns_repetidos.append(nome)

# Repetindo o ano de lançamento de cada álbum a quandidade de músicas que temos naquele álbum.

ano_lancamento_albuns_repetidos = []
for posicao, nome in enumerate(ano_lancamento_albuns[::]):
    vezes_ano = int(num_faixas[posicao])
    for quantidade in range(0,vezes_ano):
        ano_lancamento_albuns_repetidos.append(nome)


# Criando o DataFrame com os dados que já temos.

df = pd.DataFrame(list(zip(titulo_dos_albuns_repetidos,
                           titulo_das_musicas,
                           ano_lancamento_albuns_repetidos)),
                           columns=["Nome dos ÁLbuns","Nome das Músicas","Ano dos Lançamentos"])

# Função para pegar o link onde contém a letra de cada música.

link_para_as_letras = []

def LinkLetrasMusicas(link):
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    links = soup.find_all("a",attrs={"class": "nameMusic"})
    
    # Pegando cada link e adicionando em uma lista.
    
    for link in links:
        link_para_as_letras.append(link.get("href"))

LinkLetrasMusicas("https://www.vagalume.com.br/skillet/discografia/")

    







