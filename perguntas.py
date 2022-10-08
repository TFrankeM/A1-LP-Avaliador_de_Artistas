import numpy as np
import pandas as pd


                    ### GRUPO DE PERGUNTAS 1 ###
                    
## Músicas mais ouvidas e músicas menos ouvidas com base na popularidade, por Álbum ##
def musica_ouvida_album(dataframe):
    """
    musica_ouvida_album retorna as músicas mais ouvidas e as músicas menos ouvidas com base na popularidade, por álbum.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return dic_de_dataframes: dicionário com um dataframe para cada álbum com suas músicas ordenadas por popularidade.
    """ 
    
    # .sort_values(['Álbuns','Popularidade'], ascending=False) => ordena 1º em relação a 'Álbuns' e depois a 'Popularidade' em ordem decrescente.
    dataframe = dataframe.sort_values(['Álbuns','Popularidade'], ascending=False)
    
    # Nome único dos álbuns
    albuns_unicos = dataframe['Álbuns'].unique()
    
    # Dicionário com os nomes dos álbuns
    dic_de_dataframes_pop = {elem : pd.DataFrame() for elem in albuns_unicos}
    
    # Adicionar ao dicionário o conteúdo: as músicas de cada álbum ordenadas pela popularidade
    for chave in dic_de_dataframes_pop.keys():
        dic_de_dataframes_pop[chave] = dataframe[:][dataframe['Álbuns'] == chave]

    return dic_de_dataframes_pop


## Músicas mais longas e músicas mais curtas por álbum ##
def musica_tamanho_album(dataframe):
    """
    musica_tamanho_album retorna as músicas mais longas e as músicas mais curtas por álbum.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return dic_de_dataframes_dur: dicionário com um dataframe para cada álbum com suas músicas ordenadas por duração.
    """ 
    # .sort_values(['Álbuns','Duração'], ascending=False) => ordena 1º em relação a 'Álbuns' e depois a 'Duração' em ordem decrescente.
    dataframe = dataframe.sort_values(['Álbuns','Duração'], ascending=False)
    
    # Nome único dos álbuns
    albuns_unicos = dataframe['Álbuns'].unique()
    
    # Dicionário com os nomes dos álbuns
    dic_de_dataframes_dur = {elem : pd.DataFrame() for elem in albuns_unicos}
    
    # Adicionar ao dicionário o conteúdo: as músicas de cada álbum ordenadas pela popularidade
    for chave in dic_de_dataframes_dur.keys():
        dic_de_dataframes_dur[chave] = dataframe[:][dataframe['Álbuns'] == chave]
    
    return dic_de_dataframes_dur
    
    
## Músicas mais ouvidas e músicas menos ouvidas com base na popularidade [em toda a história da banda ou artista] ##
def musica_ouvida_carreira(dataframe):
    """
    musica_ouvida_carreira retorna, com base na popularidade, as músicas mais ouvidas e as músicas menos
    ouvidas dentre todas as músicas da banda.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return mais_ouvidas_carreira: dataframe com as músicas mais ouvidas.
    :return menos_ouvidas_carreira: dataframe com as músicas menos ouvidas.
    """ 
    
    # Frame do dataframe com as 3 músicas mais ouvidas na carreira da banda.
        # .sort_values(['Reproduções'], ascending=False) => ordena em relação a 'Reproduções' em ordem decrescente.
        # .head(3)                                       => seleciona as 3 musicas mais tocadas.
    mais_ouvidas_carreira = dataframe.sort_values(['Popularidade'], ascending=False).head(10)
    # Frame do dataframe com as 3 músicas menos ouvidas na carreira da banda.
        # .sort_values(['Reproduções'], ascending=False) => ordena em relação a 'Reproduções' em ordem decrescente.
        # .head(3)                                       => seleciona as 3 musicas menos tocadas.
    menos_ouvidas_carreira = dataframe.sort_values(['Popularidade'], ascending=True).head(10)
    
    return mais_ouvidas_carreira, menos_ouvidas_carreira

    
## Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista] ##
def musica_tamanho_carreira(dataframe):
    """
    musica_tamanho_carreira retorna as músicas mais longas e as músicas mais curtas dentre todas as músicas da banda.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return mais_longas_carreira: dataframe com as músicas mais longas da banda.
    :return mais_curtas_carreira: dataframe com as músicas mais curtas da banda.
    """ 
    
    # Frame do dataframe com as 3 músicas mais longas da banda.
        # .sort_values(['Duração'], ascending=False) => ordena em relação a 'Duração' em ordem decrescente.
        # .head(3)                                   => seleciona as 3 musicas mais longas.
    mais_longas_carreira = dataframe.sort_values(['Duração'], ascending=False).head(10)
    # Frame do dataframe com as 3 músicas mais curtas da banda.
        # .sort_values(['Duração'], ascending=False) => ordena em relação a 'Duração' em ordem decrescente.
        # .head(3)                                   => seleciona as 3 musicas mais curtas.
    mais_curtas_carreira = dataframe.sort_values(['Duração'], ascending=True).head(10)
    
    return mais_longas_carreira, mais_curtas_carreira


## Álbuns mais premiados ##
def mais_premiado(dataframe):
    """
    mais_premiado encontra o álbum mais premiado da banda.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return df_premios: dataframe com o nome dos álbuns e o número de premiações de cada um deles.
    """
    
    # Lista com o número de prêmios por álbum.
    premios = dataframe.groupby('Álbuns')['Prêmios'].first()

    # Dataframe com o nome dos álbuns e o número de prêmios de cada um.
    df_premios = pd.DataFrame({'Álbuns': premios.index,
                                'Número de Prêmios': premios.tolist()}).sort_values('Número de Prêmios', ascending=False)
    
    return df_premios


## Relação entre a duração da música e sua popularidade ##
def musica_popularidade(dataframe):
    """
    musica_popularidade retorna uma relação entre a duração da música e sua popularidade.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return relacao: dataframe com intervalos de duração e a média das popularidades das músicas daquele intervalo.
    """
    
    # Criação de máscaras para intervalos de 1 minuto de duração.
    mask_0_a_2_minutos = dataframe['Duração'].between('00:00','02:00')
    mask_2_a_3_minutos = dataframe['Duração'].between('02:01','03:00')
    mask_3_a_4_minutos = dataframe['Duração'].between('03:01','04:00')
    mask_4_a_5_minutos = dataframe['Duração'].between('04:01','05:00')
    mask_5_a_6_minutos = dataframe['Duração'].between('05:01','06:00')
    mask_6_a_7_minutos = dataframe['Duração'].between('06:01','11:00')
    # Criação de um dataframe com os intervalos de duração e com as médias de reprodução das músicas com duração naquele intervalo.
    relacao = pd.DataFrame({'Intervalo de Duração': ['0:00 a 2:00 min', '2:01 a 3:00 min', '3:01 a 4:00 min', '4:01 a 5:00 min', '5:01 a 6:00 min', '6:01 a 7:00 min'],
                            'Média de Popularidade': [
                                                    dataframe.loc[mask_0_a_2_minutos, ['Popularidade']].mean()[0],
                                                    dataframe.loc[mask_2_a_3_minutos, ['Popularidade']].mean()[0],
                                                    dataframe.loc[mask_3_a_4_minutos, ['Popularidade']].mean()[0],
                                                    dataframe.loc[mask_4_a_5_minutos, ['Popularidade']].mean()[0],
                                                    dataframe.loc[mask_5_a_6_minutos, ['Popularidade']].mean()[0],
                                                    dataframe.loc[mask_6_a_7_minutos, ['Popularidade']].mean()[0],
                                                    ]})
    
    return relacao.fillna(0)


                ### GRUPO DE PERGUNTAS 2 ###
                
## Palavras mais comuns nos títulos dos Álbuns ##
def palavra_titulo_album(dataframe):
    """
    palavra_titulo_album encontra a frequência das palavras dos nomes dos álbuns.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return palavras_titulo_album: uma string com todas as palavras que formam os nomes dos álbuns.
    :return freq_palavras_album: um dataframe com as palavras e o número de ocorrências.
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
    
    return palavras_titulo_album, freq_palavras_album

    
## Palavras mais comuns nos títulos das músicas ##
def palavra_titulo_musica(dataframe):
    """
    palavra_titulo_musica encontra a frequência das palavras dos nomes das músicas.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return palavras_titulo_musica: uma string com todas as palavras que formam os nomes das músicas.
    :return freq_palavras_musica: um dataframe com as palavras e o número de ocorrências.
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
    
    return palavras_titulo_musica, freq_palavras_musica

    
## Palavras mais comuns nas letras das músicas, por álbum ##
def palavra_letra_album(dataframe):
    """
    palavra_letra_album encontra a frequência das palavras das letras das músicas, por álbum.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return dic_palavras_por_album: um dicionário com uma string para cada álbum contendo todas as palavras dele.
    :return dic_freq_palav_por_album: um dicionário com um dataframe para cada álbum contendo as suas palavras únicas e o número de ocorrências delas.
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

    return dic_palavras_por_album, dic_freq_palav_por_album
    

## Palavras mais comuns nas letras das músicas, em toda a discografia ##
def palavra_letra_carreira(dataframe):
    """
    palavra_letra_carreira encontra a frequência das palavras das letras das músicas em relação a toda a discografia.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return palavras_letras: uma string com todas as palavras que formam as letras das músicas.
    :return freq_palav_letra_carreira: um dataframe com as palavras e o número de ocorrências.
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
    
    return palavras_letras, freq_palav_letra_carreira


## Recorrência do título de um álbum como tema das letras ##
def titulo_album_nas_letras(dataframe):
    """
    titulo_album_nas_letras encontra a frequência dos títulos dos álbuns na letra das músicas.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return: dataframe com os nomes dos álbuns e o número de vezes que eles aparecem.
    """
    
    # Agrupamos a coluna de letras em relação aos álbuns e adicionamos a um dicionário.
    dicionario = dict(tuple(dataframe.groupby('Álbuns')['Letras']))
    # Dicionário com as strings das letras dos álbuns
    dic_palavras_album = {}
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
        # Dataframe com as letras de todas as músicas de um álbum.
        album = pd.DataFrame({'Letras':dicionario[chave]})
        # As letras das músicas são separadas em uma palavra por linha em um comprido dataframe de uma coluna.
        palav_letras_por_album = album['Letras'].str.lower().str.split().explode().str.replace("[(){}[?!.:;,/-]","", regex=True)
        
        # Retornar um dicionário com strings das letras de cada álbum, cada chave é o nome do respectivo álbum, para que seja feito a WordCloud.
        palavras_todas_as_letras = []
        for elemento in palav_letras_por_album:
            palavras_todas_as_letras.append(elemento)
        palavras_todas_as_letras = ' '.join(palavras_todas_as_letras)
        dic_palavras_album[chave.lower().replace(',','')] = palavras_todas_as_letras

    # Armazena temporariamente o número de ocorrências de cada título.
    freq_titulo_na_letra = []
    for album in dic_palavras_album:
        freq_titulo_na_letra.append(dic_palavras_album[album].count(album))
    # Dataframe com o nome dos álbum e quantas vezes esse nome aparece na letra das músicas desse álbum.
    df_palavras_album = pd.DataFrame({'Nome do álbum':dic_palavras_album.keys(), 'Ocorrências nas músicas': freq_titulo_na_letra})

    return df_palavras_album
    
## Recorrência do título de uma música como tema da letra ##
def titulo_musica_nas_letras(dataframe):
    """
    titulo_musica_nas_letras encontra a frequência dos títulos das músicas na letra da respectiva música.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return df_palavras_musica: um dataframe com os nomes das músicas e o número de vezes que elas aparecem na respectiva música.
    :return zero_ocorrencias: o número de músicas mencionadas 1 ou nenhuma vez.
    """
    
    # Agrupamos a coluna de letras em relação às músicas e adicionamos a um dicionário.
    dicionario = dict(tuple(dataframe.groupby('Músicas')['Letras']))
    # Dicionário com as strings das letras dos álbuns
    dic_palavras_musica = {}
    for chave in dicionario:
        # As chaves são os nomes das músicas
        # Dataframe com a letra da música
        album = pd.DataFrame({'Letras':dicionario[chave]})
        # A letra da música é separadas em uma palavra por linha em um comprido dataframe de uma coluna.
        palav_letras_por_musica = album['Letras'].str.lower().str.split().explode().str.replace("[(){}[?!.:;,/-]","", regex=True)
        
        # Retornar um dicionário com strings das letras de cada música, cada chave é o nome da respectivo música, para que seja feito a WordCloud.
        palavras_todas_as_letras = []
        for elemento in palav_letras_por_musica:
            palavras_todas_as_letras.append(elemento)
        palavras_todas_as_letras = ' '.join(palavras_todas_as_letras)
        dic_palavras_musica[chave.lower().replace(',','')] = palavras_todas_as_letras
    # Armazena temporariamente o número de ocorrências de cada título.
    freq_titulo_na_letra = []
    for album in dic_palavras_musica:
        freq_titulo_na_letra.append(dic_palavras_musica[album].count(album))
    # Dataframe com o nome dos álbum e quantas vezes esse nome aparece na letra das músicas desse álbum.
    df_palavras_musica = pd.DataFrame({'Nome da música':dic_palavras_musica.keys(), 'Ocorrências na música': freq_titulo_na_letra})
    # Visto que são muitas músicas, aplicamos uma máscara para que sejam apresentadas apenas as música com mais de 10 citações
    zero_ocorrencias = len(df_palavras_musica[ df_palavras_musica['Ocorrências na música'] <= 1 ])
    df_palavras_musica = df_palavras_musica[ df_palavras_musica['Ocorrências na música'] > 10 ]

    return df_palavras_musica, zero_ocorrencias


                ### GRUPO DE PERGUNTAS 3 - EXTRAS ###
                
## Álbum mais popular ##
def album_popular(dataframe):
    """
    album_popular analisa a popularidade dos álbuns para encontrar o mais popular.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return df_album_popularidade: dataframe com o nome, o número de faixas, a soma da popularidade das músicas e a popularidade média de cada álbum.
    """
    
    # Lista com os títulos dos álbuns.
    titulos = np.unique(dataframe['Álbuns'].unique()).tolist()

    # Lista com o número de faixas por álbum.
    faixas = dataframe.groupby('Álbuns')['Álbuns'].value_counts().tolist()

    # Lista com a soma da popularidade das músicas de cada álbum.
    pop_soma = dataframe.groupby("Álbuns")['Popularidade'].sum().tolist()

    # Dataframe com as informações da popularidade dos álbuns.
    df_album_popularidade = pd.DataFrame({'Álbuns': titulos,
                                          'Faixas': faixas,
                                          'Soma popularidade':pop_soma})
    # Adicionar coluna com a popularidade média de cada álbum.
    df_album_popularidade['Média popularidade'] = (df_album_popularidade['Soma popularidade'] / df_album_popularidade['Faixas'])
    #df_album_popularidade = df_album_popularidade.sort_values(['Média popularidade'], ascending=False)

    return df_album_popularidade


## Mudanças de aspectos dos álbuns ao longo do tempo ##
def mudancas_ao_longo_tempo(dataframe):
    """
    mudancas_ao_longo_tempo analisa como aspectos técnicos da discografia da banda mudaram ao longo do tempo.
    :param dataframe: dataframe de onde são retiradas as informações.
    :return df_album_popularidade: dataframe com o ano de lançamento, número de faixas, popularidade média e duração total do álbum.
    """
    
    # Lista com os anos de lançamentos dos álbuns.
    ano_lancamentos = dataframe.groupby('Álbuns')['Ano dos Lançamentos'].max().tolist()

    # Lista com o número de faixas por álbum.
    faixas = dataframe.groupby('Álbuns')['Álbuns'].value_counts().tolist()

    # Lista com a média da popularidade de cada álbum.
    pop_media = dataframe.groupby("Álbuns")['Popularidade'].mean().tolist()

    # Lista com a duração total de cada álbum.
        # Transformar a duração em minutos:
    for linha, duracao in enumerate(dataframe['Duração']):
        dataframe['Duração'][linha] = int(duracao[0:2])*60 + int(duracao[3:5])
    duracao_album = dataframe.groupby('Álbuns')['Duração'].sum().tolist()

    df_cronologico = pd.DataFrame({'Ano': ano_lancamentos,
                                    'Faixas': faixas,
                                    'Popularidade média': pop_media,
                                    'Duração do álbum (seg)': duracao_album}).sort_values('Ano')
    
    return df_cronologico


## Calcula a quantidade de palavras de sentido positivo e a quantidade de palavras de sentido negativo ##
def positividade(dataframe, sentido_palavras):
    """
    positividade analisa as palavras de todas as músicas classificando-as em positivas, negativas ou nenhuma das anteriores.
    :param dataframe: dataframe de onde são retiradas as informações.
    :param sentido_palavras: dataframe com as palavras classificadas de acordo com a sua conotação.
    :return string_negativa: string com as palavras negativas.
    :return string_positiva: string com as palavras positivas.
    :return df_negativas: dataframe com as palavras negativas e o número de vezes em que elas aparecem.
    :return df_positivas: dataframe com as palavras positivas e o número de vezes em que elas aparecem.
    """

    palavras_negativas = []
    palavras_positivas = []

    palavras_nas_letras = dataframe["Letras"].str.lower().str.split().explode().str.replace("[(){}[?!.:;,/-]","", regex=True)
    for palavra in palavras_nas_letras:
        for palav_neg in sentido_palavras['Negative Sense Word']:
            if palavra == palav_neg:
                palavras_negativas.append(palavra)
                
        for palav_pos in sentido_palavras['Positive Sense Word']:
            if palavra == palav_pos:
                palavras_positivas.append(palavra)
                
    # Strings.
        # Palavras negativas.
    string_negativa = ' '.join(palavras_negativas)
        # Palavras positivas.
    string_positiva = ' '.join(palavras_positivas)

    # Palavras únicas e suas frequências
    pal_neg, freq_neg = np.unique(palavras_negativas, return_counts=True)
    pal_pos, freq_pos = np.unique(palavras_positivas, return_counts=True)

    # Agrupar palavras únicas e suas frequências em dataframes.
    df_negativas = pd.DataFrame({'Palavras Negativas': pal_neg.tolist(),
                                          'Ocorrências Neg': freq_neg.tolist()}).sort_values('Ocorrências Neg', ascending=False)
    df_positivas = pd.DataFrame({'Palavras Positivas': pal_pos.tolist(),
                                          'Ocorrências Pos': freq_pos.tolist()}).sort_values('Ocorrências Pos', ascending=False)

    # Resetar o index.
    df_negativas = df_negativas.reset_index(drop=True)
    df_positivas = df_positivas.reset_index(drop=True)
        
    return string_negativa, string_positiva, df_negativas, df_positivas

