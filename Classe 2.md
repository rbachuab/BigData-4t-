# python

Versió de Python -> cada versió implementa noves funcions/n'aparta les obsoletes.

Python parteix d'una BASE, tot el que volguem i que no estigui inclòs a la base, ho afegim mitjançant mòduls o llibreries. Per tal d'integrar-se a la base de python, les llibreries depenen de la versió de Python de la base per funcionar, si les versions varien es poden donar incompatibilitats.

Per solucionar la incompatibilitat entre versions PyCharm genera entorns virtuals per cada projecte amb la versió desitjada.

#### LLibreries

Les llibreries s'instal·len a cadascun dels projectes en cas de no haver-les instal·lat a l'arrel de python de l'ordinador.

### Variables

Són immutables

````python
""" Fan un comentari"""
````
### Llistes

```Python
array=["a","b","c"]
````

Imprimir variables dins de text:

```python
array=["a","b","c"]  
  
for a in array:  
    print(f"En {Nom} no ha vingut a classe :(")
```

### For

Loops per iterar arrays 

```Python
	num = [1,2,3,4,10]  
afegir =2  
  
for alumnes in num:  
    alumnes += afegir  
    print(alumnes)
```

### Condicionals

##### If/Else

```python
llista_compra=["Pomes", "Tomaquets", "iogurt"]  
  
for producte in llista_compra:  
    if producte=="Tomaquets":  
        print(producte)  
    else:  
        print("No hi ha tomaquets a la llista")
```

##### Elif
Per comprovar més de dos condicions

```python
nums=[1,2,3,4,5,6,7,8,9]  
  
for num in nums:  
    if num<6:  
        print(f"{num} és més petit que 6.")  
    elif num==6:  
        print(f"El {num} és igual a 6")  
    else:  
        print(f"{num} és més gran que 6")
```

##### Len
Funció integrada a python per contar el nombre d'elements d'una llista, una string etc.

#### Index
Aquesta funció ens permet saber quin index ocupa un element dins d'una llista.

```python
llista = ["adrià", "maria", "lluís"]  
  
nom = "maria"  
  
if nom in llista:  
    position = llista.index(nom)  
    print(position)
```

### Set
Elimina valors duplicats d'una llista

```python
llista = ["adrià", "maria", "lluís", "dani", "dani", "alex"]  
  
valors_unics = len(set(llista))  
print(valors_unics)
```


# Exercicis

## Exercici 1

```python
ex1 = "esto es un ejercicio" #creem una variable que conté la string
print(ex1) #imrpimim la variable
  
nota_examen = 9  #definim la nota de l'examen
print(nota_examen)  #imprimim la nota de l'examen
  
asignatura="Creació d'objectes digitals" #creem la variable assignatura amb la string que conté el nom
  
print(f"En la asignatura {asignatura} he obtenido un {nota_examen}.") #imprimim la relació entre assignatura i la nota de l'examen  
  
frase= f"En la asignatura {asignatura} he obtenido un {nota_examen}." #guardem el contingut del print en una variable
  
nota_examen = 3 #reescrivim la nota de l'examen.

print(frase) #imprimim la frase del print amb la nota actualitzada.
```

## Exercici A


## Exercici B

Per iterar dues llistes alhora podem fer servir la funció zip() per unir-les.

```python
notas = ["5","7","6","4","8","2"]  
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]  
  
for nota, nom in zip(notas, alumnos):  #iterem les dues llistes amb la funció zip
    nota = int(nota) + 1  #passem la string nota a enter i li sumem 1
    print(f"L'alumn@ {nom} té un {nota}.") #imprimim la relació entre l'alumne i la nota.
```

## Calculos

### Ejercicio A (Easy mode)

La UAB acaba de celebrar sus jornadas de puertas abiertas y los futuros estudiantes han acudido a las sesiones informativas. Cada vez que una persona entra en una sesión se anota su nombre. Alguien ha juntado todos los nombres en una sola lista... ¿Puedes sacar información útil de este listado?

1.  ¿Cuantas personas han asistido a las jornadas de puertas abiertas?
2.  ¿Cuantas personas han asistido a más de dos sesiones?
3.  ¿Qué porcentaje de los asistentes accede a más de dos sesiones?

```python
#1
llista_neta = set(llista)  #netegem la llista amb set() per descartar els noms repetits
print(f"Han assistit {len(llista_neta)} persones.") #imprimim el nombre total de persones que han assistit.
```

```python
#2  
contador_duplicats = 0  #establim un contador
for assistent in llista_neta:  
    if llista.count(assistent)>1:  
        contador_duplicats+=1  
print(f"{contador_duplicats} han assistit més d'una vegada.")
```

```python
#3
percent= (contador_duplicats / len(llista_neta)) * 100  
print(percent)
```

### Ejercicio B (dificultad media*)

```python
notes = ["5","3","7","8","9.5","4","6,2"]  
alumnes = ["adria","agnès","josep","rafa","cristina","Gemma","Eduard"]  
  
  
total_notes= 0 #establim un contador  
for n, al in zip(notes, alumnes): #itarem les dues llistes alhora  
    print(f"El alumno/a {al} ha obtenido un {n}") #imprimim les notes de cadascun dels alumnes  
    n = n.replace(',', '.') #substituim totes les comes de la llista per punts, per tal d'evitar errors de càlcul.  
    total_notes += float(n) #transformem l'string de la llista a decimal per afegir al contador  
  
  
mitjana = total_notes / len(notes) #calculem la longitud de la llista i calculem la mitjana  
nota_max = max(notes) #calculem la nota més alta  
nota_min = min(notes) #calculem la nota més baixa  
  
print(f"La nota mitjana és {round(mitjana,1)}") #imprimim la nota mitjada arrodonida a un decimal  
print(f"La nota més alta és {nota_max} i és de {alumnes[notes.index(nota_max)]}") #imprimim la nota més alta i busquem quina posició ocupa dins la llista de notes per tal d'imprimir la mateixa posició de la llista d'alumnes. 
print(f"La nota més baixa és {nota_min} i és de {alumnes[notes.index(nota_min)]}") #imprimim la nota més baixa i busquem quina posició ocupa dins la llista de notes per tal d'imprimir la mateixa posició de la llista d'alumnes. ```
