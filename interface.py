import perguntas as pg
import pandas as pd

def ler_banco_de_dados():
    dataframe = pd.read_excel('BD - Skillet.xlsx')
    return dataframe

def interface():
    # Define o número máximo de colunas exibidas no console. 
    pd.options.display.max_columns = 5
    # Define o número máximo de dicimais exibidos no console. 
    pd.options.display.float_format = "{:.2f}".format
    
    # Dataframe com as músicas da banda Skillet
    dataframe = ler_banco_de_dados()
    
    # Inicio da vizualização no console
    print('\n' + '\033[1;36m~\033[m' * 50)
    
    print('\033[1;36m~\033[m' + ' '*2 + '\033[1;32m PERGUNTAS DE NEGÓCIO SOBRE A BANDA SKILLET \033[m' + ' '*2 + '\033[1;36m~\033[m')
    
    print('\033[1;36m~\033[m' * 50)
    
    # Acionamento de todas as funções
    
    mais_ouvidas, menos_ouvidas = pg.musica_ouvida_album(dataframe)
    
    print('\033[1;32m \nAs músicas mais ouvida de cada álbum foram: \033[m \n', mais_ouvidas[['Álbuns','Músicas','Reproduções']], sep='')
    print('\033[1;32m \nAs músicas menos ouvida de cada álbum foram: \033[m \n', menos_ouvidas[['Álbuns','Músicas','Reproduções']], sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    mais_longas, mais_curtas = pg.musica_tamanho_album(dataframe)
    print('\033[1;32m \nAs músicas mais longas de cada álbum são: \033[m \n', mais_longas[['Álbuns','Músicas','Duração']], sep='')
    print('\033[1;32m \nAs músicas mais curtas de cada álbum são: \033[m \n', mais_curtas[['Álbuns','Músicas','Duração']], sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    mais_ouvidas_carreira, menos_ouvidas_carreira = pg.musica_ouvida_carreira(dataframe)
    print('\033[1;32m \nAs músicas mais ouvidas entre todas as músicas da banda são: \033[m \n', mais_ouvidas_carreira[['Álbuns','Músicas','Reproduções']], sep='')
    print('\033[1;32m \nAs músicas menos ouvidas entre todas as músicas da banda são: \033[m \n', menos_ouvidas_carreira[['Álbuns','Músicas','Reproduções']], sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    mais_longas_carreira, mais_curtas_carreira = pg.musica_tamanho_carreira(dataframe)
    print('\033[1;32m \nAs músicas mais longas entre todas as músicas da banda são: \033[m \n', mais_longas_carreira[['Álbuns','Músicas','Duração']], sep='')
    print('\033[1;32m \nAs músicas mais curtas entre todas as músicas da banda são: \033[m \n', mais_curtas_carreira[['Álbuns','Músicas','Duração']], sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    # NOT READY => pg.mais_premiado(dataframe)
    print('NOT READY')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    relacao = pg.musica_popularidade(dataframe)
    print('\033[1;32m \nComo é possível observar na tabela abaixo, as músicas com maior média de reproduções \033[m', end='')
    print(f'\033[1;32mtêm duração dentro do intervalo de {relacao["Intervalo de Duração"].max()}: \033[m')
    print(relacao)
    if relacao["Intervalo de Duração"].max() <= '3:00':
        print('\033[1;32m\nLogo, podemos concluir que músicas mais curtas são mais populares. \033[m')
    if '3;00' < relacao["Intervalo de Duração"].max() <= '4:00':
        print('\033[1;32m\nLogo, podemos concluir que músicas de duração média são mais populares. \033[m')
    else:
        print('\033[1;32m\nLogo, podemos concluir que músicas mais longas são mais populares. \033[m')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    palavras_titulo_album, freq_palavras_album = pg.palavra_titulo_album(dataframe)
    print('\033[1;32m \nNão há uma palavra no título da música mais frequente do que outra, pois todas elas ocorrem apenas uma vez. Observe: \033[m \n', freq_palavras_album, sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    palavras_titulo_musica, freq_palavras_musica = pg.palavra_titulo_musica(dataframe)
    print('\033[1;32m \nAs palavras mais frequentes nos nomes das músicas são: \033[m \n', freq_palavras_musica.head(5), sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    dic_palavras_por_album, dic_freq_palav_por_album = pg.palavra_letra_album(dataframe)
    print('\033[1;32m \nAs palavras mais frequentes nas letras das músicas, por álbum, são: \033[m \n')
    for album in dic_freq_palav_por_album:
        print(f' \033[1;36m{ album }\033[m \n { dic_freq_palav_por_album[album].head(5) } \n')

    print('\033[1;36m~\033[m' * 50)
    
    
    palavras_letras, freq_palav_letra_carreira = pg.palavra_letra_carreira(dataframe)
    print('\033[1;32m \nAs palavras mais frequentes nas letras das músicas são: \033[m \n', freq_palav_letra_carreira.head(10), sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    df_palavras_album = pg.titulo_album_nas_letras(dataframe)
    print('\033[1;32m \nPara avaliar se o título do álbum é tema recorrente das letras das músicas, levamos em conta o número de vezes em que ele aparece na letra.', end='')
    print('\033[1;32m Em vista disso, geramos o seguinte dataframe: \033[m \n', df_palavras_album, sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    df_palavras_musica, zero_ocorrencias = pg.titulo_musica_nas_letras(dataframe)
    print('\033[1;32m \nPara averiguar se o título da música é tema recorrente da letra, levamos em conta o número \033[m', end='')
    print(f'\033[1;32mde vezes que ele aparece na letra da música. Nesse sentido, {zero_ocorrencias} \033[m', end='')
    print('\033[1;32m nomes de músicas foram mencionados apenas 1 ou nenhum vez. Além disso, as 20 músicas cujos nomes mais apareceram na letra são: \n \033[m', df_palavras_musica.sort_values("Ocorrências na música", ascending = False).head(20), sep='')

