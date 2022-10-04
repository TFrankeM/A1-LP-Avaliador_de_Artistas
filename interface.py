import perguntas as pg
import pandas as pd


def ler_banco_de_dados(arquivo, chamar_interface):
    """
    ler_banco_de_dados lê o arquivo excel com o banco de dados da Banda Skillet e faz o
    tratamento de erro. Pode acionar a função interface().
    :param arquivo: Arquivo excel a ser lido e convertido em dataframe.
    :param chamar_interface: possui dois valores: False retorna o dataframe; True aciona
    a função interface().
    :return dataframe: Retorna um dataframe com informações da banda Skillet. 
    """ 
    
    try:
        # Define o número máximo de colunas exibidas no console. 
        pd.options.display.max_columns = 5
        # Define o número máximo de dicimais exibidos no console. 
        pd.options.display.float_format = "{:.2f}".format
        
        dataframe = pd.read_excel(arquivo)
        
        # Nomes obrigatórios para as colunas
        teste_de_titulo_coluna = dataframe[['Álbuns', 'Músicas', 'Ano dos Lançamentos', 'Duração', 'Popularidade', 'Letras']]

        # É levantado erro se a entrada de uma coluna não for de um tipo esperado.
        for album in dataframe['Álbuns']:
            if isinstance(album, (str)) == False:
                raise TypeError(f'A entrada "{album}" de "Álbuns" é do tipo int o float. Era esperada uma str.')
        for musica in dataframe['Músicas']:
            if isinstance(musica, (str)) == False:
                raise TypeError(f'A entrada "{musica}" de "Música" é do tipo int o float. Era esperada uma str.')
        for ano in dataframe['Ano dos Lançamentos']:
            if isinstance(ano, (int, float)) == False:
                raise TypeError(f'A entrada "{ano}" de "Ano dos Lançamentos" é do tipo string. Era esperado um int ou float.')
        for duracao in dataframe['Duração']:
            if isinstance(duracao, (str)) == False:
                raise TypeError(f'A entrada "{duracao}" de "Duração" é do tipo int ou float. Era esperada uma str.')
        for popularidade in dataframe['Popularidade']:
            if isinstance(popularidade, (int, float)) == False:
                raise TypeError(f'A entrada "{popularidade}" de "Popularidade" é do tipo string. Era esperado um int ou float.')
        for letra in dataframe['Letras']:
            if isinstance(letra, (str)) == False:
                raise TypeError(f'A entrada "{letra}" de "Letras" é do tipo int ou float. Era esperada uma str.')
        
        # Se a função for chamada a partir do módulo main, será chamada a interface.
        if chamar_interface == True:
            interface(dataframe)
        # Se a função for chamada a partir do módulo visualizações, será retornado o dataframe.
        if chamar_interface == False:
            return dataframe
        
    # Tratameto de erro para se o arquivo não for encontrado.
    except FileNotFoundError:
        print('O arquivo fornecido não foi encontrado.')
    # Tratameto de erro para se não houver um nome obrigatório de coluna.
    except KeyError:
        print('Este módulo funciona apenas com nomes de colunas predefinidos. São eles: "Álbuns", "Músicas", "Ano dos Lançamentos", "Duração", "Popularidade", "Letras" ')
    
    except TypeError as error:
        print(error)


def interface(dataframe):
    # Inicio da vizualização no console
    print('\n' + '\033[1;36m~\033[m' * 50)
    
    print('\033[1;36m~\033[m' + ' '*2 + '\033[1;32m PERGUNTAS DE NEGÓCIO SOBRE A BANDA SKILLET \033[m' + ' '*2 + '\033[1;36m~\033[m')
    
    print('\033[1;36m~\033[m' * 50)
    
    
            # Acionamento de todas as funções
    
    
    ## Músicas mais ouvidas e músicas menos ouvidas com base na popularidade por Álbum ##
    mais_ouvidas, menos_ouvidas = pg.musica_ouvida_album(dataframe)
    print('\033[1;32m \nCom base na popularidade, as músicas mais ouvida de cada álbum foram: \033[m \n', mais_ouvidas[['Álbuns','Músicas','Popularidade']], sep='')
    print('\033[1;32m \nCom base na popularidade, as músicas menos ouvida de cada álbum foram: \033[m \n', menos_ouvidas[['Álbuns','Músicas','Popularidade']], sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    ## Músicas mais longas e músicas mais curtas por álbum ##
    mais_longas, mais_curtas = pg.musica_tamanho_album(dataframe)
    print('\033[1;32m \nAs músicas mais longas de cada álbum são: \033[m \n', mais_longas[['Álbuns','Músicas','Duração']], sep='')
    print('\033[1;32m \nAs músicas mais curtas de cada álbum são: \033[m \n', mais_curtas[['Álbuns','Músicas','Duração']], sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    ## Músicas mais ouvidas e músicas menos ouvidas com base na popularidade [em toda a história da banda ou artista] ##
    mais_ouvidas_carreira, menos_ouvidas_carreira = pg.musica_ouvida_carreira(dataframe)
    print('\033[1;32m \nAs músicas mais ouvidas, com base na popularidade, entre todas as músicas da banda são: \033[m \n', mais_ouvidas_carreira[['Álbuns','Músicas','Popularidade']], sep='')
    print('\033[1;32m \nAs músicas menos ouvidas, com base na popularidade, entre todas as músicas da banda são: \033[m \n', menos_ouvidas_carreira[['Álbuns','Músicas','Popularidade']], sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    ## Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista] ##
    mais_longas_carreira, mais_curtas_carreira = pg.musica_tamanho_carreira(dataframe)
    print('\033[1;32m \nAs músicas mais longas entre todas as músicas da banda são: \033[m \n', mais_longas_carreira[['Álbuns','Músicas','Duração']], sep='')
    print('\033[1;32m \nAs músicas mais curtas entre todas as músicas da banda são: \033[m \n', mais_curtas_carreira[['Álbuns','Músicas','Duração']], sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    ## Álbuns mais premiados ##
    # NOT READY => pg.mais_premiado(dataframe)
    print('NOT READY')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    ## Relação entre a duração da música e sua popularidade ##
    relacao = pg.musica_popularidade(dataframe)
    print('\033[1;32m \nComo é possível observar na tabela abaixo, as músicas com maior popularidade \033[m', end='')
    print(f'\033[1;32mtêm duração dentro do intervalo de {relacao["Intervalo de Duração"].iloc[0]}: \033[m')
    print(relacao)
    
    print('Logo, podemos concluir que as músicas de até 4 minutos são as mais populares.')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    ## Palavras mais comuns nos títulos dos Álbuns ##
    palavras_titulo_album, freq_palavras_album = pg.palavra_titulo_album(dataframe)
    print('\033[1;32m \nNão há uma palavra no título da música mais frequente do que outra, pois todas elas ocorrem apenas uma vez. Observe: \033[m \n', freq_palavras_album, sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    ## Palavras mais comuns nos títulos das músicas ##
    palavras_titulo_musica, freq_palavras_musica = pg.palavra_titulo_musica(dataframe)
    print('\033[1;32m \nAs palavras mais frequentes nos nomes das músicas são: \033[m \n', freq_palavras_musica.head(5), sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    ## Palavras mais comuns nas letras das músicas, por álbum ##
    dic_palavras_por_album, dic_freq_palav_por_album = pg.palavra_letra_album(dataframe)
    print('\033[1;32m \nAs palavras mais frequentes nas letras das músicas, por álbum, são: \033[m \n')
    for album in dic_freq_palav_por_album:
        print(f' \033[1;36m{ album }\033[m \n { dic_freq_palav_por_album[album].head(5) } \n')

    print('\033[1;36m~\033[m' * 50)
    
    
    ## Palavras mais comuns nas letras das músicas, em toda a discografia ##
    palavras_letras, freq_palav_letra_carreira = pg.palavra_letra_carreira(dataframe)
    print('\033[1;32m \nAs palavras mais frequentes nas letras das músicas são: \033[m \n', freq_palav_letra_carreira.head(10), sep='')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    ## Recorrência do título de um álbum como tema das letras ##
    df_palavras_album = pg.titulo_album_nas_letras(dataframe)
    print('\033[1;32m \nPara avaliar se o título do álbum é tema recorrente das letras das músicas, levamos em conta o número de vezes em que ele aparece na letra.', end='')
    print('\033[1;32m Em vista disso, geramos o seguinte dataframe: \033[m \n', df_palavras_album, sep='')
    print('Logo, os títulos "Dominion" e "Rise" são temas recorrrentes nas letras das suas músicas.')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    ## Recorrência do título de uma música como tema da letra ##
    df_palavras_musica, zero_ocorrencias = pg.titulo_musica_nas_letras(dataframe)
    print('\033[1;32m \nPara averiguar se o título da música é tema recorrente da letra, levamos em conta o número \033[m', end='')
    print(f'\033[1;32mde vezes que ele aparece na letra da música. Nesse sentido, {zero_ocorrencias} \033[m', end='')
    print('\033[1;32m nomes de músicas foram mencionados apenas 1 ou nenhum vez. Além disso, as 20 músicas cujos nomes mais apareceram na letra são: \n \033[m', df_palavras_musica.sort_values("Ocorrências na música", ascending = False).head(20), sep='')

    print('\033[1;36m~\033[m' * 50)


    # NOT READY => pg.
    print('NOT READY')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    # NOT READY => pg.
    print('NOT READY')
    
    print('\033[1;36m~\033[m' * 50)
    
    
    # NOT READY => pg.(dataframe)
    print('NOT READY')
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
