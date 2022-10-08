import seaborn as sns
import pandas as pd
import perguntas1 as pg
import matplotlib.pyplot as plt

#dataframe = pd.read_excel('BD - Skillet.xlsx')

##### Grupo de perguntas 1 #####

#Músicas mais ouvidas e músicas menos ouvidas por Álbum
def grafico_musica_popularidade_por_album(dataframe):
    dic_de_dataframes = pg.musica_ouvida_album(dataframe)
    for album in dic_de_dataframes:
        grafico = sns.catplot(data=dic_de_dataframes[album], x="Popularidade", y="Músicas", kind="bar",height=8)
        grafico.set_axis_labels("Popularidade","Músicas")
        plt.title(f"Popularidade das músicas do álbum {album}")
        plt.subplots_adjust(top=0.96)
        plt.savefig(f"imagens\Popularidade das músicas por álbum\Popularidade das músicas do álbum {album}.png")

#Músicas mais longas e músicas mais curtas por Álbum
def grafico_tamanho_por_album(dataframe):
    dic_de_dataframes = pg.musica_tamanho_album(dataframe)
    for album in dic_de_dataframes:
        grafico = sns.catplot(data=dic_de_dataframes[album], x="Duração", y="Músicas", kind="bar",height=8)
        grafico.set_axis_labels("Duração","Músicas")
        plt.title(f"Tamanho das músicas do álbum {album}")
        plt.subplots_adjust(top=0.96)
        plt.savefig(f"imagens\Tamanho das músicas por álbum\Popularidade das músicas do álbum {album}.png")



#Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista]
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

#Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista]
def grafico_musica_mais_ouvida_carreira(dataframe):
    mais_ouvidas_carreira, menos_ouvidas_carreira = pg.musica_ouvida_carreira(dataframe)
    p141 = sns.catplot(data=mais_ouvidas_carreira, x="Popularidade", y="Músicas",kind="bar",height=8)
    p141.set_axis_labels("Popularidade", "")
    plt.title("Músicas mais populares em toda a carreira")
    return plt.savefig('imagens\Músicas mais populares em toda a carreira.png')

def grafico_musica_menos_ouvida_carreira(dataframe):
    mais_ouvidas_carreira, menos_ouvidas_carreira = pg.musica_ouvida_carreira(dataframe)
    p142 = sns.catplot(data=menos_ouvidas_carreira, x="Popularidade", y="Músicas",kind="bar",height=8)
    p142.set_axis_labels("Popularidade", "")
    plt.title("Músicas menos populares em toda a carreira")
    return plt.savefig('imagens\Músicas menos populares em toda a carreira.png')

#Álbuns mais premiados
def mais_premiado(dataframe):
    premiacao = pg.mais_premiado(dataframe)
    p15 = sns.catplot(data=premiacao, x="Número de Prêmios", y="Álbuns",kind="bar",height=8)
    plt.title("Premiação dos álbuns")
    return plt.savefig('imagens\Premiação dos álbuns.png')

#Existe alguma relação entre a duração da música e sua popularidade?
def grafico_musica_popularidade(dataframe):
    popularidade = pg.musica_popularidade(dataframe)
    p16 = sns.lineplot(data=popularidade, y="Média de Popularidade", x = "Intervalo de Duração")
    plt.title("Relação entre duração e popularidade")
    return plt.savefig('imagens\Relação entre duração e popularidade.png')

##### Gráficos de perguntas 2 #####