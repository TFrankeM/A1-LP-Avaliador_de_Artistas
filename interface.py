import perguntas as pg
import pandas as pd
import warnings



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
        # Ignorar avisos no console.
        warnings.filterwarnings("ignore")
        # Define o número máximo de colunas exibidas no console. 
        pd.options.display.max_columns = 5
        # Define o número máximo de dicimais exibidos no console. 
        pd.options.display.float_format = "{:.2f}".format
        
        dataframe = pd.read_excel(arquivo)
        
        # Nomes obrigatórios para as colunas
        teste_de_titulo_coluna = dataframe[['Álbuns', 'Músicas', 'Ano dos Lançamentos', 'Duração', 'Popularidade', 'Prêmios', 'Letras']]

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
        for premio in dataframe['Prêmios']:
            if isinstance(premio, (int, float)) == False:
                raise TypeError(f'A entrada "{premio}" de "Prêmios" é do tipo str. Era esperado um int ou float.')
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
        print('Este módulo funciona apenas com nomes de colunas predefinidos. São eles: "Álbuns", "Músicas", "Ano dos Lançamentos", "Duração", "Popularidade", "Prêmios", "Letras" ')
    
    except TypeError as error:
        print(error)


def interface(dataframe):
    """
    interface aciona as funções do módulo perguntas e printa as respostas.
    :param dataframe: dataframe de onde são retiradas as informações.
    """ 
    
    # Inicio da vizualização no console
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    print('\033[1;36m~\033[m' + ' '*17 + '\033[1;32m PERGUNTAS DE NEGÓCIO SOBRE A BANDA SKILLET \033[m' + ' '*17 + '\033[1;36m~\033[m')
    
    print('\033[1;36m~\033[m' * 80)
    
    
        # Acionamento de todas as funções

                ### GRUPO DE PERGUNTAS 1 ###    
    
    
    ## Músicas mais ouvidas e músicas menos ouvidas com base na popularidade por Álbum ##
    dic_de_dataframes_pop = pg.musica_ouvida_album(dataframe)
    print('\033[1;36m \nMÚSICAS MAIS E MENOS OUVIDAS POR ÁLBUM\033[m')
    
    print('\033[1;32mCom base na popularidade, as músicas mais ouvida de cada álbum foram: ')
    for album in dic_de_dataframes_pop:
        print(f' \033[1;36m{ album }\033[m \n { dic_de_dataframes_pop[album][["Músicas","Popularidade"]].head(5).to_string(index=False) } \n')

    print('\033[1;32m \nCom base na popularidade, as músicas menos ouvida de cada álbum foram: ')
    for album in dic_de_dataframes_pop:
        print(f' \033[1;36m{ album }\033[m \n { dic_de_dataframes_pop[album][["Músicas","Popularidade"]].sort_values("Popularidade", ascending=True).head(5).to_string(index=False) } \n')
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Músicas mais longas e músicas mais curtas por álbum ##
    dic_de_dataframes_dur = pg.musica_tamanho_album(dataframe)
    print('\033[1;36m \nMÚSICAS MAIS LONGAS E MAIS CURTAS POR ÁLBUM \033[m')
    
    print('\033[1;32mAs músicas mais longas de cada álbum são: ')
    for album in dic_de_dataframes_dur:
        print(f' \033[1;36m{ album }\033[m \n { dic_de_dataframes_dur[album][["Músicas","Duração"]].head(5).to_string(index=False) } \n')

    print('\033[1;32m \nAs músicas mais curtas de cada álbum são: ')
    for album in dic_de_dataframes_dur:
        print(f' \033[1;36m{ album }\033[m \n { dic_de_dataframes_dur[album][["Músicas","Duração"]].sort_values("Duração", ascending=True).head(5).to_string(index=False) } \n')
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Músicas mais ouvidas e músicas menos ouvidas com base na popularidade [em toda a história da banda ou artista] ##
    mais_ouvidas_carreira, menos_ouvidas_carreira = pg.musica_ouvida_carreira(dataframe)
    print('\033[1;36m \nMÚSICAS MAIS E MENOS OUVIDAS \033[m')
    
    print('\033[1;32mAs músicas mais ouvidas, com base na popularidade, entre todas as músicas da banda são: \033[m \n\n', mais_ouvidas_carreira[['Álbuns','Músicas','Popularidade']].to_string(index=False), sep='')
    print('\033[1;32m \nAs músicas menos ouvidas, com base na popularidade, entre todas as músicas da banda são: \033[m \n\n', menos_ouvidas_carreira[['Álbuns','Músicas','Popularidade']].to_string(index=False), sep='')
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista] ##
    mais_longas_carreira, mais_curtas_carreira = pg.musica_tamanho_carreira(dataframe)
    print('\033[1;36m \nMÚSICAS MAIS LONGAS E MAIS CURTAS \033[m')
    
    print('\033[1;32mAs músicas mais longas entre todas as músicas da banda são: \033[m \n\n', mais_longas_carreira[['Álbuns','Músicas','Duração']].to_string(index=False), sep='')
    print('\033[1;32m \nAs músicas mais curtas entre todas as músicas da banda são: \033[m \n\n', mais_curtas_carreira[['Álbuns','Músicas','Duração']].to_string(index=False), sep='')
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Álbuns mais premiados ##
    df_premios = pg.mais_premiado(dataframe)
    print('\033[1;36m \nÁLBUNS MAIS PREMIADOS\033[m')
    
    print(f'\033[1;32mO álbum mais premiado da banda é {df_premios["Álbuns"].iloc[0]}. Observer o esquema completo: \033[m')
    print(df_premios.to_string(index=False))
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Relação entre a duração da música e sua popularidade ##
    relacao = pg.musica_popularidade(dataframe)
    relacao = relacao.sort_values(['Média de Popularidade'], ascending=False)
    print('\033[1;36m \nRELAÇÃO ENTRE DURAÇÃO E POPULARIDADE DA MÚSICA\033[m')
    
    print('\033[1;32mComo é possível observar na tabela abaixo, as músicas com maior popularidade \033[m', end='')
    print(f'\033[1;32mtêm duração dentro do intervalo de {relacao["Intervalo de Duração"].iloc[0]}: \033[m')
    print(relacao.to_string(index=False))
    
    print('\033[1;32m \nLogo, podemos concluir que as músicas de até 4 minutos são as mais populares. \033[m')
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    

                ### GRUPO DE PERGUNTAS 2 ###


    ## Palavras mais comuns nos títulos dos Álbuns ##
    palavras_titulo_album, freq_palavras_album = pg.palavra_titulo_album(dataframe)
    print('\033[1;36m \nPALAVRAS MAIS COMUNS NOS TÍTULOS DOS ÁLBUNS\033[m')
    
    print('\033[1;32mNão há uma palavra no título da música mais frequente do que outra, pois todas elas ocorrem apenas uma vez. Observe: \033[m \n', freq_palavras_album, sep='')
    
    print('\033[1;36m~\033[m' * 80)
    
    
    ## Palavras mais comuns nos títulos das músicas ##
    palavras_titulo_musica, freq_palavras_musica = pg.palavra_titulo_musica(dataframe)
    print('\033[1;36m \nPALAVRAS MAIS COMUNS NOS TÍTULOS DAS MÚSICAS\033[m')
    
    print('\033[1;32mAs palavras mais frequentes nos nomes das músicas são: \033[m \n', freq_palavras_musica.head(5), sep='')
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Palavras mais comuns nas letras das músicas, por álbum ##
    dic_palavras_por_album, dic_freq_palav_por_album = pg.palavra_letra_album(dataframe)
    print('\033[1;36m \nPALAVRAS MAIS COMUNS NAS LETRAS DAS MÚSICAS, POR ÁLBUM\033[m')
    
    print('\033[1;32mAs palavras mais frequentes nas letras das músicas, por álbum, são: \033[m \n')
    for album in dic_freq_palav_por_album:
        print(f' \033[1;36m{ album }\033[m \n { dic_freq_palav_por_album[album].head(5) } \n')

    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Palavras mais comuns nas letras das músicas, em toda a discografia ##
    palavras_letras, freq_palav_letra_carreira = pg.palavra_letra_carreira(dataframe)
    print('\033[1;36m \nPALAVRAS MAIS COMUNS NAS LETRAS DAS MÚSICAS\033[m')
    
    print('\033[1;32mAs palavras mais frequentes nas letras das músicas são: \033[m \n', freq_palav_letra_carreira.head(10), sep='')
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Recorrência do título de um álbum como tema das letras ##
    df_palavras_album = pg.titulo_album_nas_letras(dataframe)
    print('\033[1;36m \nRECORRÊNCIA DO TÍTULO DE UM ÁLBUM EM SUAS LETRAS\033[m')
    
    print('\033[1;32mPara avaliar se o título do álbum é tema recorrente das letras das músicas, levamos em conta o número de vezes em que ele aparece na letra.', end='')
    print('\033[1;32m Em vista disso, geramos o seguinte dataframe: \033[m \n', df_palavras_album, sep='')
    print('\033[1;32m\nLogo, os títulos "Dominion" e "Rise" são temas recorrrentes nas letras das suas músicas.\033[m')
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Recorrência do título de uma música como tema da letra ##
    df_palavras_musica, zero_ocorrencias = pg.titulo_musica_nas_letras(dataframe)
    print('\033[1;36m \nRECORRÊNCIA DO TÍTULO DE UMA MÚSICA EM SUA LETRA\033[m')
    
    print('\033[1;32mPara averiguar se o título da música é tema recorrente da letra, levamos em conta o número \033[m', end='')
    print(f'\033[1;32mde vezes que ele aparece na letra da música. Nesse sentido, {zero_ocorrencias} \033[m', end='')
    print('\033[1;32m nomes de músicas foram mencionados apenas 1 ou nenhum vez. Além disso, as 20 músicas cujos nomes mais apareceram na letra são: \n \033[m', df_palavras_musica.sort_values("Ocorrências na música", ascending = False).head(20).to_string(index=False), sep='')

    print('\n' + '\033[1;36m~\033[m' * 80)


                ### GRUPO DE PERGUNTAS 3 - EXTRAS ###


    ## Álbum mais popular ##
    album_popularidade = pg.album_popular(dataframe)
    print('\033[1;36m \nÁLBUM MAIS POPULAR\033[m')
    
    print('\033[1;32mPara termos uma ideia do álbum mais popular da banda, foram computadas a soma da popularidade das músicas \033[m', end='')
    print('\033[1;32mde cada álbum e a média da popularidade de cada um. Nesse sentido, identificamos que o álbum mais popular é\033[m', end='')
    print(f'\033[1;32m {album_popularidade["Álbuns"].iloc[0]}, visto que a média aponta para a maior popularidade. Observe o esquema completo: \033[m')
    print(album_popularidade.to_string(index=False))
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Mudanças de aspectos dos álbuns ao longo do tempo ##
    df_cronologico = pg.mudancas_ao_longo_tempo(dataframe)
    print('\033[1;36m \nMUDANÇAS NOS ÁLBUNS\033[m')
    
    print('\033[1;32mDetendo-nos agora sobre aspectos técnicos da discografia da banda. Vamos analisar como o número de \033[m', end='')
    print('\033[1;32mfaixas, a popularidade média e a duração dos álbuns mudaram ao longo da trajetória da banda: \033[m')
    print(df_cronologico.to_string(index=False))
    print('\033[1;32m \nNão é possível tirar conclusões significativas sobre a duração dos álbuns, mas é perceptível que a popularidade\033[m', end='')
    print('\033[1;32m da banda cresceu com o passar do tempo.\033[m')
    
    print('\n' + '\033[1;36m~\033[m' * 80)
    
    
    ## Calcula a quantidade de palavras de sentido positivo e a quantidade de palavras de sentido negativo ##
    print('\033[1;36m \nCONOTAÇÃO DAS PALAVRAS\033[m')
    try:
        # Ler banco de dados com a conotação das palavras.
        sentido_palavras = pd.read_excel('Positive and Negative Word List.xlsx')

        # Nomes obrigatórios para as colunas
        teste_de_titulo_coluna = sentido_palavras[['Positive Sense Word', 'Negative Sense Word']]
                    
        string_negativa, string_positiva, df_negativas, df_positivas = pg.positividade(dataframe, sentido_palavras)
        # Agrupar os dataframes das palavavras positivas e negativas.
        df_sentido = pd.concat([df_positivas.head(20), df_negativas.head(20)], axis=1)
        
        print('\n\033[1;32mFormada em 1996 em Memphis, Tennesse, Skillet é uma banda de rock alternativo cristão e, portanto, tem músicas \033[m', end='')
        print('\033[1;32mcarregadas com a temática religiosa. Nesse sentido, decidimos depositar nossa atenção sobre as letras de suas \033[m', end='')
        print('\033[1;32mmúsicas, a fim de encontrar um padrão em suas palavras. O método utilizado foi classificar as palavras de acordo \033[m', end='')
        print('\033[1;32mcom o seu sentido (em positivo/bom ou negativo/ruim) utilizando o banco de dados "Positive and Negative Word List" \033[m', end='')
        print(f'\033[1;32mcomo parâmetro. Foram encontradas {df_negativas["Ocorrências Neg"].sum()} palavras de conotação negativa e {df_positivas["Ocorrências Pos"].sum()} \033[m', end='')
        print('\033[1;32mpalavras de conotação positiva nas letras das músicas. As 20 palavras mais comuns desses dois grupos são as seguintes: \033[m')
        print(df_sentido)
        
    # Erro para se "Positive and Negative Word List.xlsx" não for encontrado.
    except FileNotFoundError:
        print('Esta função precisa do banco de dados "Positive and Negative Word List.xlsx" para funcionar.')
    # Erro para se não houver um nome obrigatório de coluna.
    except KeyError:
        print('Este módulo funciona apenas com nomes de colunas predefinidos. São eles: "Positive Sense Word", "Negative Sense Word".')
    
    except TypeError as error:
        print(error)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
