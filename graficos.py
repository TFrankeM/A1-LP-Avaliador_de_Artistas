import seaborn as sns
import pandas as pd
import perguntas as pg
import matplotlib.pyplot as plt
import numpy as np


#Pegando o arquivo
dataframe = pd.read_excel('BD - Skillet.xlsx')

##### Grupo de perguntas 1 #####

#Existe alguma relação entre a duração da música e sua popularidade?

def grafico_musica_popularidade(dataframe):
    popularidade = pg.musica_popularidade(dataframe)
    grafico = sns.lineplot(data=popularidade, y="Média de Popularidade", x = "Intervalo de Duração")
    plt.title("Relação entre duração e popularidade")
    plt.subplots_adjust(top=0.96)
    return plt.savefig('imagens\Grupo 1\Relação entre duração e popularidade.png')
grafico_musica_popularidade(dataframe)

#definindo a paleta de cores
paleta = "ch:rot=-.75,hue=0.5,light=.75"

#Músicas mais ouvidas e músicas menos ouvidas por Álbum

def grafico_musica_popularidade_por_album(dataframe):
    dic_de_dataframes = pg.musica_ouvida_album(dataframe)
    for album in dic_de_dataframes:
        grafico = sns.catplot(data=dic_de_dataframes[album], x="Popularidade", y="Músicas",
                              kind="bar",height=8, palette=paleta)
        grafico.set_axis_labels("Popularidade","Músicas")
        plt.title(f"Popularidade das músicas do álbum {album}")
        plt.subplots_adjust(top=0.96)
        plt.savefig(f"imagens\Grupo 1\Popularidade das músicas por álbum\Popularidade das músicas do álbum {album}.png")
grafico_musica_popularidade_por_album(dataframe)

#Ajustando dataframe pra converter minutos em segundos:
for linha, duracao in enumerate(dataframe['Duração']):
    dataframe['Duração'][linha] = int(duracao[0:2]) * 60 + int(duracao[3:5])
#Músicas mais longas e músicas mais curtas por Álbum
def grafico_tamanho_por_album(dataframe):
    dic_de_dataframes = pg.musica_tamanho_album(dataframe)
    for album in dic_de_dataframes:
        grafico = sns.catplot(data=dic_de_dataframes[album], x="Duração", y="Músicas",
                              kind="bar",height=8, palette=paleta)
        grafico.set_axis_labels("Duração","Músicas")
        plt.title(f"Tamanho das músicas do álbum {album}")
        plt.subplots_adjust(top=0.96)
        plt.savefig(f"imagens\Grupo 1\Tamanho das músicas por álbum\Tamanho das músicas do álbum {album}.png")
grafico_tamanho_por_album(dataframe)


#Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista]
def grafico_musica_mais_longa_carreira(dataframe):
    mais_longas_carreira, mais_curtas_carreira = pg.musica_tamanho_carreira(dataframe)
    grafico = sns.catplot(data=mais_longas_carreira, x="Duração", y="Músicas",
                          kind="bar",height=8, palette=paleta)
    grafico.set_axis_labels("Duração","")
    plt.title("Músicas mais longas em toda a carreira")
    plt.subplots_adjust(top=0.96)
    return plt.savefig('imagens\Grupo 1\Músicas mais longas em toda a carreira.png')
grafico_musica_mais_longa_carreira(dataframe)
def grafico_musica_mais_curta_carreira(dataframe):
    mais_longas_carreira, mais_curtas_carreira = pg.musica_tamanho_carreira(dataframe)
    grafico = sns.catplot(data=mais_curtas_carreira, x="Duração", y="Músicas",
                          kind="bar",height=8, palette=paleta)
    grafico.set_axis_labels("Duração","")
    plt.title("Músicas mais curtas em toda a carreira")
    plt.subplots_adjust(top=0.96)
    return plt.savefig('imagens\Grupo 1\Músicas mais curtas em toda a carreira.png')

#Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista]
def grafico_musica_mais_ouvida_carreira(dataframe):
    mais_ouvidas_carreira, menos_ouvidas_carreira = pg.musica_ouvida_carreira(dataframe)
    grafico = sns.catplot(data=mais_ouvidas_carreira, x="Popularidade", y="Músicas",
                          kind="bar",height=8, palette=paleta)
    grafico.set_axis_labels("Popularidade", "")
    plt.title("Músicas mais populares em toda a carreira")
    plt.subplots_adjust(top=0.96)
    return plt.savefig('imagens\Grupo 1\Músicas mais populares em toda a carreira.png')

def grafico_musica_menos_ouvida_carreira(dataframe):
    mais_ouvidas_carreira, menos_ouvidas_carreira = pg.musica_ouvida_carreira(dataframe)
    grafico = sns.catplot(data=menos_ouvidas_carreira, x="Popularidade", y="Músicas",
                          kind="bar",height=8, palette=paleta)
    grafico.set_axis_labels("Popularidade", "")
    plt.title("Músicas menos populares em toda a carreira")
    plt.subplots_adjust(top=0.96)
    return plt.savefig('imagens\Grupo 1\Músicas menos populares em toda a carreira.png')


#Voltando o dataframe original para o resto das funções
dataframe = pd.read_excel('BD - Skillet.xlsx')
#Álbuns mais premiados
def mais_premiado(dataframe):
    premiacao = pg.mais_premiado(dataframe)
    grafico = sns.catplot(data=premiacao, x="Número de Prêmios", y="Álbuns",
                          kind="bar",height=8, palette=paleta)
    plt.title("Premiação dos álbuns")
    plt.subplots_adjust(top=0.96)
    return plt.savefig('imagens\Grupo 1\Premiação dos álbuns.png')
mais_premiado(dataframe)


##### Gráficos de perguntas 2 #####

from PIL import Image
from wordcloud import STOPWORDS, WordCloud, ImageColorGenerator
import interface as it


# Banco de dados visualizado
arquivo = 'BD - Skillet.xlsx'
# Recebe apenas o dataframe, sem acionar o módulo de perguntas.
dataframe = it.ler_banco_de_dados(arquivo, False)


# Wordcloud com os títulos dos álbuns.
def WcTitulosAlbuns(dataframe):
    """
    WcTitulosAlbuns funãoque cria o wordcloud com os títulos dos álbuns.
    :param dataframe: DataFrame que contém as palavras.
    :return: WordCloud com as palavras dos títulos dos álbuns.
    """
    palavras_titulo_album, freq_palavras_album = pg.palavra_titulo_album(dataframe)
    wctituloalbum = WordCloud(background_color="white")
    wctituloalbum.generate(palavras_titulo_album)
    wctituloalbum.to_file("imagens/Grupo 2/Wc_Titulo_dos_Albuns.jpg")


WcTitulosAlbuns(dataframe)


def WcTituloMusicas(dataframe):
    """
    WcTituloMusicas função que cria wordcloud dos títulos.
    :param dataframe: DataFrame que contém as palavras.
    :return: WordCloud com as palavras dos títulos das músicas.
    """
    try:
        palavras_titulo_musica, freq_palavras_musica = pg.palavra_titulo_musica(dataframe)

        # Máscara que vai mudar o formato da imagem
        titulomusicaetmask = np.array(Image.open("imagens/Grupo 2/skillet nome.jpg"))

        # Gerando a wordcloud
        wctitulo = WordCloud(background_color="white", mask=titulomusicaetmask, contour_width=3, contour_color="black")
        wctitulo.generate(palavras_titulo_musica)

        # Mudando as cores.
        cores = ImageColorGenerator(titulomusicaetmask)
        wctitulo.recolor(color_func=cores)
        wctitulo.to_file("imagens/Grupo 2/Wc_Titulos_das_Musicas.jpg")
    except FileNotFoundError:
        print("A máscara para a wordcloud não foi encontrada.")


WcTituloMusicas(dataframe)


def WcPorAlbum(dataframe):
    """
    WcPorAlbum faz a Wordcloud das letras por álbum.
    :param dataframe: DataFrame que contém as palavras.
    :return: WordCloud com as palavras das letras por álbum.
    """

    # Chamando a função e pegando o dicionário.
    dic_palavras_por_album, dic_freq_palav_por_album = pg.palavra_letra_album(dataframe)

    # Para cada álbum pegamos as plavras das músicas do mesmo e fazermos a wordcloud.
    for album in dic_palavras_por_album:
        wcletraalbum = WordCloud(background_color="white")
        wcletraalbum.generate(dic_palavras_por_album[album])
        wcletraalbum.to_file(f"imagens/Grupo 2/Wc_Letras_do_{album}.jpg")


WcPorAlbum(dataframe)


def WcLetraCarreira(dataframe):
    """
    WcLetraCarreira faz a Wordcloud das letras das músicas.
    :param dataframe: DataFrame que contém as palavras.
    :return: WordCloud com as palavras de todas as letras da banda, a imagem é no formato de uma frigideira em referência ao nome da banda.
    """
    try:
        # Chamndo a função, pegando a lista que será usada e adicionando a mascara.
        palavras_letras, freq_palav_letra_carreira = pg.palavra_letra_carreira(dataframe)
        letrascarreiramask = np.array(Image.open("imagens/Grupo 2/frigideira.jpg"))
        wcletracarreira = WordCloud(background_color="white", mask=letrascarreiramask)
        wcletracarreira.generate(palavras_letras)

        # Mudando as cores e salvando o wordcloud.
        cores = ImageColorGenerator(letrascarreiramask)
        wcletracarreira.recolor(color_func=cores)
        wcletracarreira.to_file("imagens/Grupo 2/Wc_Todas_as_Músicas.jpg")
    except FileNotFoundError:
        print("A máscara não para a wordcoud não foi encontrada.")


WcLetraCarreira(dataframe)

def recorrencia_titulo_album(dataframe):
    a = pg.titulo_album_nas_letras(dataframe)
    grafico = sns.catplot(data=a, x="Ocorrências nas músicas", y="Nome do álbum",
                          kind="bar", height=8, palette=paleta)
    grafico.set_axis_labels("Ocorrências na música", "Nome do álbum")
    plt.title("Recorrência do título do álbum na letra")
    plt.subplots_adjust(top=0.96)
recorrencia_titulo_album(dataframe)

def recorrencia_titulo_musica(dataframe):
    a, b = pg.titulo_musica_nas_letras(dataframe)
    grafico = sns.catplot(data=a, x="Ocorrências na música", y="Nome da música",
                          kind="bar", height=8, palette=paleta)
    grafico.set_axis_labels("Ocorrências na música", "Nome da música")
    plt.title("Recorrência do título da música na letra")
    plt.subplots_adjust(top=0.96)
recorrencia_titulo_musica(dataframe)


##### Gráficos de perguntas 3 #####

def grafico_album_popular(dataframe):
    p = pg.album_popular(dataframe)
    grafico = sns.catplot(data=p, x="Média popularidade", y="Álbuns",
                          kind="bar",height=8, palette=paleta)
    grafico.set_axis_labels("Popularidade","Álbuns")
    plt.title("Popularidade dos álbuns")
    plt.subplots_adjust(top=0.96)
    return plt.savefig("imagens\Grupo 3\Popularidade dos álbuns")
grafico_album_popular(dataframe)

def grafico_mudancas_ao_longo_tempo(dataframe):
    df = pg.mudancas_ao_longo_tempo(dataframe)
    figure, left_ax = plt.subplots()
    left_ax.plot(df['Ano'], df['Duração do álbum (seg)'], color='red')
    left_ax.set_ylabel('Duração do álbum (seg)', color='red')

    # Cria eixo Y na direita e plota dados nele
    right_ax = left_ax.twinx()
    right_ax.plot(df['Ano'], df['Popularidade média'], color='blue')
    right_ax.set_ylabel('Popularidade média', color='blue')
    plt.title("Mudanças nos álbuns ao longo do tempo")
    return plt.savefig("imagens\Grupo 3\Mudanças nos álbuns ao longo do tempo.png")
grafico_mudancas_ao_longo_tempo(dataframe)
