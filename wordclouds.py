from PIL import Image
from wordcloud import STOPWORDS, WordCloud, ImageColorGenerator
import numpy as np
import interface as it
import perguntas as pg


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
    wctituloalbum.to_file("imagens/WordClouds/Wc_Titulo_dos_Albuns.jpg")


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
        titulomusicaetmask = np.array(Image.open("imagens/WordClouds/skillet nome.jpg"))

        # Gerando a wordcloud
        wctitulo = WordCloud(background_color="white", mask=titulomusicaetmask, contour_width=3, contour_color="black")
        wctitulo.generate(palavras_titulo_musica)

        # Mudando as cores.
        cores = ImageColorGenerator(titulomusicaetmask)
        wctitulo.recolor(color_func=cores)
        wctitulo.to_file("imagens/WordClouds/Wc_Titulos_das_Musicas.jpg")
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
        wcletraalbum.to_file(f"imagens/WordClouds/Wc_Letras_do_{album}.jpg")


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
        letrascarreiramask = np.array(Image.open("imagens/WordClouds/frigideira.jpg"))
        wcletracarreira = WordCloud(background_color="white", mask=letrascarreiramask)
        wcletracarreira.generate(palavras_letras)

        # Mudando as cores e salvando o wordcloud.
        cores = ImageColorGenerator(letrascarreiramask)
        wcletracarreira.recolor(color_func=cores)
        wcletracarreira.to_file("imagens/WordClouds/Wc_Todas_as_Músicas.jpg")
    except FileNotFoundError:
        print("A máscara não para a wordcoud não foi encontrada.")


WcLetraCarreira(dataframe)