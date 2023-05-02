
# Anàlisi d'interacció a Twitter durant la campanya de les eleccions municipals 

El dataset d'aquesta anàlisi conté tweets publicats entre l'1/04/2023 i el 16/04/2023, al voltant dels polítics Basha Changue, Ernest Maragall, Ada Colau, Jaume Collboni, Xavier Trias, Anna Grau, Eva Parera, Daniel Sirera, candidats a les eleccions municipals a Barcelona aquest 2023. 

Dels 40.913 tweets que conformen el dataset, se n'han pogut analitzar un total de 30.044, netejant el més acuradament possible el text dels tweets per trobar-hi la presència dels polítics mencionats. Per exemple, tweets on es cita a l'Ada Colau com a Ada C, no s'han tingut en compte. No obstant això, els tweets descartats són saltejats dins la mostra, i en tot cas els tweets analitzats suposen un 73,4% del total capturat. 

Tenint en compte, doncs, que partim de l'anàlisi de 30.044 tweets, anem a respondre les següents preguntes:

# Quin és el candidat més mencionat?

![](https://github.com/rbachuab/BigData-4t-/blob/main/Exercici%20Twitter/Pasted%20image%2020230501112657.png)

Si observem els candidats per nombre de tweets en què apareixen mencionats, ens trobem amb uns resultats desproporcionats. L'Ada Colau concentra el 76,44% dels tweets, concretament 22.966, sent la que més opinió genera per part dels usuaris. Mentre que el segon més mencionat, en Xavier Trias, se'l menciona gairebé deu vegades menys: 2.807 tweets. Les candidates per Valents i la Cup, Eva Parera i Basha Changue, tenen un volum similar de tweets, seguides de l'Anna Grau, Jaume Collboni i finalment, Daniel Sirera, que tanca la llista amb 601 mencions. 

Un fet a tenir en compte en els resultats és que mentre la resta de candidats no tenen una vida pública accentuada, Ada Colau és l'actual alcaldessa de Barcelona i se l'acostuma a mencionar en tweets que no tenen tant a veure amb la campanya de les municipals, sinó amb la gestió i notícies de la ciutat. És molt probable, doncs, que part dels tweets no vinguin derivats de la campanya electoral, tot i que pel context de les dates en què es produeixen, sí que tindran influència en la percepció de la candidata.

# Quina és la repercussió dels tweets en què es mencionen els candidats?

![](https://github.com/rbachuab/BigData-4t-/blob/main/Exercici%20Twitter/Pasted%20image%2020230501183034.png)

Vist que l'Ada Colau és la que més volum de mencions acumula, analitzem quina repercussió tenen els tweets en què es menciona cadascun dels candidats. Per fer-ho tindrem en compte en la mitjana de likes, la mitjana de replies i la mitjana de retweets de cada menció. 

Pel que fa a la mitjana de likes, podem observar com Jaume Collboni i Ada Colau es situen al capdavant amb una mitjana de 3,2 likes per menció, seguits per Basha Changue i Anna Grau, entre 2,6 i 2,7 likes; i la resta de candidats al darrere, amb Daniel Sirera a la cua. 

Pel que fa a la mitjana de replies, Basha Changue lídera la llista, 1 reply per menció de mitjana, seguida per Jaume Collboni, Anna Grau i Ada Colau. Finalment la mitjana de retweets ens mostra el domini d'Ada Colau, amb 791 retweets de mitjana per menció, Eva Parera amb 318,4 i Jaume Collboni amb 105,4. 

D'aquests resultats destaca el rendiment de Jaume Collboni, que amb tan sols 707 mencions, té una repercussió per menció equiparable a la de l'Ada Colau. 

Basha Changue és la candidata que més respostes generen els tweets en què se la menciona i tercera en likes, no obstant això, el tipus de mencions no generen el mateix volum de retweets. Eva Parera té una mitjana de retweets que només és superada per la mitjana de l'Ada, malgrat que en la resta de categories no destaqui. 

Seria interessant vincular aquestes mètriques al contingut del text, per veure realment si són favorables o no aquests tweets. En aquest moment, de forma descontextualitzada, tan sols podem concloure que l'Ada Colau és la que té més repercussió quan se la menciona, en nombre de retweets, i en una mitjana de likes i replies sòlida respecte a la resta de candidats. Les mencions de Basha Changue són les que generen més discussió dins del tweet en què se la menciona, molt igualada amb Jaume Collboni, que alhora complementa la discussió amb nombre de likes. En les tres mètriques, en David Sirera queda lluny dels seus rivals, fet que de primeres fa pensar que no té molta presència en les discussions de la xarxa.

# Quins són els usuaris més actius?

![](https://github.com/rbachuab/BigData-4t-/blob/main/Exercici%20Twitter/Pasted%20image%2020230501183535.png)

Els 15 usuaris que han fet més mencions a candidats n'han fet entre 29 i 70. En primer lloc, trobem el diari naciodigital amb 70 mencions, seguit de 5 usuaris i el compte del diari El Nacional.cat. Altres comptes rellevants són BTVnotícies, bcnencomu (el partit de l'Ada Colau) i el compte de CUPBarcelona (el partit de Basha Changue).

Així doncs, els usuaris que més mencionen als candidats estan dividits entre entitats reconeixibles, com mitjans de comunicació i partits polítics, i usuaris de Twitter. 

Anem a veure sobre qui creen tweets cadascun d'aquests comptes per detectar si estan generant contingut al voltant d'un candidat en concret, o de tots alhora.

# A qui mencionen aquests usuaris?

![](https://github.com/rbachuab/BigData-4t-/blob/main/Exercici%20Twitter/Pasted%20image%2020230501190005.png)

El compte més actiu, @naciodigital ha mencionat de manera gairebé equitativa a tots els candidats -si bé Anna Grau ha rebut menys mencions i Ada Colau una mica més- tenint en compte que no totes les mencions de l'Ada Colau tenen relació amb les eleccions, podem dir que tractant-se d'un mitjà, ha comunicat de forma imparcial en el nombre de mencions, a falta d'analitzar el contingut. Una distribució semblant en el repartiment de mencions el trobem en els altres mitjans detectats, @btvnoticies i @elnacionalcat, aquest últim amb una mica més de fixació cap a Xavier Trias. 

El fenomen interessant comença a partir de l'observació del segon usuari més actiu, @LauraMartiBCN, que de les 59 mencions publicades, 58 són de l'Ada Colau i una d'en Xavier Trias. El mateix observem en el 4t usuari i com era d'esperar, en el compte de @bcnencomu. La detecció en el gràfic de columnes de pràcticament un sol color, ens mostren comptes generadors d'opinió al voltant d'un únic candidat: @despertaferro11 per Xavier Trias, @cupbarcelona per la Basha Changue, @derechacatalana amb Eva Parera. Caldria veure si l'opinió generada per aquests comptes és en positiu o en negatiu, i si les mencions a altres candidats per part d'aquests comptes busquen aconseguir l'efecte contrari, és a dir, el d'elogiar o criticar la part contrària.

# Visualització de les mencions 

![](https://github.com/rbachuab/BigData-4t-/blob/main/Exercici%20Twitter/Graf.png)

En aquest graf estan representades totes les mencions dels usuaris cap a un o més candidats a les eleccions municipals de Barcelona. Els núvols de punts, desemboquen a un o més nodes centrals, que representen cadascun dels candidats, els colors ens indiquen la proximitat de l'usuari a cada comunitat.

A primera vista, destaca la presència de l'Ada Colau, seguida per Xavier Trias que queda en segon pla i la resta de candidats. Aquests volums en la representació constaten els resultats del primer gràfic que hem analitzat sobre els candidats més mencionats. 

Ara bé, la creació d'un gràfic de graf ens permet observar a la pràctica una hipòtesi que hem arrossegat al llarg d'aquesta anàlisi: que l'Ada Colau rep moltes mencions desvinculades de la campanya. Si ens fixem en l'òrbita de nodes que envolta a l'Ada Colau, a la part inferior podem veure una quantitat immensa d'usuaris que mencionen a la candidata, però que queden aïllats de la resta de nodes, i per tant de la conversa. Aquesta distància es podria correspondre amb el fet que l'Ada, com a actual alcaldessa, rep mencions massives que no tenen per què anar relacionades a la campanya electoral, sinó que poden tenir a veure amb la seva connotació de persona pública i la gestió actual, que si bé influencien la percepció que es té sobre l'alcaldessa, no va vinculada a la campanya com a tal. 

Per contra, el núvol de nodes situat al centre del gràfic i que fa de punt d'unió entre les mencions de tots els candidats, és l'epicentre de la conversa al voltant de les eleccions municipals, ja que interrelaciona directament els diferents candidats que es presenten.

Si observem la resta de candidats, podem detectar un altre fenomen del qual hem parlat, i que en la comunitat que envolta l'Ada és difícil de destriar pel soroll de mencions alienes que hi ha. Tots els candidats tenen un núvol d'usuaris que l'apunten quasi exclusivament al seu node. Una part d'aquestes mencions, es donarà el cas com l'Ada Colau, que són alienes a la conversa al voltant de les eleccions, però entre aquestes agrupacions d'usuaris, es troben també els comptes que a l'apartat anterior hem etiquetat com a generadores d'opinió sobre els candidats, és a dir, els comptes que publiquen per alimentar la discussió sobre un dels polítics en concret, i no sobre la resta.

![](https://github.com/rbachuab/BigData-4t-/blob/main/Exercici%20Twitter/Pasted%20image%2020230502174111.png)
