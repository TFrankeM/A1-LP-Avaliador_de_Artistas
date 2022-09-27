import requests
from bs4 import BeautifulSoup


url = "https://www.vagalume.com.br/skillet/discografia/"


# Função scrapping que vai pegar os títulos dos álbuns, nome das músicas e ano 
# de lançamento dos álbuns e colocalos em uma lista

def AlbumsTitle(url):
    album_titles = []
    name_of_musics = []
    year_of_releases = []

    # Pegando todo o código da página.
    site = requests.get(url).content
    soup = BeautifulSoup(site, 'html.parser')
    
    # Pegando apenas as partes do código que queremos, títulos dos albuns e músicas e ano de lançamento do álbum.
    classes_album_titles= soup.find_all("h3",attrs={"class": "albumTitle"})
    classes_name_of_musics = soup.find_all("a", attrs={"class": "nameMusic"})
    classes_year_of_releases = soup.find_all("p",attrs={"class": "albumYear"})
    
    
    # Em cada for pegamos do trecho de código epenas os textos que nos interressa.
    
    for album_title in classes_album_titles:
        album_titles.append(album_title.text)
    
    for name_of_music in classes_name_of_musics:
        name_of_musics.append(name_of_music.text)            
    
    for year_of_release in classes_year_of_releases:
        year_of_releases.append(year_of_release.text[0:4])
            
















