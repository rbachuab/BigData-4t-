import pandas as pd
# 2 ¿Cuales son las categorías más vistas y en las que más horas de directo se han realizado?


list_viewers=[] #llista per agrupar el viewer_count
list_ocurrencies=[] #llista per agrupar el nombre de directes d'un mateix joc

df= pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["game_name", "viewer_count"]) #importem chuncks i columnes

for chunk in df: #processem cada chunk
    dfviews = chunk.groupby("game_name")["viewer_count"].sum().reset_index() #agrupem les instàncies de cada joc amb la suma total dels viewers que han tingut
    dfocurrencies = chunk.groupby("game_name").size().reset_index(name='ocurrencies') #agrupem les instàncies de cada joc i associem el nombre total d'ocurrencies simultànies.

    list_viewers.append(dfviews) #afegim a la llista el resultat de processar el chunk
    list_ocurrencies.append(dfocurrencies) #afegim a la llista el resultat de processar el chunk

final_frame_viewers = pd.concat(list_viewers) #concatenem totes les llistes resultants
final_frame_ocurrencies = pd.concat(list_ocurrencies) #concatenem totes les llistes resultants

df_viewers_2 = final_frame_viewers.groupby("game_name")["viewer_count"].sum().reset_index() #eliminem duplicats de categoria i sumem els resultats totals
df_ocurrencies_2 = final_frame_ocurrencies.groupby("game_name")["ocurrencies"].sum().reset_index() #eliminem duplicats de categoria i sumem els resultats totals

final_frame_2 = df_viewers_2.merge(df_ocurrencies_2) #Fem merge dels dos df per obtenir-ne un que contingui el nom del joc, el nombre de viewers, i el nombre d'ocurrències.
final_frame_2.to_csv("2.csv") #exportem a csv