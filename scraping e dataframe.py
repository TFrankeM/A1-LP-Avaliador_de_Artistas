from ast import Return
import requests
from bs4 import BeautifulSoup
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Função scrapping que vai pegar os títulos dos álbuns e retorna uma lista com os títulos.
titulo_dos_albuns = []

def TituloAlbuns(link):
    """
    TituloAlbuns 
    :param tracks_id: Lista com os id's das músicas
    :return: não retorna nada, epenas executa a função Popularidade para cada id de música
    """
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')

    titulos_albuns = soup.find_all("h3",attrs={"class": "albumTitle"})
    
    for titulo_de_album in titulos_albuns:
        titulo_dos_albuns.append(titulo_de_album.text)
    
    return titulo_dos_albuns
TituloAlbuns("https://www.vagalume.com.br/skillet/discografia/")      


# Função que faz scraping do título das músicas e retorna uma lista com os títulos
titulo_das_musicas = []

def TituloMusicas(link): 
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    titulos_musicas = soup.find_all("a", attrs={"class": "nameMusic"})
    
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

# Função que faz o scraping do ano de lançamento de cada álbum e retorna uma lista com os anos.
ano_lancamento_albuns = []

def AnoLancamentoAlbuns(link): 
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    anos_dos_lancamentos = soup.find_all("p",attrs={"class": "albumYear"})
    
    for ano_de_lancamento in anos_dos_lancamentos:
        ano_lancamento_albuns.append(ano_de_lancamento.text[0:4])
    return ano_lancamento_albuns
AnoLancamentoAlbuns("https://www.vagalume.com.br/skillet/discografia/")


# Função que faz o scraping do número de faixas que cada álbum contém e retorna uma lista com a quantidade.
num_faixas = []

def QuantidadeDeFaixas(link):
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    quantidade_de_faixas = soup.find_all("p",attrs={"class": "track"})
    
    for quantidade in quantidade_de_faixas:
        num_faixas.append(quantidade.text[2:4])
    return num_faixas
QuantidadeDeFaixas("https://www.vagalume.com.br/skillet/discografia/")


# Preciso Dar alguma descrição para essas duas funções depois!!!!!!!!!!!!!!!
titulo_dos_albuns_repetidos = []

def RepetindoAlbuns(titulo):
    for posicao, nome in enumerate(titulo[::]):
        vezes = int(num_faixas[posicao])
        for quantidade in range(0, vezes):
            titulo_dos_albuns_repetidos.append(nome)
    return titulo_dos_albuns_repetidos
RepetindoAlbuns(titulo_dos_albuns)

ano_lancamento_albuns_repetidos = []

def RepetindoAnos(anos):       
    for posicao, nome in enumerate(anos[::]):
        vezes_ano = int(num_faixas[posicao])
        for quantidade in range(0,vezes_ano):
            ano_lancamento_albuns_repetidos.append(nome)
    
    return ano_lancamento_albuns_repetidos
RepetindoAnos(ano_lancamento_albuns)


# Função para scraping do link do site que contém as páginas de todas as letras das músicas e adicionar em uma lista.
link_para_as_letras = []

def LinkLetraMusicas(link):
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    links = soup.find_all("a",attrs={"class": "nameMusic"})
    
    for link in links:
        link_para_as_letras.append(link.get("href"))
    
    return link_para_as_letras
LinkLetraMusicas("https://www.vagalume.com.br/skillet/discografia/")


# A função "LinkLetraMusica" acima não pegou o link por completo, então vamos ter que completar com "https://www.vagalume.com.br"
# para que o scraping funcione corretemente.

# Função que vai crigar uma lista com o pedaço do link que está faltando 128 vezes, que é a quantidade 
# de músicas que temos nos álbuns.
pedaco_que_falta = []

def PedacoFaltando(pedaco):
    for i in range(0,128):
        pedaco_que_falta.append(pedaco)
    return pedaco_que_falta
PedacoFaltando("https://www.vagalume.com.br")


# Função que vai juntar o pedaço que falta do link com o restante do link e adicionar em uma lista com os links completos.
link_letras_completo = []

def CompletandoLink(pedaco_que_falta):    
    for n1, n2 in zip(pedaco_que_falta, link_para_as_letras):
        link_letras_completo.append(n1 + n2)
    return link_letras_completo
CompletandoLink(pedaco_que_falta)



# Função que vai fazer o scraping das letras das músicas e adicionar em uma lista.
letras_das_musicas = []

def LetrasMusicas(link):
    site = requests.get(link).content
    soup = BeautifulSoup(site, 'html.parser')
    letras_musicas = soup.find_all("div", attrs={"id": "lyrics"})     
    
    for letra_de_musica in letras_musicas:
        letras_das_musicas.append(letra_de_musica.get_text(" "))
    return letras_das_musicas


# Função que vai percorrer link_letras_completo e para cada link nessa lista executar a função "LetrasMusicas"
# e no final teremos uma lista com QUASE todas as letras das músicas.

def QuaseTodasAsLetras(links):
    for link in links:
        LetrasMusicas(link)
QuaseTodasAsLetras(link_letras_completo)


# Repare na palavra "quase" em destaque anteriormente, isso se deve ao fato de que temos uma música que sua letra
# é colocada no site de uma forma diferente das demais, e por isso vamos ter que fazer um scraping separado para essa
# letra e depois apenas vamos adicionala no lugar que ela deveria ser originalmente, que sabemos apenas observando o site.

# Função que vai pegar a letra da musica gasoline que falta.

gasoline_letra_completa = []
def GasolineLetra(link):
    site = requests.get(link).content
    soup = BeautifulSoup(site,'html.parser')
    letra_gasoline = soup.find_all("div",attrs={"id": "lyrics"})
    for parte in letra_gasoline:
        gasoline_letra_completa.append(parte.text)
    return gasoline_letra_completa
GasolineLetra("https://www.vagalume.com.br/skillet/gasoline.html")

# Função que adiciona a letra da musica gasoline no lugar correto
def GasolineNoLugar(posicao):
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

for track_id in tracks_id:
    Popularidade(track_id)

# No spotfy, em um dos álbuns temos no álbum collide quando coletamos, aqui retiramos a popularidade dessa música
del popularity[64]


# Criando o DataFrame com os dados que temos
dataframe_skillet = pd.DataFrame(list(zip(titulo_dos_albuns_repetidos,titulo_das_musicas,
                                            ano_lancamento_albuns_repetidos,duracao_das_musicas,popularity,
                                            letras_das_musicas)),columns=["Álbuns","Músicas","Ano dos Lançamentos","Duração","Popularidade","Letras"])

# Adicionamos 0 na frente de cada duração com apenas 3 números para que a ordenação por duração funcione.
for linha, duracao in enumerate(dataframe_skillet['Duração']):
    if len(duracao) == 4:
        dataframe_skillet['Duração'].iloc[linha] = '0' + duracao

# Salvando o DataFrame como excel
dataframe_skillet.to_excel("BD - Skillet.xlsx",index=None)

