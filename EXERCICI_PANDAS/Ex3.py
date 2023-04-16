import pandas as pd
#3¿Como han evolucionado (captura a captura) estas categorias a lo largo del mes?


df= pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["captured_at", "viewer_count","game_name"]) #importem el csv dins d'un dataframe indicant el chunksize, el separador i les columnes que farem servir.
list = [] #processem cada chunk

for chunk in df: #iterem els chunks dins del dataframe
   list.append(chunk.groupby(["captured_at","game_name"])["viewer_count"].sum().reset_index()) #agrupem el chunk per captured_at i game_name, i ens quedem amb la suma d'espectadors. Ho afegim a la llista que conté els resultats de processar els chunks.

final_frame_1 = pd.concat(list).groupby(["captured_at","game_name"])["viewer_count"].sum().reset_index() #concatenem els chunks processats per resoldre la fragmentació de la informació en processar en chunks.
final_frame_1.to_csv("3.csv") #exportem a csv
