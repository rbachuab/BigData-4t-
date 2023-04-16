
# 1. ¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?

![Evolució d'espectadors](https://github.com/rbachuab/BigData-4t-/blob/main/EXERCICI_PANDAS/Pasted%20image%2020230416102430.png?raw=true)

Analitzant el gràfic de l'evolució d'espectadors a Twitch durant el més de febrer, podem veure clarament que té un comportament cíclic: pels matins, de 8h a 15h aproximadament, el volum d'espectadors decreix fins a arribar a un mínim diari estable que ronda els 60.000 espectadors. De 15h a 20h es produeix una tendència a l'alça fins a arribar al primer pic dirari, al voltant de les 21h, aleshores decreix subtilment per remuntar a continuació fins al màxim diàri, que s'acostuma a produir a les 23h. Posteriorment, el volum d'espectadors segueix sent elevat, però segueix una tendència a la baixa fins que decreix pronunciadament entre les 3 del matí i les 8h. Aquest comportament descriu els habits de consum de la plataforma en parla castellana, sent la franja horaria del vespre la que més espectadors rep, tan per ser el moment en que la majoria de gent a Espanya no va a treballar o a l'escola, com per coincidir amb els espectadors de Sud-amèrica.

Vist el comportament cíclic, destaquen les variacions al llarg del mes en els pics màxims d'espectadors. D'aquests pics destaquen sobre la resta el del 26/2, arribant al màxim capturat de febrer amb 1.638.108 espectadors, el del 27/2 i el del 28/2, tots tres superant el milió d'espectadors connectats. Els tres pics, coincideien amb macro-esdeveniments impulsats per la comunitat de streamers en parla hispana, que generen molta expectació del públic i donen músucul per enlairar les xifres d'audiència. En aquest cas el 26 de febrer es va jugar la Kings League amb l'ex-jugador professional Ronaldinho com a convidat especial. El 27 l'Ibai va presentar el seu esdeveniment propi, La Velada del Año 3. Finalment, el pic del 28 coincideix amb els Squid Games, potenciats segurament amb el que al diari Marca i Vandal titulaven com el retorn sorpresa d'Auronplay després de distanciar-se del focus d'atenció.


# 2. ¿Cuáles son las categorías más vistas y en las que más horas de directo se han realizado?

![Categories més vistes](https://github.com/rbachuab/BigData-4t-/blob/main/EXERCICI_PANDAS/Pasted%20image%2020230416105844.png?raw=true)

El top 10 categories més vistes el més de febrer de 2023 són Just Chatting, Sports, Minecraft, League of Legends, VALORANT, Hogwarts Legacy, GTA V, Fortnite, Special Events i FIFA 2023.

Destaca especialment el domini de Just Chatting (186.414.128 d'espectadors) per damunt de la resta de categories, arribant a l'extrem que si sumessim els espectadors de les tres categories seguents en el rànquing, Sports, Minecraft i League of Legends, no arribariem encara al total de Just Chatting. Així doncs, és la categoria amb més demanda de la plataforma, si bé és cert que també és la més àmplia i variada en termes dels continguts que poden contenir.

Anem a veure les que més hores tenen:

![Categories per hores](https://github.com/rbachuab/BigData-4t-/blob/main/EXERCICI_PANDAS/Pasted%20image%2020230416111132.png?raw=true)

En aquest cas la categoria que apareix més al llarg de les captures és Fortnite (si dividim el nombre d'ocurrenciès fetes cada 15 min entre 4 obtenim un valor aproximat de 858 mil hores de directe), seguida de VALORANT, Just Chatting, League of Legends i Minecraft. 

Podem veure una petita correlació entre el nombre d'hores invertides i el volum d'espectadors de cada categoria, veient que els jocs als que més es juga acostumen a situar-se també entre els més vistos, amb petites variacions de popularitat que poden fer-los pujar o baixar lleugerament en la classificació d'espectadors totals. D'aquesta manera podriem col·locar Fortnite i Valorant com les més streamejades, mentre que Just Chatting, amb una lleugera variació d'hores, supera àmpliament en popularitat a les altres dues. 

D'entre totes aquestes categories, però, hi ha dos casos que destaquen per la seva excepcionalitat, i que no han aparegut en la segona gràfica que hem analitzat. Si comparem el volum d'hores en directe, amb el nombre total d'espectadors de cada categoria, ens trobem el gràfic a continuació:

![Categories mes vistes per hores invertides](https://github.com/rbachuab/BigData-4t-/blob/main/EXERCICI_PANDAS/Pasted%20image%2020230416113144.png?raw=true)

![Top 10 categories](https://github.com/rbachuab/BigData-4t-/blob/main/EXERCICI_PANDAS/Pasted%20image%2020230416113636.png?raw=true)

Tan la categoria Sports com la categoria Special Events apareixen al top 10 de categories amb més espectadors, però les dues tenen un nombre d'hores en directe dràsticament inferior. Aquestes dades ens donen altra vegada nocions sobre la força que tenen els grans esdeveniments com a fenòmen a Twitch. La categoría Sports es la categoria en que es comptabilitza la Kings League, responsable del màxim pic d'audiència del mes de febrer. La categoria Special Events, tal com el nom indica, dona cabuda a aquest tipus d'esdeveniments. La capacitat d'atracció d'espectadors d'aquestes categories amb un volum d'hores de directe irrisòria en comparació amb la resta de categories dominants, demostres la gran popularitat que tenen aquests continguts dins de Twitch.


# 3. ¿Cómo han evolucionado (captura a captura) estas categorias a lo largo del mes?


![Evolució categories](https://github.com/rbachuab/BigData-4t-/blob/main/EXERCICI_PANDAS/Pasted%20image%2020230416115538.png?raw=true)

Si observem les evolucions de les 10 categories amb més espectadors durant el més de febrer es reafirma l'analisi fet anteriorment: els pics d'audiència coincideixen en gran mesura amb grans esdeveniments dins la plataforma.

En general les categories dominants, mantenen un cicle estable i perllongat en el temps, que segueix els hàbits de consum de Twitch pel que fa a les hores en que es produeixen els màxims i mínims. Aquest és el cas de jocs com Fortnite, GTA V, el LOL, o el Valorant. 

Per altra banda, veiem com el comportament cíclic d'algunes de les categories es veu trencat pels grans esdeveniments introduïts més amunt. En el cas de la categoria de Sports, els pics coincideixen amb els caps de setmana en que s'ha jugat la Kings Legue, culminant amb el cap de setmana en que apareix Ronaldinho. En el cas de Minecraft, els cicles habituals es veuen despuntats per esdeveniments com els Squid Craft Games 2. I fins i tot, el màxim que despunta de Just Chatting es pot vincular a la casuística del retorn de l'Auronplay, que no seria un esdeveniment com a tal, malgrat que es vinculi amb els Squid Craft Games, però si una fita amb gran interes pel públic de la plataforma.

Seria interessant comparar el Top 10 categories de febrer, amb el Top 10 categories amb més espectadors de mesos anterios per veure quines són les categories amb una trajectòria més sòlida. D'aquesta manera podriem acabar d'aïllar alguns casos com el de Hogwarts Legacy, que es comporta d'una manera molt diferent a la resta de categories segurament més ben establertes.

# 4. ¿Cuál es la distribución de los streamers si los clasificamos por volumenes de audiencia y horas realizadas?


Si observem els streamers més vistos a Twitch durant el mes de febrer veiem que destaca per davant de tot altre cop la Kings League, amb un total de 43.710.847 espectadors, seguida per ibai, illoJuan, ElSpreen, juanguarnizo, ElMariana, LVPEs, el xokas, auronplay i rivers_gg en el top 10 més vistos. A simple vista, es reafirma el lideratge d'actors com la Kings League i ibai en l'acaparament d'espectadors dins de Twitch, tal com veniem veient en la resta de l'anàlisi, situant-se entre els més vistos. És destacable la presencia també d'auronplay, que tot i no haver fer streamings durant tot el febrer, la tornada va ser prou potent com per colar-se en el top 10 amb més espectadors. 

Tanmateix, seria interessant analitzar en quines categories han passat més hores fent directes aquests canals, per acabar de constatar la vinculació que tenen amb les categories més vistes. En el cas de la kings league amb Sports, ibai amb Just Chatting i Special Events, i la resta amb les seves categories respectives. Aquest anàlisi permetria detectar, si hi ha algun streamer que està fent directes en una categoria diferent a les mencionades com a més consumides pels espectadors a nivell global.

El rànquing canvia dràsticament quan analitzem el numero d'hores de directes realitzades al mes de febrer.

![Nombre d'hores en directe](https://github.com/rbachuab/BigData-4t-/blob/main/EXERCICI_PANDAS/Pasted%20image%2020230416174719.png?raw=true)

La llista que es mostra en la gràfica són canals que han deixat el directe obert al voltant de 672 hores, que corresponen a les hores que va tenir el mes de febrer. No obstant això, pel que fa al volum d'espectadors, tan sols el canal viviendoenlacalle té una suma important, concretament de 3.539.891 espectadors, col·locant-lo en la posició 22 dels streamers més vistos durant aquest mes. 

![Total espectadors per hores en directe](https://github.com/rbachuab/BigData-4t-/blob/main/EXERCICI_PANDAS/Pasted%20image%2020230416175736.png?raw=true)

Pel que fa al top 10 streamers més vistos, el que ha fet més hores és LVPes, al voltant de les 292 hores, situant-se en setena posició en volum d'espectadors. Mentre que com s'ha observat, auronplay, tot i només haver fet directe al voltant de 19 hores, ha superat en espectadors a la rivers_gg, que li triplicava el nombre d'hores, degut a la espectació de la seva tornada.

Amb aquestes dades es pot concloure que no hi ha una relació directe entre el nombre d'hores en directes que fa un streamer i el volum d'espectadors que rep, sinó que el resultat d'audència va relacionat en la popularitat del contingut i/o streamer ,i l'espectació que es genera en un moment concret.

# 5. ¿Cuál ha sido la evolución (captura a captura) de la desviación estándar en el volumen de espectadores?

![Dispersió](https://github.com/rbachuab/BigData-4t-/blob/main/EXERCICI_PANDAS/Pasted%20image%2020230416182308.png?raw=true)

La desviació estándar en el volum d'espectadors es manté estable la majoria de dies del mes, excepte quan es produeixen picss de desviació coincidint amb els dies assenyalats pels esdeveniments, que marquen un punt de ruptura amb la tendència de la desviació quan no esprodueixen aquests esdeveniments. El 26 de febrer es situa com el dia amb una variació més alta en el nombre d'espectadors del més de febrer.

# Conclusió

Tal com hem pogut veure Twitch segueix cicles en el volum d'espectadors que són constants al llarg del mes, de la mateixa manera que les categories més vistes acostumen a tenir una audiència estable, amb fluctuacions mínimes. No obstant això, aquests cicles es veuen trencats per esdeveniments clau dins la comunitat com el fenòmen de la kings league, que disparen els màxims d'espectadors per l'alt nivell d'interès per part de l'audiència. Fent que aquests esdeveniments, trenquin amb les tendències habituals de la plataforma.

