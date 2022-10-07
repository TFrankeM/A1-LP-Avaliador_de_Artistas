import seaborn as sns
import pandas as pd
import perguntas as pg
import matplotlib.pyplot as plt
import graficos as gf

dataframe = pd.read_excel('BD - Skillet.xlsx')
df = dataframe
#print(pg.mais_premiado(dataframe))
gf.grafico_musica_popularidade(df)
plt.show()