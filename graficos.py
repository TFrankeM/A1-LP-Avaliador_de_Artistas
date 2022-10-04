import seaborn as sns
import pandas as pd
import perguntas as pg
import matplotlib.pyplot as plt

data1 = pd.read_excel('BD - Skillet.xlsx')
for linha, duracao in enumerate(data1['Duração']):
    data1['Duração'][linha] = int(duracao[0:2])*60 + int(duracao[3:5])
mais_ouvidas, menos_ouvidas = pg.musica_ouvida_album(data1)
mais_longas, mais_curtas = pg.musica_ouvida_carreira(data1)



sns.set_theme(style="darkgrid")

p111 = sns.catplot(data=mais_ouvidas, x="Popularidade", y="Músicas",kind="bar")
p111.set_axis_labels("Popularidade","")
plt.title("Músicas mais populares de cada álbum")

p112 = sns.catplot(data=menos_ouvidas, x="Popularidade", y="Músicas",kind="bar")
p112.set_axis_labels("Popularidade","")
plt.title("Músicas menos populares de cada álbum")

p121 = sns.catplot(data=mais_longas, x="Duração", y="Músicas",kind="bar", hue="Álbuns")
p121.set_axis_labels("Duração","")
plt.title("Músicas mais longas de cada álbum")

plt.show()
