
# Anàlisi Dataset Twitch mes de Febrer 2023

## Importació

```python
import pandas as pd
import time

inici = time.time() #situem un contador d'inici en iniciar el programa

df= pd.read_csv('direction.csv', sep='\t') #indiquem que el separador és un tabulador - "\t"



final = time.time() #situem un contador al final de l'execució

print(final-iniial) #permet saber el temps que hem estat executant

```


Aquest arxiu de 4GB no el podem obrir ni amb Excel ni amb l'ordinador per falta de RAM

## Mostres

Anem a extreure una mostra.

```python
import pandas as pd
import time

inici = time.time() #situem un contador d'inici en iniciar el programa

sample = df.sample(frac=0.1) #extreiem una mostra amb .sample() d'una fracció del 10% del dataset (0.1)

df= pd.read_csv('direction.csv', sep='\t') #indiquem que el separador és un tabulador - "\t

final = time.time() #situem un contador al final de l'execució

print(final-iniial) #permet saber el temps que hem estat executant

```

Aquest recurs no ens serveix perquè per calcular el 10% del dataset s'ha de processar el total del dataset. Així doncs, no ens estalviem el temps i els recursos de lectura.

Per tal de solucionar-ho hem d'atacar el problema a la lectura del dataset.

``` python
import pandas as pd
import time

inici = time.time() #situem un contador d'inici en iniciar el programa
df= pd.read_csv('direction.csv', sep='\t', nrows= 2) #indiquem que el separador és un tabulador - "\t | delimitem el nombre de files a llegir a 2.

for col in df.columns:
	print(col) #Imprimim les columnes que té el csv.

final = time.time() #situem un contador al final de l'execució

print(final-iniial) #permet saber el temps que hem estat executant

```
Amb aquesta mostra ens estalviem llegir més del compte i filtrar les columnes que farem servir quan tornem a carregar el dataset.

## Filtratge de columnes

```python
import pandas as pd
import time

inici = time.time() #situem un contador d'inici en iniciar el programa
df= pd.read_csv('direction.csv', 
				sep='\t', #indiquem que el separador és un tabulador - "\t
				nrows= 2, #delimitem el nombre de files a llegir a 2.
				usecols=["captured_at","streamer_name","viewer_count", "game_name", "stream_title"]) #indiquem les columnes que volem



for col in df.columns:
	print(col) #Imprimim les columnes que té el csv.

final = time.time() #situem un contador al final de l'execució

print(final-iniial) #permet saber el temps que hem estat executant

```

## Stream més vist

```python
import pandas as pd
import time

inici = time.time() #situem un contador d'inici en iniciar el programa
df= pd.read_csv('direction.csv', 
				sep='\t', #indiquem que el separador és un tabulador - "\t
				nrows= 2, #delimitem el nombre de files a llegir a 2.
				usecols=["captured_at","streamer_name","viewer_count", "game_name", "stream_title"]) #indiquem les columnes que volem


posicio = df["viewer_count"].idxmax() #.idmax ens torna la posicio amb el valor més alt de viewer_count dins del dataframe.

print(df["streamer_name"].iloc[posicio]) #imprimim el nom de lstreamer apuntant a la posicio que ocupa a la llista fent servir iloc, i passant la posicio de lstreaming amb més viewer count


for col in df.columns:
	print(col) #Imprimim les columnes que té el csv.

final = time.time() #situem un contador al final de l'execució

print(final-inicial) #permet saber el temps que hem estat executant

```

Granuralitat de les dades --> nivell de profunditat i detall de les dades.

```python
import pandas as pd
import time

inici = time.time() #situem un contador d'inici en iniciar el programa
df= pd.read_csv('direction.csv', 
				sep='\t', #indiquem que el separador és un tabulador - "\t
				nrows= 2, #delimitem el nombre de files a llegir a 2.
				usecols=["captured_at","streamer_name","viewer_count", "game_name", "stream_title"]) #indiquem les columnes que volem


posicio = df["viewer_count"].idxmax() #.idmax ens torna la posicio amb el valor més alt de viewer_count dins del dataframe.

print(df["streamer_name"].iloc[posicio]) #imprimim el nom de lstreamer apuntant a la posicio que ocupa a la llista fent servir iloc, i passant la posicio de lstreaming amb més viewer count


dades_kings_league = df[df["streamer_name"] == "kingsleague"] 

dades_kings_league.to_csv("kingsleague.csv", index=False)


for col in df.columns:
	print(col) #Imprimim les columnes que té el csv.

final = time.time() #situem un contador al final de l'execució

print(final-inicial) #permet saber el temps que hem estat executant

```


## Chunks

chunksize permet dividir el df en blocs  d'una llargada determinada per processar el total del dataframe per blocs, i no de cop.


```python
import pandas as pd
import time

inici = time.time() #situem un contador d'inici en iniciar el programa
df= pd.read_csv('direction.csv', 
				sep='\t', #indiquem que el separador és un tabulador - "\t
				usecols=["captured_at","streamer_name","viewer_count", "game_name", "stream_title"]) #indiquem les columnes que volem
				chunksize = 1000 #carregarà el dataset en blocs de 10000 files

llista_kings_league =[]

for chunk in df:  #iterem tots els chunks
	dades_kings_league = chunk[chunk<`"streamer_name"] == "kingslegue" #busquem els streams fets des del canal kingsleague
	llista_kings_league.append(dades_kings_league)

final_frame = pd.concat(llista_kings_league) 
dades_kings_league.to_csv("kingsleague.csv", index=False)

```
