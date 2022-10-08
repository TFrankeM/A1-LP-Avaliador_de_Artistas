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
def grafico_musica_popularidade(dataframe):
    popularidade = pg.musica_popularidade(dataframe)
    grafico = sns.lineplot(data=popularidade, y="Média de Popularidade", x = "Intervalo de Duração",)
    plt.title("Relação entre duração e popularidade")
    plt.subplots_adjust(top=0.96)
    return plt.savefig('imagens\Grupo 1\Relação entre duração e popularidade.png')
grafico_musica_popularidade(dataframe)
plt.show()