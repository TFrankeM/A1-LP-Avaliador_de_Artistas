from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud
import sys, os
import numpy as np
import pandas as pd
import interface as it
import perguntas as pg


# Banco de dados visualizado
arquivo = 'BD - Skillet.xlsx'
# Recebe apenas o dataframe, sem acionar o módulo de perguntas.
dataframe = it.ler_banco_de_dados(arquivo, False)




# Acho que o(s) gráfico(s) de uma pergunta devem estar em uma função, assim, seriam 15 funções...

# exemplo bobo
def grafico1(dataframe):
    mais_ouvidas, menos_ouvidas = pg.musica_ouvida_album(dataframe)
    mais_ouvidas.plot(x='Álbuns', y='Popularidade')
    plt.show()


grafico1(dataframe)

def wordcloud1(dataframe):
    palavras_titulo, freq_palavras_musica = pg.palavra_letra_carreira(dataframe)

    stopwords = STOPWORDS

    wc = WordCloud(background_color="white", stopwords=stopwords, height=640, width=1280)
    wc.generate(palavras_titulo)

    # store to file
    wc.to_file("WordCloud1.png")
    plt.show()
wordcloud1(dataframe)
