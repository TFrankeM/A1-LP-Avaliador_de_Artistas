import seaborn as sns
import pandas as pd
import perguntas as pg
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

dataframe = pd.read_excel('BD - Skillet.xlsx')
paleta = "ch:rot=-.75,hue=0.5,light=.75"
# a = pg.titulo_album_nas_letras(dataframe)
# print(a)
def grafico_album_popular(dataframe):
    p = pg.album_popular(dataframe)
    grafico = sns.catplot(data=p, x="Média popularidade", y="Álbuns",
                          kind="bar",height=8, palette=paleta)
    grafico.set_axis_labels("Popularidade","Álbuns")
    plt.title("Músicas mais longas em toda a carreira")
    plt.subplots_adjust(top=0.96)
    return plt.savefig("imagens\Grupo 3\Músicas mais longas em toda a carreira")
grafico_album_popular(dataframe)
plt.show()