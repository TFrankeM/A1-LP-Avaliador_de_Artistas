import numpy as np
import pandas as pd

print('\n' + '\033[1;36m~\033[m' * 50)

print('\033[1;36m~\033[m' + ' '*2 + '\033[1;32m PERGUNTAS DE NEGÓCIO SOBRE A BANDA SKILLET \033[m' + ' '*2 + '\033[1;36m~\033[m')

print('\033[1;36m~\033[m' * 50)

                    ### GRUPO DE PERGUNTAS 1 ###
                    
## Músicas mais ouvidas e músicas menos ouvidas por Álbum ##
def musica_ouvida_album(dataframe):
    """
    musica_ouvida_album retorna as músicas mais ouvidas e as músicas menos ouvidas por álbum.
    :param dataframe: Dataframe de onde são retiradas as informações.
    :return: Retorna um dataframe com as músicas mais ouvidas por álbum e um dataframe com as
    músicas menor ouvidas por álbum.
    """ 
    
    # Frame do dataframe com as 3 músicas mais ouvidas de cada álbum.
        # .sort_values(['Álbuns','Reproduções'], ascending=False) => ordena 1º em relação a 'Álbuns' e depois a 'Reproduções' em ordem decrescente.
        # .groupby('Álbuns').head(3)                            => seleciona as 3 musicas mais ouvidas de cada álbum.   
    mais_ouvidas = dataframe.sort_values(['Álbuns','Reproduções'], ascending=False).groupby('Álbuns').head(3)
    
    # Frame do dataframe com as 3 músicas menos ouvidas de cada álbum.
        # .sort_values(['Álbuns','Reproduções'], ascending=False) => ordena 1º em relação a 'Álbuns' e depois a 'Reproduções' em ordem decrescente
        # .groupby('Álbuns').tail(3)                            => seleciona as 3 musicas menos ouvidas de cada álbum.
    menos_ouvidas = dataframe.sort_values(['Álbuns','Reproduções'], ascending=False).groupby('Álbuns').tail(3)


    print('\033[1;32m \nAs músicas mais ouvida de cada álbum foram: \033[m \n', mais_ouvidas[['Álbuns','Músicas','Reproduções']], sep='')
    print('\033[1;32m \nAs músicas menos ouvida de cada álbum foram: \033[m \n', menos_ouvidas[['Álbuns','Músicas','Reproduções']], sep='')
    # print('\n\n', mais_ouvida)
    # print('\n\n', menos_ouvida)

    return mais_ouvidas, menos_ouvidas


## Músicas mais longas e músicas mais curtas por álbum ##
def musica_tamanho_album(dataframe):
    """
    musica_tamanho_album retorna as músicas mais longas e as músicas mais curtas por álbum.
    :param dataframe: Dataframe de onde são retiradas as informações.
    :return: Retorna um dataframe com as músicas mais longas por álbum e um dataframe com as
    músicas mais curtas por álbum.
    """ 
    # Frame do dataframe com as 3 músicas mais longas de cada álbum.
        # .sort_values(['Álbuns','Duração'], ascending=False) => ordena 1º em relação a 'Álbuns' e depois a 'Duração' em ordem decrescente.
        # .groupby('Álbuns').head(3)                            => seleciona as 3 musicas mais longas de cada álbum.
    mais_longas = dataframe.sort_values(['Álbuns','Duração'], ascending=False).groupby('Álbuns').head(3)        
                                                                                                       
    # Frame do dataframe com as 3 músicas mais curtas de cada álbum.
        # .sort_values(['Álbuns','Duração'], ascending=False) => ordena 1º em relação a 'Álbuns' e depois a 'Duração' em ordem decrescente.
        # .groupby('Álbuns').tail(3)                            => seleciona as 3 musicas mais curtas de cada álbum.
    mais_curtas = dataframe.sort_values(['Álbuns','Duração'], ascending=False).groupby('Álbuns').tail(3)
    
    print('\033[1;32m \nAs músicas mais longas de cada álbum são: \033[m \n', mais_longas[['Álbuns','Músicas','Duração']], sep='')
    print('\033[1;32m \nAs músicas mais curtas de cada álbum são: \033[m \n', mais_curtas[['Álbuns','Músicas','Duração']], sep='')
    # print('\n\n',mais_longa)  
    # print('\n\n', mais_curta)
    
    return mais_longas, mais_curtas
    
    
## Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista] ##
def musica_ouvida_carreira(dataframe):
    """
    musica_ouvida_carreira retorna as músicas mais ouvidas e as músicas menos ouvidas na carreira da banda.
    :param dataframe: Dataframe de onde são retiradas as informações.
    :return: Retorna um dataframe com as músicas mais ouvidas na carreira e um dataframe com as
    músicas menos ouvidas na carreira.
    """ 
    # Frame do dataframe com as 3 músicas mais ouvidas na carreira da banda.
        # .sort_values(['Reproduções'], ascending=False) => ordena em relação a 'Reproduções' em ordem decrescente.
        # .head(3)                                     => seleciona as 3 musicas mais tocadas.
    mais_ouvidas_carreira = dataframe.sort_values(['Reproduções'], ascending=False).head(3)
    # Frame do dataframe com as 3 músicas menos ouvidas na carreira da banda.
        # .sort_values(['Reproduções'], ascending=False) => ordena em relação a 'Reproduções' em ordem decrescente.
        # .head(3)                                     => seleciona as 3 musicas menos tocadas.
    menos_ouvidas_carreira = dataframe.sort_values(['Reproduções'], ascending=False).tail(3)
    
    print(f'\033[1;32m \nAs músicas mais ouvidas entre todas as músicas da banda são: \033[m \n', mais_ouvidas_carreira[['Álbuns','Músicas','Reproduções']], sep='')
    print('\033[1;32m \nAs músicas menos ouvidas entre todas as músicas da banda são: \033[m \n', menos_ouvidas_carreira[['Álbuns','Músicas','Reproduções']], sep='')
    # print('\n\n',mais_ouvidas_carreira)
    # print('\n\n',menos_ouvidas_carreira)
    return mais_ouvidas_carreira, menos_ouvidas_carreira

    
## Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista] ##
def musica_tamanho_carreira(dataframe):
    """
    musica_ouvida_carreira retorna as músicas mais longas e as músicas mais curtas dentre todas as músicas da banda.
    :param dataframe: Dataframe de onde são retiradas as informações.
    :return: Retorna um dataframe com as músicas mais longas e um dataframe com as músicas mais curtas da banda.
    """ 
    # Frame do dataframe com as 3 músicas mais longas da banda.
        # .sort_values(['Duração'], ascending=False) => ordena em relação a 'Duração' em ordem decrescente.
        # .head(3)                                     => seleciona as 3 musicas mais longas.
    mais_longas_carreira = dataframe.sort_values(['Duração'], ascending=False).head(3)
    # Frame do dataframe com as 3 músicas mais curtas da banda.
        # .sort_values(['Duração'], ascending=False) => ordena em relação a 'Duração' em ordem decrescente.
        # .head(3)                                     => seleciona as 3 musicas mais curtas.
    mais_curtas_carreira = dataframe.sort_values(['Duração'], ascending=False).tail(3)
    
    print(f'\033[1;32m \nAs músicas mais longas entre todas as músicas da banda são: \033[m \n', mais_longas_carreira[['Álbuns','Músicas','Duração']], sep='')
    print('\033[1;32m \nAs músicas mais curtas entre todas as músicas da banda são: \033[m \n', mais_curtas_carreira[['Álbuns','Músicas','Duração']], sep='')
    # print(mais_curta_carreira)
    # print(mais_longa_carreira)
    return mais_longas_carreira, mais_curtas_carreira


## Álbuns mais premiados ##
def mais_premiado(dataframe):
    pass
    # return album_mais_premiado


## Relação entre a duração da música e sua popularidade ##
def musica_popularidade(dataframe):
    pass
    # return relacao


                ### GRUPO DE PERGUNTAS 2 ###
                
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
    # (freq_palavras_album)
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
    print(freq_palavras_musica)
    # freq_palavras_musica.to_excel("Palavras Titulos Músicas.xlsx")
    return freq_palavras_musica

    
## Palavras mais comuns nas letras das músicas, por álbum ##
def palavra_letra_album(dataframe):
    pass

    
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


########## CÓDIGO PRINCIPAL ##########
# Acionamento de todas as funções
pd.options.display.max_columns = 5
pd.options.display.float_format = "{:.2f}".format

# Dataframes que estão sendo usados
dataframe = pd.read_excel('dataframe_skillet.xlsx')
dataframe = pd.read_excel('Albuns 1 e 2.xlsx')

# print(dataframe)


musica_ouvida_album(dataframe)

print('\033[1;36m~\033[m' * 50)

musica_tamanho_album(dataframe)

print('\033[1;36m~\033[m' * 50)

musica_ouvida_carreira(dataframe)

print('\033[1;36m~\033[m' * 50)

musica_tamanho_carreira(dataframe)

print('\033[1;36m~\033[m' * 50)





# print('\033[1;36m~\033[m' * 50)

# palavra_titulo_album(dataframe)

# print('\033[1;36m~\033[m' * 50)

# palavra_titulo_musica(dataframe)

