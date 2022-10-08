import seaborn as sns
import pandas as pd
import perguntas as pg
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_excel('BD - Skillet.xlsx')

##### Grupo de perguntas 1 #####

#Músicas mais ouvidas e músicas menos ouvidas por Álbum
def grafico_musica_popularidade_por_album(dataframe):
    dic_de_dataframes = pg.musica_ouvida_album(dataframe)
    for album in dic_de_dataframes:
        grafico = sns.catplot(data=dic_de_dataframes[album], x="Popularidade", y="Músicas",
                              kind="bar",height=8,palette="ch:rot=-.75,hue=0.5,light=.75")
        grafico.set_axis_labels("Popularidade","Músicas")
        plt.title(f"Popularidade das músicas do álbum {album}")
        plt.subplots_adjust(top=0.96)
grafico_musica_popularidade_por_album(dataframe)
plt.show()
