import seaborn as sns
import pandas as pd
import perguntas as pg
import matplotlib.pyplot as plt
import graficos as gf

dataframe = pd.read_excel('BD - Skillet.xlsx')
df = dataframe

def grafico_mudancas_ao_longo_tempo(dataframe):
    df = pg.mudancas_ao_longo_tempo(dataframe)
    figure, left_ax = plt.subplots()
    left_ax.plot(df['Ano'], df['Duração do álbum (seg)'], color='red')
    left_ax.set_ylabel('Duração do álbum (seg)', color='red')

    # Cria eixo Y na direita e plota dados nele
    right_ax = left_ax.twinx()
    right_ax.plot(df['Ano'], df['Popularidade média'], color='blue')
    right_ax.set_ylabel('Popularidade média', color='blue')
    plt.title("Mudanças nos álbuns ao longo do tempo")
    return plt.savefig("imagens\Mudanças nos álbuns ao longo do tempo.png")

grafico_mudancas_ao_longo_tempo(df)
# Mostra o gráfico
plt.show()
