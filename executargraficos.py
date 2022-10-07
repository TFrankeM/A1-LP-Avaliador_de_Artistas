import graficos as gf
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_excel('BD - Skillet.xlsx')
for linha, duracao in enumerate(dataframe['Duração']):
    dataframe['Duração'][linha] = int(duracao[0:2]) * 60 + int(duracao[3:5])
df = dataframe
gf.grafico_musica_mais_popular_por_album(df)
gf.grafico_musica_mais_curta_carreira(df)
gf.grafico_musica_mais_curta_por_album(df)
gf.grafico_musica_mais_longa_carreira(df)
gf.grafico_musica_mais_longa_por_album(df)
gf.grafico_musica_menos_popular_por_album(df)
plt.show()