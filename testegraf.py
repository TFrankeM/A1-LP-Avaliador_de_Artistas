import seaborn as sns
import pandas as pd
import perguntas as pg
from PIL import Image
from wordcloud import STOPWORDS, WordCloud, ImageColorGenerator
import interface as it
import numpy as np

dataframe = pd.read_excel('BD - Skillet.xlsx')
sentido_palavras = pd.read_excel('Positive and Negative Word List.xlsx')

# string_negativa, string_positiva, df_negativas, df_positivas = pg.positividade(dataframe,sentido_palavras)
# a,b,c,d=string_negativa, string_positiva, df_negativas, df_positivas
# print(a)
# print("############################################################")
# print(b)
# print("############################################################")
# print(c)
# print("############################################################")
# print(d)
# print("############################################################")

try:
    string_negativa, string_positiva, df_negativas, df_positivas = pg.positividade(dataframe, sentido_palavras)

    # Máscara que vai mudar o formato da imagem
    titulomusicaetmask = np.array(Image.open("imagens/Grupo 2/skillet nome.jpg"))

    # Gerando a wordcloud
    wctitulo = WordCloud(background_color="white", mask=titulomusicaetmask, contour_width=3, contour_color="black")
    wctitulo.generate(df_negativas)

    # Mudando as cores.
    cores = ImageColorGenerator(titulomusicaetmask)
    wctitulo.recolor(color_func=cores)
    wctitulo.to_file("imagens/Grupo 3/Wc_Titulos_das_Musicas.jpg")
except FileNotFoundError:
    print("A máscara para a wordcloud não foi encontrada.")