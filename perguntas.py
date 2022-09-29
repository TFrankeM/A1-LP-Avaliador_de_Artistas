import numpy as np
import pandas as pd


## Músicas mais ouvidas e músicas menos ouvidas por Álbum ##
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
    

## Músicas mais longas e músicas mais curtas por Álbum ##
def musica_tamanho_album(dataframe):
    # Frame do dataframe com as 3 músicas mais longas de cada álbum    
    mais_longa = dataframe.sort_values(['Duração'], ascending=False).groupby('Álbuns').head(3)        # Retorna as músicas na ordem
    # print('\n\n',mais_longa)                                                                               # decrescente de tamanho, com   
    # Frame do dataframe com as 3 músicas mais curtas de cada álbum                                   # os álbuns misturados  
    mais_curta = dataframe.sort_values(['Duração'], ascending=False).groupby('Álbuns').tail(3)
    # print('\n\n', mais_curta)
    
    # mais_curta.plot(x="Duração", y="Execuções")           # Um exemplo de gráfico
    return mais_longa, mais_curta
    
    
## Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista] ##
def musica_ouvida_carreira(dataframe):
    mais_ouvida_carreira = dataframe.sort_values(['Execuções'], ascending=False).head(3)
    # print('\n\n',mais_ouvida_carreira)
    menos_ouvida_carreira = dataframe.sort_values(['Execuções'], ascending=False).tail(3)
    # print('\n\n',menos_ouvida_carreira)
    return mais_ouvida_carreira, menos_ouvida_carreira

    
## Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista] ##
def musica_tamanho_carreira(dataframe):
    mais_longa_carreira = dataframe.sort_values(['Duração'], ascending=False).head(3)
    mais_curta_carreira = dataframe.sort_values(['Duração'], ascending=False).tail(3)
    # print(mais_curta_carreira)
    # print(mais_longa_carreira)
    return mais_longa_carreira, mais_curta_carreira


## Álbuns mais premiados ##
def mais_premiado(dataframe):
    pass
    # return album_mais_premiado


## relação entre a duração da música e sua popularidade ##
def musica_popularidade(dataframe):
    pass
    # return relacao


## Palavras mais comuns nos títulos dos Álbuns ##
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
    freq_palavras_album = df_unicos["Únicos"].str.lower().str.split().explode().str.replace("[(){}[?!.:;,/-]","").value_counts()
    # print(freq_palavras_album)
    return freq_palavras_album

    
## Palavras mais comuns nos títulos das músicas ##
def palavra_titulo_musica(dataframe):
    # Dataframe com as frequências das palavras dos nomes dos álbuns
        # .str.lower()    => transforma todas as letras em minúsculas
        # .str.split()    => separa as palavras de uma mesma "célula"por vírgulas
        # .explode()      => separa cada palavra em uma linha
        # .str.replace()  => remove caracteres especiais
        # .value_counts() => conta a frequência de cada palavra
    freq_palavras_musica = dataframe["Músicas"].str.lower().str.split().explode().str.replace("[(){}[?!.:;,/-]","").value_counts()
    # print(freq_palavras_musica)
    # freq_palavras_musica.to_excel("Palavras Titulos Músicas.xlsx")
    return freq_palavras_musica

    
## Palavras mais comuns nas letras das músicas, por álbum ##
def palavra_letra_album(dataframe):
    #### ERRADA
    # Dataframe com as frequências das palavras das letras de cada música de um álbum
        # .str.lower()    => transforma todas as letras em minúsculas
        # .str.split()    => separa as palavras de uma mesma "célula"por vírgulas
        # .explode()      => separa cada palavra em uma linha
        # .str.replace()  => remove caracteres especiais
        # .value_counts() => conta a frequência de cada palavra
    freq_palav_letra_album = dataframe["Letras"].str.lower().str.split().explode().str.replace("[(){}[?!.:;,@/-]","").value_counts().head(3)
    
    # mais_longa = dataframe.sort_values(['Duração'], ascending=False).groupby('Álbuns').head(3)
    print(freq_palav_letra_album)
    return freq_palav_letra_album

    
## Palavras mais comuns nas letras das músicas, em toda a discografia ##
def palavra_letra_carreira(dataframe):
    # Dataframe com as frequências das palavras das letras de cada música de um álbum
        # .str.lower()    => transforma todas as letras em minúsculas
        # .str.split()    => separa as palavras de uma mesma "célula"por vírgulas
        # .explode()      => separa cada palavra em uma linha
        # .str.replace()  => remove caracteres especiais
        # .value_counts() => conta a frequência de cada palavra
    freq_palav_letra_carreira = dataframe["Letras"].str.lower().str.split().explode().str.replace("[(){}[?!.:;,/-]","").value_counts().head(3)
    # print(freq_palav_letra_carreira)
    return freq_palav_letra_carreira


## Recorrência do título de um álbum nas letras ##
def titulo_album_nas_letras(dataframe):
    pass
    # return
    
    
## Recorrência do título de uma música nas letras? ##
def titulo_musica_nas_letras(dataframe):
    pass
    # return


########## FUNÇÃO PRINCIPAL ##########
    
# Provisoriamente, a função principal está sendo acionada do módulo de funções,
# mas futuramente, ele deve ser transferido para um arquivo main


pd.options.display.max_columns = 5
pd.options.display.float_format = "{:.2f}".format


dataframe = pd.read_excel('dataframe_skillet.xlsx')
print(dataframe)



## Aciona as demais funções do módulo ##
def principal(dataframe):
    # mais_ouvida_album, menos_ouvida_album = musica_ouvida_album(dataframe)

    # mais_longa_album, mais_curta_album = musica_tamanho_album(dataframe)
    
    # mais_ouvida_carreira, menos_ouvida_carreira = musica_ouvida_carreira(dataframe)
    
    # mais_longa_carreira, mais_curta_carreira = musica_tamanho_carreira(dataframe)

    # NOT READY => album_mais_premiado = mais_premiado(dataframe)

    # NOT READY => relacao = musica_popularidade(dataframe)

    # palavras_titulo_album = palavra_titulo_album(dataframe)
    
    # palavras_titulo_musica = palavra_titulo_musica(dataframe)
    
    freq_palav_letra_album = palavra_letra_album(dataframe)
    
    # freq_palav_letra_carreira = palavra_letra_carreira(dataframe)
    
    # NOT READY => relacao_titulo_album_letra = titulo_album_nas_letras(dataframe)
    
    # NOT READY => relacao_titulo_musica_letra = titulo_musica_nas_letras(dataframe)
    
principal(dataframe)
    

          