import seaborn as sns
import pandas as pd
import perguntas as pg
import matplotlib.pyplot as plt

#dataframe = pd.read_excel('BD - Skillet.xlsx')


def grafico_musica_mais_popular_por_album(dataframe):
    mais_ouvidas, menos_ouvidas = pg.musica_ouvida_album(dataframe)
    p111 = sns.catplot(data=mais_ouvidas, x="Popularidade", y="Músicas",kind="bar",hue="Álbuns",height=8)
    p111.set_axis_labels("Popularidade","")
    plt.title("Músicas mais populares de cada álbum")
    return plt.savefig('imagens\Músicas mais populares de cada álbum.png')

def grafico_musica_menos_popular_por_album(dataframe):
    mais_ouvidas, menos_ouvidas = pg.musica_ouvida_album(dataframe)
    p112 = sns.catplot(data=menos_ouvidas, x="Popularidade", y="Músicas",kind="bar",hue="Álbuns",height=8)
    p112.set_axis_labels("Popularidade","")
    plt.title("Músicas menos populares de cada álbum")
    return plt.savefig('imagens\Músicas menos populares de cada álbum.png')

def grafico_musica_mais_longa_por_album(dataframe):
    mais_longas, mais_curtas = pg.musica_tamanho_album(dataframe)
    p121 = sns.catplot(data=mais_longas, x="Duração", y="Músicas",kind="bar",hue="Álbuns",height=8)
    p121.set_axis_labels("Duração","")
    plt.title("Músicas mais longas de cada álbum")
    return plt.savefig('imagens\Músicas mais longas de cada álbum.png')

def grafico_musica_mais_curta_por_album(dataframe):
    mais_longas, mais_curtas = pg.musica_tamanho_album(dataframe)
    p122 = sns.catplot(data=mais_curtas, x="Duração", y="Músicas",kind="bar",hue="Álbuns",height=8)
    p122.set_axis_labels("Duração","")
    plt.title("Músicas mais curtas de cada álbum")
    return plt.savefig('imagens\Músicas mais curtas de cada álbum.png')

def grafico_musica_mais_longa_carreira(dataframe):
    mais_longas_carreira, mais_curtas_carreira = pg.musica_tamanho_carreira(dataframe)
    p131 = sns.catplot(data=mais_longas_carreira, x="Duração", y="Músicas",kind="bar",height=8)
    p131.set_axis_labels("Duração","")
    plt.title("Músicas mais longas em toda a carreira")
    return plt.savefig('imagens\Músicas mais longas em toda a carreira.png')

def grafico_musica_mais_curta_carreira(dataframe):
    mais_longas_carreira, mais_curtas_carreira = pg.musica_tamanho_carreira(dataframe)
    p131 = sns.catplot(data=mais_curtas_carreira, x="Duração", y="Músicas",kind="bar",height=8)
    p131.set_axis_labels("Duração","")
    plt.title("Músicas mais curtas em toda a carreira")
    return plt.savefig('imagens\Músicas mais curtas em toda a carreira.png')

def grafico_musica_mais_ouvida_carreira(dataframe):
    mais_ouvidas_carreira, menos_ouvidas_carreira = pg.musica_ouvida_carreira(dataframe)
    p141 = sns.catplot(data=mais_ouvidas_carreira, x="Popularidade", y="Músicas",kind="bar",height=8)
    p141.set_axis_labels("Popularidade", "")
    plt.title("Músicas mais populares em toda a carreira")
    return plt.savefig('imagens\Músicas mais populares em toda a carreira.png')

def grafico_musica_mais_ouvida_carreira(dataframe):
    mais_ouvidas_carreira, menos_ouvidas_carreira = pg.musica_ouvida_carreira(dataframe)
    p142 = sns.catplot(data=menos_ouvidas_carreira, x="Popularidade", y="Músicas",kind="bar",height=8)
    p142.set_axis_labels("Popularidade", "")
    plt.title("Músicas menos populares em toda a carreira")
    return plt.savefig('imagens\Músicas menos populares em toda a carreira.png')