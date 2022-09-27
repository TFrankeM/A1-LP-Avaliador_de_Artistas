import numpy as np
import pandas as pd


def musica_ouvida_album(dataframe):
    # Frame do dataframe com as 3 músicas mais ouvidas de cada álbum
    mais_ouvida = dataframe.sort_values(['Execuções'], ascending=False).groupby('Álbuns').head(3)     # Retorna as músicas na ordem      
    # Frame do dataframe com as 3 músicas menos ouvidas de cada álbum                                 # decrescente de execuções, com     
    menos_ouvida = dataframe.sort_values(['Execuções'], ascending=False).groupby('Álbuns').tail(3)    # os álbuns misturados  

    # print('\n\n', mais_ouvida)                                                        # Todos os dados do dataframe
    # print('\n\n', menos_ouvida)
    # print('\n\nMúsica mais ouvida: \n', mais_ouvida['Musicas'])               # Multi-Index e nome da música
    # print('\n\nMúsica mais ouvida: \n', mais_ouvida['Musicas'].iloc[0])       # Apenas nome da música
    # print('\n\nMúsica mais ouvida: \n', mais_ouvida['Musicas'].iloc[1])
    # print('\n\nMúsica menos ouvida: \n', menos_ouvida['Musicas'])
    # print('\n\n\n\n',mais_ouvida.loc[:,'Musicas'])
    return mais_ouvida, menos_ouvida
    

def musica_tamanho_album(dataframe):
    # Frame do dataframe com as 3 músicas mais longas de cada álbum    
    mais_longa = dataframe.sort_values(['Duração'], ascending=False).groupby('Álbuns').head(3)        # Retorna as músicas na ordem
    # print('\n\n',mais_longa)                                                                               # decrescente de tamanho, com   
    # Frame do dataframe com as 3 músicas mais curtas de cada álbum                                   # os álbuns misturados  
    mais_curta = dataframe.sort_values(['Duração'], ascending=False).groupby('Álbuns').tail(3)
    # print('\n\n', mais_curta)
    
    # mais_curta.plot(x="Duração", y="Execuções")           # Um exemplo de gráfico
    return mais_longa, mais_curta
    

def musica_ouvida_carreira(dataframe):
    mais_ouvida_carreira = dataframe.sort_values(['Execuções'], ascending=False).head(3)
    # print('\n\n',mais_ouvida_carreira)
    menos_ouvida_carreira = dataframe.sort_values(['Execuções'], ascending=False).head(3)
    # print('\n\n',menos_ouvida_carreira)
    return mais_ouvida_carreira, menos_ouvida_carreira


def palavra_titulo_album(dataframe):
    # Array com os nomes únicos dos álbuns
    array_unicos = np.unique(dataframe['Álbuns'].unique())
    # Dataframe com os nomes únicos dos álbuns
    df_unicos = pd.DataFrame({'Únicos': array_unicos.tolist()})
    # Dataframe com as frequências das palavras dos nomes dos álbuns
        # .str.lower()    => transforma todas as letras em minúsculas
        # .str.split()    => separa as palavras de uma mesma "célula"por vírgulas
        # .explode()      => separa cada palavra em uma linha
        # .str.replace()  => remove caracteres especiais
        # .value_counts() => conta a frequência de cada palavra
    freq_palavras_album = df_unicos["Únicos"].str.lower().str.split().explode().str.replace(" [!')’.(,/-`] ","").value_counts().head(3)
    # print(freq_palavras_album)
    return freq_palavras_album


def palavra_titulo_musica(dataframe):
    # Dataframe com as frequências das palavras dos nomes dos álbuns
        # .str.lower()    => transforma todas as letras em minúsculas
        # .str.split()    => separa as palavras de uma mesma "célula"por vírgulas
        # .explode()      => separa cada palavra em uma linha
        # .str.replace()  => remove caracteres especiais
        # .value_counts() => conta a frequência de cada palavra
    freq_palavras_musica = dataframe["Músicas"].str.lower().str.split().explode().str.replace(" [!')’.(,/-`] ","").value_counts().head(3)
    # print(freq_palavras_musica)
    return freq_palavras_musica


def palavra_letra_album(dataframe):
    pass


def palavra_letra_discografia(dataframe):
    pass




########## FUNÇÃO PRINCIPAL ##########
    
# Provisoriamente, a função principal está sendo acionada do módulo de funções,
# mas futuramente, ele deve ser transferido para um arquivo main


pd.options.display.max_columns = 5
pd.options.display.float_format = "{:.2f}".format


dataframe = pd.read_csv('Albuns-1-e-2.csv')
print(dataframe)


    #### COLOCAR MULTI-INDEX COM NOME DO ÁLBUM E NOME DAS MÚSICAS
# albuns = ["Skillet", "Skillet", "Skillet", "Skillet", "Skillet", 
#           "Skillet", "Skillet", "Skillet", "Skillet", "Skillet", 
#           "Hey you, I love your soul", "Hey you, I love your soul", "Hey you, I love your soul", 
#           "Hey you, I love your soul", "Hey you, I love your soul", "Hey you, I love your soul", 
#           "Hey you, I love your soul", "Hey you, I love your soul", "Hey you, I love your soul", 
#           "Hey you, I love your soul", "Hey you, I love your soul", "Hey you, I love your soul", 
#           "Hey you, I love your soul", "Hey you, I love your soul"]
# indices = pd.MultiIndex.from_arrays([albuns, dataframe["Musicas"]], names=("Álbuns", "Músicas"))

#dataframe = dataframe.drop(columns=("Musicas"))

# dataframe.set_index(indices, inplace=True)

#print(dataframe)



def principal(dataframe):
    # mais_ouvida_album, menos_ouvida_album = musica_ouvida_album(dataframe)

    # mais_longa, mais_curta = musica_tamanho_album(dataframe)
    
    # mais_ouvida_carreira, menos_ouvida_carreira = musica_ouvida_carreira(dataframe)

    # palavra_titulo_album = palavra_titulo_album(dataframe)
    
    # palavra_titulo_musica = palavra_titulo_musica(dataframe)

principal(dataframe)
    

          