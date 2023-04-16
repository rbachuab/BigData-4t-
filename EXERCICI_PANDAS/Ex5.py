import pandas as pd

#5.¿Cuál ha sido la evolución (captura a captura) de la desviación estándar en el volúmen de espectadores? ¿En qué momentos las audiencias se encuentran más polarizadas y en qué momentos la distribución es más uniforme?

df = pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["captured_at", "viewer_count"])#importem el csv dins d'un dataframe indicant el chunksize, el separador i les columnes que farem servir.
list=[] #creem el contenidor on guardarem el que processem dels chunks

for chunk in df: #iterem els chunks del dataframe
  df2 = chunk.groupby("captured_at")["viewer_count"].std().reset_index() #agrupem per captured_at i calculem la desviació estàndard dels espectadors amb el mètode .std()

pd.concat(list).groupby("captured_at")["viewer_count"].sum().to_csv("5.csv") #agrupem per captured_at per netejar la fragmentació de les dades i exportem a csv.
