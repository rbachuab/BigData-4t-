
# Twitch API

Tota la comunicació entre el frontend/aplicació d'escriptori d'una plataforma i les bases de dades passen per una API intermediaria.

Per fer solicituds a una api hi ha dues vies:
	Oficialment
	Versións simplificades
		Són versions on s'ha afegit un nivell de codi per simplificar el procés de peticions de dades. En aquest cas són llibreries.


## 1. Generem les credencials per comunicar-nos amb la API

Primer de tot hem de registrar l'aplicació a la consola. Com a url posem el localhost


Ens connectarem des de la seguent API en la versió 2.5.7, que és més senzilla.
https://pytwitchapi.readthedocs.io/en/v2.5.7/index.html

Guia: https://pytwitchapi.readthedocs.io/en/v2.5.7/index.html

Aleshores instalem a PyChart l'API en la versió amb la que treballarem.

```python
pip install twitchAPI==2.5.7.1 #instal·lació de les llibreries de la API
```
## 2. Importació de llibreries i autentificació

A continuació importem llibreries

```python
from twitchAPI.twitch import Twitch #importem api de twitch
from pprint import pprint #No cal, serveix per imprimir per pantalla la informació de manera ordenada.

twitch = Twitch('my_app_key', 'my_app_secret') #Establim les credencials amb les que ens identificarem a l'hora de fer peticions.

print(twitch.get_users(logins=['your_twitch_username']))
```

Substituim my_app_key per la credencial que hem creat a la consola de twitch dev, i generem una clau secreta.

A continuació el codi imprimeix la informació que retorna de l'API amb la info vinculada al nom d'usuari de twitch que posem.

Ara podem extreure info de Twitch, per exemple demanem els streams dels 20 primers en espanyol.

```python
streams = twitch.get_streams(first=20, language="es") #exemple de petició de streams. Acotem als primers 20 i en espanuol. Podem consultar la resta de paràmetres a la pàgina de documentació de la API

```
## 3. Exportat a json

Això genera una llista de dades poc clarificadores. Bolquem les dades a un fitxer json

```python
import json
from twitchAPI.twitch import Twitch
from pprint import pprint #No cal

twitch = Twitch('my_app_key', 'my_app_secret')



streams = twitch.get_streams(first=20, language="es")

with open("output_file.json", 'w', encoding='utf-8') as f:  
    json.dump(streams, f, ensure_ascii=False, indent=4) #carreguem la llista resultant a un fitxer json mitjançant el .dump

```

Aquest json ens permetrà visualitzar les diferents dades que podem extreure de cada directe. (Només l'excecutem un cop)

# Funció Recursiva

```python

def funciorecursiva():
	print("iep")
```

Dummy Variables: en funcions recursives s'utilitzen com a variables que només tindran ús eal primer cop que invoquem la funció, podem posar None com a valor.
