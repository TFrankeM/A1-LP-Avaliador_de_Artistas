import requests
import pandas as pd
import spotipy
import numpy as np
from ast import Return
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials


titulo_dos_albuns = []

def TituloAlbuns(link):
    """
    TituloAlbuns Faz o scraping dos títulos dos álbuns da banda skillet no site vagalume.
    :param link: Link do site vagalume que vai ser utilizado no scraping.
    :return: Retorna uma lista com os títulos dos álbuns da banda. 
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')

    titulos_albuns = soup.find_all("h3",attrs={"class": "albumTitle"})
    
    for titulo_de_album in titulos_albuns:
        titulo_dos_albuns.append(titulo_de_album.text)
    
    return titulo_dos_albuns
TituloAlbuns("https://www.vagalume.com.br/skillet/discografia/")      


titulo_das_musicas = []

def TituloMusicas(link):
    """
    TituloMusicas Faz o scraping dos títulos das músicas de cada álbum da banda skillet.
    :param link: Link do site vagalume que vai ser utilizado no scraping.
    :return: Retorna uma lista com os títulos das músicas de cada álbum da banda. 
    """ 
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    titulos_musicas = soup.find_all("a", attrs={"class": "nameMusic"})
    
    # Colocando o nome da música que falta, e retirandao partes dos nomes que temos nos nomes das músicas que não interessa.
    for titulo_de_musica in titulos_musicas:
        if titulo_de_musica.text == '':
            titulo_das_musicas.append('Vapor')

        elif '(tradução)' in titulo_de_musica.text:
            titulo_das_musicas.append(titulo_de_musica.text.replace(' (tradução)', ''))
                
        elif '(Bonus)' in titulo_de_musica.text:
            titulo_das_musicas.append(titulo_de_musica.text.replace(' (Bonus)', ''))
                           
        else:
            titulo_das_musicas.append(titulo_de_musica.text)
    
    return titulo_das_musicas    
TituloMusicas("https://www.vagalume.com.br/skillet/discografia/")


ano_lancamento_albuns = []

def AnoLancamentoAlbuns(link):
    """
    AnoLancamentoAlbuns Faz o scraping dos anos de lançamento dos álbuns da banda skillet.
    :param link: Link do site vagalume que vai ser utilizado no scraping.
    :return: Retorna uma lista com os anos de lanlamentos dos álbuns. 
    """  
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    anos_dos_lancamentos = soup.find_all("p",attrs={"class": "albumYear"})
    
    for ano_de_lancamento in anos_dos_lancamentos:
        ano_lancamento_albuns.append(ano_de_lancamento.text[0:4])

    return ano_lancamento_albuns
AnoLancamentoAlbuns("https://www.vagalume.com.br/skillet/discografia/")


num_faixas = []

def QuantidadeDeFaixas(link):
    """
    QuantidadeDeFaixas Faz o scraping da quantidade de faixas dos álbuns da banda skillet.
    :param link: Link do site vagalume que vai ser utilizado no scraping.
    :return: Retorna uma lista com as quantidades de faixas de cada álbum álbuns. 
    """  
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    quantidade_de_faixas = soup.find_all("p",attrs={"class": "track"})
    
    for quantidade in quantidade_de_faixas:
        num_faixas.append(quantidade.text[2:4])

    return num_faixas
QuantidadeDeFaixas("https://www.vagalume.com.br/skillet/discografia/")


titulo_dos_albuns_repetidos = []

def RepetindoAlbuns(titulo):
    """
    RepetindoAlbuns repeti o nome do álbum em uma quantidade de vezes igual ao número de faixas que tem o álbum.
    :param titulo: lista com título de todos os álbuns da banda.
    :return: Retorna uma lista com os títulos dos álbuns repetidos. 
    """  
    for posicao, nome in enumerate(titulo[::]):
        vezes = int(num_faixas[posicao])
        for quantidade in range(0, vezes):
            titulo_dos_albuns_repetidos.append(nome)

    return titulo_dos_albuns_repetidos
RepetindoAlbuns(titulo_dos_albuns)


ano_lancamento_albuns_repetidos = []

def RepetindoAnos(anos):
    """
    RepetindoAnos repeti o ano de lançamento dos álbuns um número de vezes igual a quantidade de faixas que temos o álbum da banda skillet.
    :param anos: lista com os anos de lançamento dos álbuns.
    :return: Retorna uma lista com os anos de lançamentos repetidos. 
    """         
    for posicao, nome in enumerate(anos[::]):
        vezes_ano = int(num_faixas[posicao])
        for quantidade in range(0,vezes_ano):
            ano_lancamento_albuns_repetidos.append(nome)
    
    return ano_lancamento_albuns_repetidos
RepetindoAnos(ano_lancamento_albuns)


link_para_as_letras = []

def LinkLetraMusicas(link):
    """
    LinkLetraMusicas pega no site vagalume o link para todas as letras das músicas da banda skillet.
    :param link: Link do site vagalume onde será feito o scraping.
    :return: Retorna uma lista com os links de todas as letras da banda. 
    """  
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    links = soup.find_all("a",attrs={"class": "nameMusic"})
    
    for link in links:
        link_para_as_letras.append(link.get("href"))
    
    return link_para_as_letras
LinkLetraMusicas("https://www.vagalume.com.br/skillet/discografia/")


pedaco_que_falta = []

def PedacoFaltando(pedaco):
    """
    PedacoFaltando Faz uma lista com o pedaço "https://www.vagalume.com.br" que falta quando pegamos o link para as letras.
    :param pedaco: Parte do link que falta.
    :return: Retorna uma lista com o pedaço do link que falta repetido 128 vezes, ou seja a quantidade de músicas. 
    """ 
    for i in range(0,128):
        pedaco_que_falta.append(pedaco)

    return pedaco_que_falta
PedacoFaltando("https://www.vagalume.com.br")


link_letras_completo = []

def CompletandoLink(pedaco_que_falta):
    """
    CompletandoLink completo o link para música.
    :param pedaco_que_falta: Lista com o pedaço que falta repetido 128 vezes.
    :return: Retorna uma lista com o link completo para as letras das músicas. 
    """     
    for n1, n2 in zip(pedaco_que_falta, link_para_as_letras):
        link_letras_completo.append(n1 + n2)

    return link_letras_completo
CompletandoLink(pedaco_que_falta)


letras_das_musicas = []

def LetrasMusicas(link):
    """
    LetrasMusicas pega a letra de quase todas as músicas da banda skillet.
    :param link: link da letra.
    :return: Retorna uma lista com as letras das músicas. 
    """     
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    letras_musicas = soup.find_all("div", attrs={"id": "lyrics"})     
    
    for letra_de_musica in letras_musicas:
        letras_das_musicas.append(letra_de_musica.get_text(" "))
        
    return letras_das_musicas


# Pegando cada link de letra de música e executando a função LetrasMusicas para pegar a letra de quase todas as letras.
for link in link_letras_completo:
    LetrasMusicas(link)


gasoline_letra_completa = []

def GasolineLetra(link):
    """
    GasolineLetra, a música gasoline está disposta no site de forma diferente, por isso temos que fazer o scraping da sua letra separadamente.
    :param link: link da letra da música gasoline.
    :return: Retorna uma lista com a letra da música gasoline. 
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    letra_gasoline = soup.find_all("div",attrs={"id": "lyrics"})
    
    for parte in letra_gasoline:
        gasoline_letra_completa.append(parte.text)
    
    return gasoline_letra_completa
GasolineLetra("https://www.vagalume.com.br/skillet/gasoline.html")


def GasolineNoLugar(posicao):
    """
    GasolineNoLugar coloca a letra da música no lugar correto, que sabemos pelo site onde elas se encontram.
    :param posicao: posição em que a música gasoline se encontra no site.
    :return: Adiciona a letra da música gasoline na lista de letras no lugar correto. 
    """
    letras_das_musicas.insert(posicao, gasoline_letra_completa[0])
GasolineNoLugar(26)


duracao_das_musicas =  []

def DuracaoDominion(link):
    """
    DuracaoDominion encontra a duração de cada música do álbum dominion
    :param link: Link para o site que contém a duração de cada música do álbum Dominion
    :return: Adiciona a duração de cada música do álbum Dominion a lista de duração de todas as músicas da banda
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("time",attrs={"class": "songs-list-row__length"})
    
    for duracao in tempo_duracao:
        duracao_das_musicas.append(duracao.get_text(strip=True))
        
    return duracao_das_musicas
DuracaoDominion("https://music.apple.com/pt/album/dominion/1585664659")


def DuracaoUnleashed(link):
    """
    DuracaoUnleashed encontra a duração de cada música do álbum Unleashed
    :param link: Link para o site que contém a duração de cada música do álbum Unleashed
    :return: Adiciona a duração de cada música do álbum Unleashed a lista de duração de todas as músicas da banda
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("time",attrs={"class": "songs-list-row__length"})
    
    for duracao in tempo_duracao:
        duracao_das_musicas.append(duracao.get_text(strip=True))
        
    return duracao_das_musicas
DuracaoUnleashed("https://music.apple.com/br/album/unleashed/1114195788")


def DuracaoRise(link):
    """
    DuracaoRise encontra a duração de cada música do álbum Rise
    :param link: Link para o site que contém a duração de cada música do álbum Rise
    :return: Adiciona a duração de cada música do álbum Rise a lista de duração de todas as músicas da banda
    """
    duracao_rise = []
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("time",attrs={"class": "songs-list-row__length"})
    
    for duracao in tempo_duracao:
        duracao_rise.append(duracao.get_text(strip=True))
        
    for duracao in duracao_rise[0:15]:
        duracao_das_musicas.append(duracao)
    
    return duracao_das_musicas
DuracaoRise("https://music.apple.com/br/album/rise-deluxe-edition/662457451")


def DuracaoAwake(link):
    """
    DuracaoAwake encontra a duração de cada música do álbum Awake
    :param link: Link para o site que contém a duração de cada música do álbum Awake
    :return: Adiciona a duração de cada música do álbum Awake a lista de duração de todas as músicas da banda
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("time",attrs={"class": "songs-list-row__length"})
    
    for duracao in tempo_duracao:
        duracao_das_musicas.append(duracao.get_text(strip=True))

    return duracao_das_musicas
DuracaoAwake("https://music.apple.com/br/album/awake/326077729")


def DuracaoComatose(link):
    """
    DuracaoComatose encontra a duração de cada música do álbum Comatose
    :param link: Link para o site que contém a duração de cada música do álbum Comatose
    :return: Adiciona a duração de cada música do álbum Comatose a lista de duração de todas as músicas da banda
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("time",attrs={"class": "songs-list-row__length"})

    for duracao in tempo_duracao:
        duracao_das_musicas.append(duracao.get_text(strip=True))

    return duracao_das_musicas
DuracaoComatose("https://music.apple.com/br/album/comatose/193381606")


def DuracaoCollide(link):
    """
    DuracaoCollide encontra a duração de cada música do álbum Collide
    :param link: Link para o site que contém a duração de cada música do álbum Collide
    :return: Adiciona a duração de cada música do álbum Collide a lista de duração de todas as músicas da banda
    """
    duracao_collide = []
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("td",attrs={"class": "tracklist-length"})
    
    for duracao in tempo_duracao:
        duracao_collide.append(duracao.get_text(strip=True))
    
    for duracao in duracao_collide[0:10]:
        duracao_das_musicas.append(duracao)

    return duracao_das_musicas
DuracaoCollide("https://en.wikipedia.org/wiki/Collide_(Skillet_album)")


def DuracaoAlien(link):
    """
    DuracaoAlien encontra a duração de cada música do álbum Alien
    :param link: Link para o site que contém a duração de cada música do álbum Alien
    :return: Adiciona a duração de cada música do álbum Alien a lista de duração de todas as músicas da banda
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("time",attrs={"class": "songs-list-row__length"})
    
    for duracao in tempo_duracao:
        duracao_das_musicas.append(duracao.get_text(strip=True))
        
    return duracao_das_musicas
DuracaoAlien("https://music.apple.com/br/album/alien-youth/1502167776")


def DuracaoArdent(link):
    """
    DuracaoArdent encontra a duração de cada música do álbum Ardent
    :param link: Link para o site que contém a duração de cada música do álbum Ardent
    :return: Adiciona a duração de cada música do álbum Ardent a lista de duração de todas as músicas da banda
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("td",attrs={"class": "tracklist-length"})
    
    for duracao in tempo_duracao:
        duracao_das_musicas.append(duracao.get_text(strip=True))
        
    return duracao_das_musicas
DuracaoArdent("https://en.wikipedia.org/wiki/Ardent_Worship")


def DuracaoInvencible(link):
    """
    DuracaoInvencible encontra a duração de cada música do álbum Invencible
    :param link: Link para o site que contém a duração de cada música do álbum Invencible
    :return: Adiciona a duração de cada música do álbum Invencible a lista de duração de todas as músicas da banda
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("time",attrs={"class": "songs-list-row__length"})
    
    for duracao in tempo_duracao:
        duracao_das_musicas.append(duracao.get_text(strip=True))

    return duracao_das_musicas
DuracaoInvencible("https://music.apple.com/br/album/invincible/1502265525")


def DuracaoHey(link):
    """
    DuracaoHey encontra a duração de cada música do álbum Hey
    :param link: Link para o site que contém a duração de cada música do álbum Hey
    :return: Adiciona a duração de cada música do álbum Hey a lista de duração de todas as músicas da banda
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("time",attrs={"class": "songs-list-row__length"})
    
    for duracao in tempo_duracao:
        duracao_das_musicas.append(duracao.get_text(strip=True))
        
    return duracao_das_musicas
DuracaoHey("https://music.apple.com/br/album/hey-you-i-love-your-soul/1502163392")


def DuracaoSkillet(link):
    """
    DuracaoSkillet encontra a duração de cada música do álbum Skillet
    :param link: Link para o site que contém a duração de cada música do álbum Skillet
    :return: Adiciona a duração de cada música do álbum Skillet a lista de duração de todas as músicas da banda
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    tempo_duracao = soup.find_all("time",attrs={"class": "songs-list-row__length"})
    
    for duracao in tempo_duracao:
        duracao_das_musicas.append(duracao.get_text(strip=True))
        
    return duracao_das_musicas
DuracaoSkillet("https://music.apple.com/br/album/skillet/1502161585")


# Credenciais para podermos pegar os dados da api do spotfy
client_credentials_manager = SpotifyClientCredentials(client_id="bd17a12d5a91497d96e1390cfe2a96bd", client_secret="f300c3af0a6e4793bf72a57bd95fec18") 
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


tracks_id = []

def TracksID(album_id):
    """
    TracksID encontra o id de todas as músicas do álbum
    :param album_id: Id do álbum que queremos retirar od id's das músicas
    :return: Retorna uma lista com todos os id's que queremos
    """
    id = sp.album(album_id)         
    
    for item in id['tracks']['items']:
        tracks_id.append(item['id'])    
    return tracks_id


# Lista com os id's dos álbuns na ordem que aparecem no scraping 
albums_id = ["1ZUW7enyVvaUZgkcWXk6wG?si=hAxK4BTHSqGGL0m_PTf64Q","4rJu3hBFAUqIAQOlSStJzO?si=0LN3bNB0RGig7jJtnAYUhA", 
             "3AUIurHdBrfvqSs7EEr3AA?si=6iebAsEBSReJWOBYaDOO_A","0RySAmM6oDPGSE03X3dzi1?si=hLlBgzfFQo2cxSo1sLWGNg",
             "16ElbnOtY2UgGaPKoLfst4?si=kqlaN6KvT3yLUPLykc4IDA","77JbhmUqfoId7D2AHKU4zW?si=thIOQSFISLqF_dU8ZizJ1A",
             "5AffZsDjtfhfUhLCkjvypp?si=HLjL22RESS-yZMt54_xkPA","2X7l4NkRy7rgVbTg5oqGor?si=EikYkeEyT2eshz4VK6Vk_A",
             "5tzRPb7jOVIiERbbxlCIAD?si=Jk4TfTLVTqGxuyFIcRVv5A","54Zw7y8v7XDO38tNvzzbcU?si=mKVQltCLRUmfSHbLtdO-Mw",
             "5PUVPlbwm347Jt0Vdcw3s5?si=COUbyWdiR9uazcH0ryIBAw"]


# Executando a função TracksID para cada link de álbum 
for album_id in albums_id:
    TracksID(album_id)      


popularity = []

def Popularidade(id):
    """
    Popularidade encontra a popularidade de cada música de um álbum no spotfy
    :param id: id de cada música do álbum
    :return: Retorna uma lista com as popularidades de cada música contida nos álbuns da banda skillet
    """
    track_results = sp.track(id, market=None)
    popularity.append(track_results['popularity'])

    return popularity


# Executando a função Popularidade para cada link de música.
for id in tracks_id:
    Popularidade(id)

# No spotfy, em um dos álbuns temos no álbum collide quando coletamos, aqui retiramos a popularidade dessa música
del popularity[64]

premios = []
def Premios(qt1,qt2,qt3,qt4,qt5,qt6):
    """
    Premios retorna uma lista com os pêmios de cada álbum da banda skillet, premios de álbuns foram adicionados 
    para todas as músicas daquele álbum, analogamente aos prêmios individuais de músicas, que cada prêmio foi 
    somado a todas as múscias de cada álbum.
    :param qt1,qt2,qt3,qt4,qt5,qt6: Quantidades usadas para adicionar os prêmios, essas quantidades são baseadas na quantidade de músicas
    :return: Retorna uma lista com as quantidades de prêmios que cada álbum recebeu.
    """
    # Premios do álbum Dominion.
    premios_dominion = np.zeros(qt1,dtype=int)
    for item in premios_dominion:
        premios.append(item)
    
    # Premios do álbum Unleashed.
    premios_Unleashed = np.zeros(qt2,dtype=int)
    for premio in premios_Unleashed:
        premios.append(premio)
    
    # Premios do álbum Rise.
    premios_Rise = np.ones(qt3,dtype=int)*3
    for premio in premios_Rise:
        premios.append(premio)
    
    # Premios do álbum Awake.
    premios_awake = np.ones(qt4,dtype=int)
    for premio in premios_awake:
        premios.append(premio)

    # Premios do álbum Comatose.
    premios_comatose  = np.ones(qt5,dtype=int)
    for premio in premios_comatose:
        premios.append(premio)
    
    # O restante dos álbuns não tem prêmio algum.
    premios_restantes  = np.zeros(qt6,dtype=int)
    for premio in premios_restantes:
        premios.append(premio)

    return premios
Premios(12,12,15,12,11,66)



# Criando o DataFrame com os dados que temos
dataframe_skillet = pd.DataFrame(list(zip(titulo_dos_albuns_repetidos,titulo_das_musicas,
                                            ano_lancamento_albuns_repetidos,duracao_das_musicas,popularity,
                                            premios,letras_das_musicas)),columns=["Álbuns","Músicas","Ano dos Lançamentos",
                                                                                  "Duração","Popularidade","Prêmios","Letras"])

# Adicionamos 0 na frente de cada duração com apenas 3 números para que a ordenação por duração funcione.
for linha, duracao in enumerate(dataframe_skillet['Duração']):
    if len(duracao) == 4:
        dataframe_skillet['Duração'].iloc[linha] = '0' + duracao

# Salvando o DataFrame como excel
dataframe_skillet.to_excel("BD - Skillet.xlsx",index=None)

