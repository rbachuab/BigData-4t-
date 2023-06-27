# API Spotify

####Llibreria --> spotipy.readthedocs.io

## Instal·lació

Primer de tot instalem la llibreria
```
pip install spotipy --upgrade
```

## Importació i Credencials

A continuació importem a python, definim credencials i autentifiquem.

```python
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
  
SPOTIPY_CLIENT_ID='ID' #definim claus  
SPOTIPY_CLIENT_SECRET='SECRET'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET) #autentiquem  
sp = spotipy.Spotify(auth_manager=auth_manager) #emagatzema les credencials per reutilitzar-les 
   
```
## Query de playlist

Busquem una playlist, copiant el codi ID de la url

```python

playlist = '3oopyXIZGLFtHjFYN9KbuI'
```

Busquem a L'API reference la manera que contempla la llibreria per accedir a les playist, en aquest cast: playlist_items

Fem una query

```python
#https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_items  
query = sp.playlist_items(playlist, fields= None, limit=100, offset=0, market=None )
```

## Exportació a json per determinar l'estructura de les dades

La passem a un json per veure quines dades estem passant:

```python
with open('hola.json', 'w', encoding='utf-8') as f:  
    json.dump(query, f, ensure_ascii=False, indent=4) #passem la query a un document json. ensure_ascii=False permet emagatzemar emojis
```

Analitzem per veure com s'estructura la info i els camps que ens poden interessar.

Un cop determinem la info ja podem iterar per obtenir-la. En aquest cas busquem els artistes de cadascuna dels tracks dins la playlist.

```python

  
for i in query["items"]:  
    artists=i["track"]["artists"]  
    for artist in artists:  
        print(artist["name"])
```

Per generar un graph necessitem crear una llista amb dues dimencions: source|target
que estableixi les relacions de recomanació.


#IA Anàlisi de missatges d'odi a RRSS 



Hugging Face com a alternativa obreta a OpenAI 

Instal·lem transformers 
Instal·lem py torch -> llibreria encarregada de crear xarxes neuronals a python 
Similar a tensorflow, però tensorflow està pensada per funcionar amb més llenguatges. Per treballar a nivell global amb multiples dispositius -> tensorflow 


El pipe descriu el que volem que la xarxa neuronal faci 

si executem 

```python 

pipe = pipeline("text-classification") 
``` 
32 / 54
En retornarà tot el que podem fer 

# Tokenizer 

el sistema agafa la frase i segmenta, per segmentar necessita el tokenizer 

RAW DATA --> Tokenitzador (fragmenta la info a processar i atorga una puntuació positiva o negativa) --> Model (processa amb xarxes neuronals els tokens i n'extreu una puntuació final) 

```python 

##### DEPENDENCIAS 
# pip install tqdm 
# pip install pandas 
# pip install transformers 
# pip install torch 
##### 
33 / 54

##### EJEMPLOS DE MODELOS 
# https://huggingface.co/MMG/xlm-roberta-base-sa-spanish 
# https://huggingface.co/jorgeortizfuentes/spanish_hate_speech 
# https://huggingface.co/francisco-perez-sorrosal/distilbert-base-uncased-finetuned-with-spanish-tweets-clf 
##### 

from tqdm import tqdm 
import pandas as pd 
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline 

df = pd.read_csv("dataset-inmigracion.csv", nrows=100, usecols=["tweet_id","text"]) 
34 / 54
print(df) #carreguem dataset 

# Carregar Model 
tokenizer = AutoTokenizer.from_pretrained("jorgeortizfuentes/spanish_hate_speech") #agafem el model que volem 
model = AutoModelForSequenceClassification.from_pretrained("jorgeortizfuentes/spanish_hate_speech")#el carreguem 

# Generar el Pipeline 
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer) #el tokenizer és l'encarregat de fragmentar la frase 

tweets = df["text"].to_list() #generem una llista de tweets 
35 / 54
tweet_id = df["tweet_id"].to_list() #generem una llista de tweet_ids 

tup_list = [] 

for tweet, tid in zip(tweets, tweet_id): #per cada tweet i per cada id 
   result = pipe(tweet) 
   print(result) 
   content = result[0] 
   label = content["label"] 
   score = content["score"] 
   tupla = (str(tid), tweet, label, score) 
   tup_list.append(tupla) 

data = pd.DataFrame.from_records(tup_list, columns=["id", "text", "label", "score"]) 
data.to_csv("analysis.csv", index=False) 
