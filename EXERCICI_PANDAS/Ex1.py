import pandas as pd #importem la llibreria de pandas


# 1 ¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?

df = pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["captured_at", "viewer_count"]) #importem el csv dins d'un dataframe indicant el chunksize, el separador i les columnes que farem servir.
list=[] #creem una llista que servirà de contenidor per agrupar els chunks un cop processats.

for chunk in df: #iterem els chunks del dataframe
   df2 = chunk.groupby("captured_at")["viewer_count"].sum().reset_index() #per cada chunk agrupem per captured_at, i ens quedem amb la suma d'espectadors
   list.append(df2) #afegim a la llista el resultat

pd.concat(list).groupby("captured_at")["viewer_count"].sum().to_csv("1.csv")
#concatenem els resultats de cada chunk tornant a agrupar per captured_at
# per solventar qualsevol fragmentació de les dades, i sumant el valor dels
# espectadors per obtenir el dataframe final. Exportem a csv.

