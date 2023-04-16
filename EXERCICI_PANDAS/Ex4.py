import pandas as pd

list_audiencia = [] #creem la llista on guardarem les dades dels espectadors
list_hores = [] #creem la llista on guardarem les hores d'stream

df = pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["streamer_name","game_name", "viewer_count"]) #importem el csv dins d'un dataframe indicant el chunksize, el separador i les columnes que farem servir.

for chunk in df: #iterem els chunks dins del dataframe
    df_audiencia = chunk.groupby('streamer_name')['viewer_count'].sum().reset_index() #agrupem els resultats amb el mateix streamer_name i ens quedem amb la suma d'espectadors que tenen.
    df_hores = chunk.groupby('streamer_name').size().transform(lambda x: x*0.25).reset_index(name='hores') #agrupem els resultats amb el mateix streamer name, calculem quants cops apareix, i dividim entre 4 per aconseguir aproximadament el nombre d'hores de directe que té. (cada captura es realitza aproximadament cada 15 mins. 15*4=60. Anomenem a la columna hores

    list_audiencia.append(df_audiencia) #afegim el resultat d'espectadors a la llista audiencia
    list_hores.append(df_hores) #afegim el resultat d'hores a la llista hores

df_audiencia_final = pd.concat(list_audiencia).groupby('streamer_name')['viewer_count'].sum().reset_index() #evitem la fragmentació de les dades derivada de processar per chunks, agrupant per streamer name i sumant els espectadors totals.
df_hores_final = pd.concat(list_hores).groupby('streamer_name')['hores'].sum().reset_index() #repetim el procés anterior, però ara tenint en compte el total de les hores
df_final = df_audiencia_final.merge(df_hores_final) #fem merge per unir els dos dataframes en una taula única

df_final.to_csv('4.csv') #exportem a csv