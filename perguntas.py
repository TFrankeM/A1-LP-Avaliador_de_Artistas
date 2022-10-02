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
        # .groupby('Álbuns').head(3)                              => seleciona as 3 musicas mais ouvidas de cada álbum.   
    mais_ouvidas = dataframe.sort_values(['Álbuns','Reproduções'], ascending=False).groupby('Álbuns').head(3)
    
    # Frame do dataframe com as 3 músicas menos ouvidas de cada álbum.
        # .sort_values(['Álbuns','Reproduções'], ascending=False) => ordena 1º em relação a 'Álbuns' e depois a 'Reproduções' em ordem decrescente
        # .groupby('Álbuns').tail(3)                              => seleciona as 3 musicas menos ouvidas de cada álbum.
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
        # .groupby('Álbuns').head(3)                          => seleciona as 3 musicas mais longas de cada álbum.
    mais_longas = dataframe.sort_values(['Álbuns','Duração'], ascending=False).groupby('Álbuns').head(3)        
                                                                                                       
    # Frame do dataframe com as 3 músicas mais curtas de cada álbum.
        # .sort_values(['Álbuns','Duração'], ascending=False) => ordena 1º em relação a 'Álbuns' e depois a 'Duração' em ordem decrescente.
        # .groupby('Álbuns').tail(3)                          => seleciona as 3 musicas mais curtas de cada álbum.
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
        # .head(3)                                       => seleciona as 3 musicas mais tocadas.
    mais_ouvidas_carreira = dataframe.sort_values(['Reproduções'], ascending=False).head(3)
    # Frame do dataframe com as 3 músicas menos ouvidas na carreira da banda.
        # .sort_values(['Reproduções'], ascending=False) => ordena em relação a 'Reproduções' em ordem decrescente.
        # .head(3)                                       => seleciona as 3 musicas menos tocadas.
    menos_ouvidas_carreira = dataframe.sort_values(['Reproduções'], ascending=False).tail(3)
    
    print('\033[1;32m \nAs músicas mais ouvidas entre todas as músicas da banda são: \033[m \n', mais_ouvidas_carreira[['Álbuns','Músicas','Reproduções']], sep='')
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
        # .head(3)                                   => seleciona as 3 musicas mais longas.
    mais_longas_carreira = dataframe.sort_values(['Duração'], ascending=False).head(5)
    # Frame do dataframe com as 3 músicas mais curtas da banda.
        # .sort_values(['Duração'], ascending=False) => ordena em relação a 'Duração' em ordem decrescente.
        # .head(3)                                   => seleciona as 3 musicas mais curtas.
    mais_curtas_carreira = dataframe.sort_values(['Duração'], ascending=False).tail(3)
    
    print('\033[1;32m \nAs músicas mais longas entre todas as músicas da banda são: \033[m \n', mais_longas_carreira[['Álbuns','Músicas','Duração']], sep='')
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
    """
    musica_popularidade retorna uma relação entre a duração da música e sua popularidade em relação ao número de reproduções.
    :param dataframe: Dataframe de onde são retiradas as informações.
    :return: Retorna um dataframe com intervalos de duração e a média das reprodução das músicas daquele intervalo.
    """
    # Criação de máscaras para intervalos de 1 minuto de duração.
    mask_0_a_2_minutos = dataframe['Duração'].between('0:00','2:00')
    mask_2_a_3_minutos = dataframe['Duração'].between('2:01','3:00')
    mask_3_a_4_minutos = dataframe['Duração'].between('3:01','4:00')
    mask_4_a_5_minutos = dataframe['Duração'].between('4:01','5:00')
    mask_5_a_6_minutos = dataframe['Duração'].between('5:01','6:00')
    mask_6_a_7_minutos = dataframe['Duração'].between('6:01','7:00')
    # Criação de um dataframe com os intervalos de duração e com as médias de reprodução das músicas com duração naquele intervalo.
    relacao = pd.DataFrame({'Intervalo de Duração': ['0 a 2 min', '2 a 3 min', '3 a 4 min', '4 a 5 min', '5 a 6 min', '6 a 7 min'],
                            'Média de Reproduções': [
                                                    dataframe.loc[mask_0_a_2_minutos, ['Reproduções']].mean()[0],
                                                    dataframe.loc[mask_2_a_3_minutos, ['Reproduções']].mean()[0],
                                                    dataframe.loc[mask_3_a_4_minutos, ['Reproduções']].mean()[0],
                                                    dataframe.loc[mask_4_a_5_minutos, ['Reproduções']].mean()[0],
                                                    dataframe.loc[mask_5_a_6_minutos, ['Reproduções']].mean()[0],
                                                    dataframe.loc[mask_6_a_7_minutos, ['Reproduções']].mean()[0],
                                                    ]})
    relacao = relacao.sort_values(['Média de Reproduções'], ascending=False)
    
    print('\033[1;32m \nComo é possível observar na tabela abaixo, as músicas com maior média de reproduções \033[m', end='')
    print(f'\033[1;32mtêm duração dentro do intervalo de {relacao["Intervalo de Duração"].max()}: \033[m')
    print(relacao)
    if relacao["Intervalo de Duração"].max() <= '3:00':
        print('\033[1;32m\nLogo, podemos concluir que músicas mais curtas são mais populares. \033[m')
    if '3;00' < relacao["Intervalo de Duração"].max() <= '4:00':
        print('\033[1;32m\nLogo, podemos concluir que músicas de duração média são mais populares. \033[m')
    else:
        print('\033[1;32m\nLogo, podemos concluir que músicas mais longas são mais populares. \033[m')
    return relacao


                ### GRUPO DE PERGUNTAS 2 ###
                
## Palavras mais comuns nos títulos dos Álbuns ##
def palavra_titulo_album(dataframe):
    """
    palavra_titulo_album encontra a frequência das palavras dos nomes dos álbuns.
    :param dataframe: Dataframe de onde são retiradas as informações.
    :return: Retorna uma string com todas as palavras que formam os nomes dos álbuns e um dataframe com as palavras e o número de ocorrências.
    """
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
    palavras_album = df_unicos["Únicos"].str.lower().str.split().explode().str.replace("[(){}[?!.:;,/-]","", regex=True)
    # Gerar um dataframe para deixar o print do console mais organizado e facilitar a geração de gráficos.
    freq_palavras_album = palavras_album.value_counts()
    freq_palavras_album = pd.DataFrame({'Palavras únicas': freq_palavras_album.index,'Ocorrências':freq_palavras_album.tolist()})
    
    # Retornar uma string para que seja feito a WordCloud
    palavras_titulo_album = []
    for palavras in palavras_album:
        palavras_titulo_album.append(palavras)
    palavras_titulo_album = ' '.join(palavras_titulo_album)
    
    print('\033[1;32m \nNão há uma palavra no título da música mais frequente do que outra, pois todas elas ocorrem apenas uma vez. Observe: \033[m \n', freq_palavras_album, sep='')
    return palavras_titulo_album, freq_palavras_album

    
## Palavras mais comuns nos títulos das músicas ##
def palavra_titulo_musica(dataframe):
    """
    palavra_titulo_album encontra a frequência das palavras dos nomes das músicas.
    :param dataframe: Dataframe de onde são retiradas as informações.
    :return: Retorna uma string com todas as palavras que formam os nomes das músicas e um dataframe com as palavras e o número de ocorrências.
    """
    # Dataframe com as frequências das palavras dos nomes dos álbuns
        # .str.lower()    => transforma todas as letras em minúsculas
        # .str.split()    => separa as palavras de uma mesma "célula"por vírgulas
        # .explode()      => separa cada palavra em uma linha
        # .str.replace()  => remove caracteres especiais
        # .value_counts() => conta a frequência de cada palavra
    palavras_musica = dataframe["Músicas"].str.lower().str.split().explode().str.replace("[(){}[?!.:;,/-]"," ", regex=True)
    freq_palavras_musica = palavras_musica.value_counts()
    # Gerar um dataframe para deixar o print do console mais organizado e facilitar a geração de gráficos.
    freq_palavras_musica = pd.DataFrame({'Palavras únicas': freq_palavras_musica.index,'Ocorrências':freq_palavras_musica.tolist()})
    
    # Retornar uma string para que seja feito a WordCloud
    palavras_titulo_musica = []
    for palavra in palavras_musica:
        palavras_titulo_musica.append(palavra)
    palavras_titulo_musica = ' '.join(palavras_titulo_musica)
    
    print('\033[1;32m \nAs palavras mais frequentes nos nomes das músicas são: \033[m \n', freq_palavras_musica.head(5), sep='')
    return palavras_titulo_musica, freq_palavras_musica

    
## Palavras mais comuns nas letras das músicas, por álbum ##
def palavra_letra_album(dataframe):
    """
    palavra_titulo_album encontra a frequência das palavras das letras das músicas, por álbum.
    :param dataframe: Dataframe de onde são retiradas as informações.
    :return: Retorna um dicionário com uma string para cada álbum contendo todas as palavras dele e um dicionário com um dataframe contendo as suas palavras únicas e o número de ocorrências delas.
    """
    # Agrupamos a coluna de letras em relação aos álbuns e adicionamos a um dicionário.
    dicionario = dict(tuple(dataframe.groupby('Álbuns')['Letras']))
    # Dicionário com as strings das letras dos álbuns
    dic_palavras_por_album = {}
    # Dicionário com a frequência das palavras por álbum
    dic_freq_palav_por_album = {}
    for chave in dicionario:
        # As chaves são:
            # Alien Youth
            # Ardent Worship
            # Awake
            # Collide
            # Comatose
            # Dominion
            # Hey You, I Love Your Soul
            # Invincible
            # Rise
            # Skillet
            # Unleashed
        # Dataframe com as letras de todas as músicas de um álbum na forma de dataframe.
        album = pd.DataFrame({'Letras':dicionario[chave]})
        # As letras das músicas são separadas em uma palavra por linha em um comprido dataframe de uma coluna.
        palav_letras_por_album = album['Letras'].str.lower().str.split().explode().str.replace("[(){}[?!.:;,/-]","", regex=True)
        # São contadas as ocorrências de cada palavra do álbum.
        freq_palav_letras_por_album = palav_letras_por_album.value_counts()
        
        # Gerar um dataframe para deixar o print do console mais organizado e facilitar a geração de gráficos.
        frequencias_palavras_album = pd.DataFrame({'Palavras únicas': freq_palav_letras_por_album.index,'Ocorrências':freq_palav_letras_por_album.tolist()})
        
        # Adicionar o dataframe de cada um dos álbum a um dicionário cuja chave é o nome do álbum.
        dic_freq_palav_por_album[f'{chave}'] = frequencias_palavras_album

        # Retornar um dicionário com strings das letras de cada álbum, cada chave é o nome do respectivo álbum, para que seja feito a WordCloud.
        palavras_todas_as_letras = []
        for elemento in palav_letras_por_album:
            palavras_todas_as_letras.append(elemento)
        palavras_todas_as_letras = ' '.join(palavras_todas_as_letras)
        dic_palavras_por_album[chave] = palavras_todas_as_letras
        
    print('\033[1;32m \nAs palavras mais frequentes nas letras das músicas, por álbum, são: \033[m \n')
    for album in dic_freq_palav_por_album:
        print(f' \033[1;36m{ album }\033[m \n { dic_freq_palav_por_album[album].head(5) } \n')

    return dic_palavras_por_album, dic_freq_palav_por_album
    

## Palavras mais comuns nas letras das músicas, em toda a discografia ##
def palavra_letra_carreira(dataframe):
    """
    palavra_titulo_album encontra a frequência das palavras das letras das músicas em relação a toda a discografia.
    :param dataframe: Dataframe de onde são retiradas as informações.
    :return: Retorna uma string com todas as palavras que formam as letras das músicas e um dataframe com as palavras e o número de ocorrências.
    """
    # Dataframe com as frequências das palavras das letras de cada música de um álbum
        # .str.lower()    => transforma todas as letras em minúsculas
        # .str.split()    => separa as palavras de uma mesma "célula"por vírgulas
        # .explode()      => separa cada palavra em uma linha
        # .str.replace()  => remove caracteres especiais
        # .value_counts() => conta a frequência de cada palavra
    palav_letras_carreira = dataframe["Letras"].str.lower().str.split().explode().str.replace("[(){}[?!.:;,/-]","", regex=True)
    freq_palav_letra_carreira = palav_letras_carreira.value_counts()
    # Gerar um dataframe para deixar o print do console mais organizado e facilitar a geração de gráficos.
    freq_palav_letra_carreira = pd.DataFrame({'Palavras únicas': freq_palav_letra_carreira.index,'Ocorrências':freq_palav_letra_carreira.tolist()})
    
    # Retornar uma string para que seja feito a WordCloud
    palavras_letras = []
    for palavra in palav_letras_carreira:
        palavras_letras.append(palavra)
    palavras_letras = ' '.join(palavras_letras)
    
    print('\033[1;32m \nAs palavras mais frequentes nas letras das músicas são: \033[m \n', freq_palav_letra_carreira.head(10), sep='')
    return palavras_letras, freq_palav_letra_carreira


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
dataframe = pd.read_excel('Dataframe.xlsx')
#dataframe = pd.read_excel('Albuns 1 e 2.xlsx')

# print(dataframe)


# musica_ouvida_album(dataframe)

# print('\033[1;36m~\033[m' * 50)

# musica_tamanho_album(dataframe)

# print('\033[1;36m~\033[m' * 50)

# musica_ouvida_carreira(dataframe)

# print('\033[1;36m~\033[m' * 50)

# musica_tamanho_carreira(dataframe)

# print('\033[1;36m~\033[m' * 50)

# NOT READY => mais_premiado(dataframe)

# print('\033[1;36m~\033[m' * 50)

# musica_popularidade(dataframe)

# print('\033[1;36m~\033[m' * 50)

# palavra_titulo_album(dataframe)

# print('\033[1;36m~\033[m' * 50)

# palavra_titulo_musica(dataframe)

# print('\033[1;36m~\033[m' * 50)

palavra_letra_album(dataframe)

# print('\033[1;36m~\033[m' * 50)

# palavra_letra_carreira(dataframe)

# print('\033[1;36m~\033[m' * 50)

# NOT READY =>

# print('\033[1;36m~\033[m' * 50)

# NOT READY =>









