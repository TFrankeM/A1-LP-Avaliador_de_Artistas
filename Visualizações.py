import interface as it
import perguntas as pg


dataframe = it.ler_banco_de_dados()

# Acho que o(s) gráfico(s) de uma pergunta devem estar em uma função, assim, seriam 15 funções...

# exemplo bobo
def grafico1(dataframe):
    mais_ouvidas, menos_ouvidas = pg.musica_ouvida_album(dataframe)
    mais_ouvidas.plot(x='Álbuns', y='Popularidade')

grafico1(dataframe)


