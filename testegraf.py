import seaborn as sns
import pandas as pd
import perguntas1 as pg
import matplotlib.pyplot as plt
import graficos as gf

dataframe = pd.read_excel('BD - Skillet.xlsx')
df = dataframe
# a, b = pg.palavra_titulo_album(dataframe)
# print(a)
# print("##########################")
# print(b)
def grafico_musica_popularidade_por_album(dataframe):
    dic_de_dataframes = pg.musica_ouvida_album(dataframe)
    for album in dic_de_dataframes:
        grafico = sns.catplot(data=dic_de_dataframes[album], x="Popularidade", y="Músicas", kind="bar",height=8)
        grafico.set_axis_labels("Popularidade","")
        plt.title(f"Popularidade das músicas do álbum {album}")
        plt.subplots_adjust(top=0.96)
        plt.savefig(f"imagens\Popularidade das músicas por álbum\Popularidade das músicas do álbum {album}.png")

grafico_musica_popularidade_por_album(df)
plt.show()


