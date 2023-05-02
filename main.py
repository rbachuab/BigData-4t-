import pandas as pd #importem llibreries
import glob
import json
import numpy as np



datasets = glob.glob("api_responses/*json") #importem els fitxer json amb glob
llista_politics = ['Basha Changue', 'Ernest Maragall', 'Ada Colau','Jaume Collboni', 'Xavier Trias', 'Anna Grau','Eva Parera', 'Daniel Sirera'] #creem una llista amb els polítics que volem analitzar

llista_mencions = [] #creem els contenidors que ens serviran per extreure les dades que ens interessen.
llista_autors = []
llista_likes = []
llista_retweets = []
llista_quoted = []
llista_replies = []

llista_graf = [] #creem una llista on hi bolcarem les dades necessàries per fer el graf

for data in datasets: #iterem tots els arxius json

    with open(data, encoding="utf-8") as f: #per cada fitxer, l'obrim i especifiquem que està codificat en utf-8
        pre_df = json.loads(f.read()) #passem les dades a un contenidor per processar-los

    for tweet in pre_df['data']: #interem cadascun dels tweets que conté el json
        lower_tweet = "" #establim la variable lower_tweet on hi posarem els tweets nets
        for word in tweet['text']: #iterem el contingut del text del tweet
            lower_tweet = lower_tweet + word.lower() #transformem tots els caracters a minuscula
            lower_tweet = lower_tweet.replace(" ","") #eliminem els espais en blanc

        for politic in llista_politics: #iterem la llista de polítics per trobar les mencions
            if politic.replace(" ","").lower() in lower_tweet: #mirem si la cadena de text del nom del polític, net, es troba entre els caràcters del text.
                llista_mencions.append(politic) #En cas que hi sigui, carreguem el nom del politic, sense netejar a la llista de mencions.
                llista_likes.append(tweet['public_metrics']['like_count']) #carreguem la resta de mètriques qu interessen
                llista_retweets.append(tweet['public_metrics']['retweet_count'])
                llista_quoted.append(tweet['public_metrics']['quote_count'])
                llista_replies.append(tweet['public_metrics']['reply_count'])

                author_id = tweet['author_id'] #guardem l'author_id
                for user in pre_df['includes']['users']: #iterem cada usuari present a la llista de users
                    if user['id'] == author_id: #si la id d'aquests usuaris coincideix amb l'autor del tweet que estem processant,
                        user_name = user['username'] #el guardem com a user_name
                        break #parem el for

                    else: #en cas contrari, seguim iterant
                        pass
                llista_autors.append(user_name) #afegint l'user_name a la llista d'autors


                df_graf = pd.DataFrame({"source": user_name, "target": politic}, index=[0]) #creem el dataframe amb les columnes source i target per l'elaboració del graf
                llista_graf.append(df_graf) #afegim el dataframe a la llista_graf


#print(tweets)
#print(len(llista_mencions))
#print(len(llista_likes))
#print(len(llista_autors))

#print(len(data['user_id']))

df = pd.DataFrame (np.column_stack([llista_mencions, llista_autors, llista_likes, llista_retweets, llista_quoted, llista_replies]),
                               columns=['politics_name', 'author_name', 'likes', 'retweets', 'quoted', 'replies']) #creem el dataframe i apilem les llistes a dins

df_graf_final = pd.concat(llista_graf) #concatenem el dataframe del graf

df_graf_final.to_csv("graf.csv", index=False) #exportem el dataframe del graf a csv
df.to_csv('Mencions.csv', index=False) #exportem el dataframe amb les mètriques de les mencions a csv.