import seaborn as sns
import pandas as pd
import perguntas as pg
import matplotlib.pyplot as plt

dataframe = pd.read_excel('BD - Skillet.xlsx')
for linha, duracao in enumerate(dataframe['Duração']):
    dataframe['Duração'][linha] = int(duracao[0:2])*60 + int(duracao[3:5])
mais_ouvidas, menos_ouvidas = pg.musica_ouvida_album(dataframe)
mais_longas, mais_curtas = pg.musica_tamanho_album(dataframe)
mais_ouvidas_carreira, menos_ouvidas_carreira = pg.musica_ouvida_carreira(dataframe)
mais_longas_carreira, mais_curtas_carreira = pg.musica_tamanho_carreira(dataframe)

#sns.set_theme(style="darkgrid")

p111 = sns.catplot(data=mais_ouvidas, x="Popularidade", y="Músicas",kind="bar",hue="Álbuns",height=8)
p111.set_axis_labels("Popularidade","")
titulo = "Músicas mais populares de cada álbum"
plt.title(titulo)
plt.savefig('imagens\Músicas mais populares de cada álbum.png')

p112 = sns.catplot(data=menos_ouvidas, x="Popularidade", y="Músicas",kind="bar",hue="Álbuns",height=8)
p112.set_axis_labels("Popularidade","")
plt.title("Músicas menos populares de cada álbum")
plt.savefig('imagens\Músicas menos populares de cada álbum.png')

p121 = sns.catplot(data=mais_longas, x="Duração", y="Músicas",kind="bar",hue="Álbuns",height=8)
p121.set_axis_labels("Duração","")
plt.title("Músicas mais longas de cada álbum")
plt.savefig('imagens\Músicas mais longas de cada álbum.png')

p122 = sns.catplot(data=mais_curtas, x="Duração", y="Músicas",kind="bar",hue="Álbuns",height=8)
p122.set_axis_labels("Duração","")
plt.title("Músicas mais curtas de cada álbum")
plt.savefig('imagens\Músicas mais curtas de cada álbum.png')

p131 = sns.catplot(data=mais_longas_carreira, x="Duração", y="Músicas",kind="bar",height=8)
p131.set_axis_labels("Duração","")
plt.title("Músicas mais longas em toda a carreira")
plt.savefig('imagens\Músicas mais longas em toda a carreira.png')
plt.show()