import seaborn as sns
import pandas as pd
import perguntas as pg
import matplotlib.pyplot as plt

data1 = pd.read_excel('BD - Skillet.xlsx')
mais_ouvidas, menos_ouvidas = pg.musica_ouvida_album(data1)
#mais_ouvidas = mais_ouvidas.head(3)

sns.set_theme(style="darkgrid")

g = sns.catplot(data=mais_ouvidas, x="Popularidade", y="Músicas",kind="bar")
g.despine(left=True)
g.set_axis_labels("Popularidade","")
g.set_titles("{col_name} {col_var}")
plt.title("Músicas mais populares de cada álbum")
plt.show()
