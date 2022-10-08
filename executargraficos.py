import graficos as gf
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_excel('BD - Skillet.xlsx')
gf.grafico_musica_popularidade(dataframe)

for linha, duracao in enumerate(dataframe['Duração']):
    dataframe['Duração'][linha] = int(duracao[0:2]) * 60 + int(duracao[3:5])



df = dataframe
gf.grafico_musica_popularidade_por_album(df)
gf.grafico_tamanho_por_album(df)
gf.grafico_musica_mais_longa_carreira(df)
gf.grafico_musica_mais_curta_carreira(df)
gf.grafico_musica_mais_ouvida_carreira(df)
gf.grafico_musica_menos_ouvida_carreira(df)
gf.mais_premiado(df)
gf.grafico_album_popular(df)
print("Ok")