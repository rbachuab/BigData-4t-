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
