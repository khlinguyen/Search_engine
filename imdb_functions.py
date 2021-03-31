# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:44:23 2020

Ce module appelé « imdb_functions » a été construit autour du thème cinématographique.
Il vise 2 principales tâches, à savoir importer les données du site kaggle et définir 
plusieurs fonctions qui permettent d'accéder à une information précise dans ces dernières.
"""

import pandas as pd

path = "C:/Users/dionc/Desktop/Données"

IMDb_movies= pd.read_csv(path+"/IMDb movies.csv", sep=",")
IMDb_names= pd.read_csv(path+"/IMDb names.csv", sep=",")
IMDb_ratings= pd.read_csv(path+"/IMDb ratings.csv", sep=",")
IMDb_title_principals= pd.read_csv(path+"/IMDb title_principals.csv", sep=",")

def get_movie_info(movie): 
   # 1- Constitution de la dataframe pertinente
    
      # On convertie toutes les variables d'intérêts en minuscule pour éviter les erreurs lié a la saisi de majuscules ou non
      movie1=movie.lower()  
      IMDb_movies["title_low"]=IMDb_movies["original_title"].str.lower()
      result1 = IMDb_movies[IMDb_movies["title_low"].str.contains(movie1)]
      
      #trie par année du plus récent au plus anciens
      result1["year"] = result1["year"].astype(str).astype(int)
      result1=result1.sort_values(by='year', ascending=False)
      
      #Gestion des erreurs de saisie et des films qui ont un même titre
      a=result1.shape
      if a[0]==0 :
          res="\n Aucun résultat trouvé pour un film au nom de "+movie+"."+"\n"
          res=res+" Veuillez vérifier votre saisie."
      
        #Recupération de l'info
      else :  
          result1 = result1[['imdb_title_id','original_title','date_published','duration','genre','country','language','actors','description']]
          result2 = IMDb_ratings[['imdb_title_id','mean_vote','allgenders_0age_avg_vote','allgenders_18age_avg_vote','allgenders_30age_avg_vote','allgenders_45age_avg_vote']]
          result = pd.merge(result1, result2, on='imdb_title_id', how='inner')
          
    # 2-3 Extraction de l'information, On stock toute l'information récupéré dans une variable char appelé result
          res=str(a[0])+" résultat(s) trouvé(s) pour le titre "+movie+".\n\n\n"
          i=0
          while i<a[0] :
              res = res+"Titre original du film : "+str(result["original_title"][i])+"\n"+"\n"
              res = res +"Date de sortie : "+str(result["date_published"][i])+"\n"+"\n"
              res = res +"Durée : "+str(result["duration"][i])+"mins"+"\n"+"\n"
              res = res +"Genre : "+str(result["genre"][i])+"\n"+"\n"
              res = res +"Pays de production : "+str(result["country"][i])+"\n"+"\n"
              res = res +"Langue du film : "+str(result["language"][i])+"\n"+"\n"
              res = res +"Les acteurs principaux : "+str(result["actors"][i])+"\n"+"\n"
              res = res +"Description : "+str(result["description"][i])+"\n"+"\n"
              res = res +"Note moyenne : "+str(result["mean_vote"][i])+"\n"
              res = res +"Note moyenne reçue par les - de 18 ans : "+str(result["allgenders_0age_avg_vote"][i])+"\n"
              res = res +"Note moyenne reçue par les [18-29] ans : "+str(result["allgenders_18age_avg_vote"][i])+"\n"
              res = res +"Note moyenne reçue par les [30-44] ans : "+str(result["allgenders_30age_avg_vote"][i])+"\n"
              res = res +"Note moyenne reçue par les + de 45 ans : "+str(result["allgenders_45age_avg_vote"][i])+"\n\n"
              res = res +"---------------------------------------------------------------------------------------------"+"\n\n"
              i=i+1
      return res



def get_commun_actors(movie1,annee1,movie2,annee2):
 # 1-Constitution de la dataframe pertinente

    #Filtrage titre film
  actors1 = IMDb_movies.loc[IMDb_movies["original_title"] == movie1]
  actors2 = IMDb_movies.loc[IMDb_movies["original_title"] == movie2]
    #Filtrage annnee film
  actors1 = actors1.loc[IMDb_movies["year"] == annee1 ]
  actors2 = actors2.loc[IMDb_movies["year"] == annee2]
  actors1 = list(actors1["actors"])
  actors2 = list(actors2["actors"])
  actors1 = actors1[0].split(',')
  actors2 = actors2[0].split(',')
  actors1_=[]
  actors2_=[]
  
 # 2-3 Extraction de l'information, On stock toute l'information récupéré dans une variable char appelé result
  for element in actors1:
        actors1_.append(element.strip())
  for element in actors2:
        actors2_.append(element.strip())    
  actors2_=set(actors2_)
  actors1_=set(actors1_)
  result=list(actors2_.intersection(actors1_))
  list_final = ', '.join(result)
  if result==[] :
        resultat="Ces acteurs n'ont joué dans aucun film en commun."
  else:
       resultat="Liste des acteurs en commun pour ces 2 films :\n"+list_final
  return resultat




def get_actor_info(name):
 # 1-Constitution de la dataframe pertinente  
    df1=IMDb_names.copy()
    df2=IMDb_title_principals.copy()
    df3=IMDb_movies.copy()
    df4=IMDb_ratings.copy()

    df1=df1.loc[lambda df1:df1['name']==name,:]

 # 2-Extraction de l'information
    #Gestion des erreurs de saisie 
    a=df1.shape
    if a[0]==0 :
        result="\n"+" Aucun résultat trouvé pour un acteur/une actrice au nom de "+name+"."+"\n"
        result=result+" Veuillez respecter les majuscules et vérifier votre saisie. "
    
    #Recupération de l'info
    else: 
        result = pd.merge(df1, df2,how="left", on='imdb_name_id')
        
        result1=pd.merge(result,df3, how="left",on='imdb_title_id' )
        
        result2=pd.merge(result1,df4, how="left",on='imdb_title_id' )
        
        
        list_film=result2['original_title']
        list_co_stars=result2['actors']
        list_bio=result['bio']
        biographie=list_bio[0]
        
        moyenne=result2['weighted_average_vote'].mean(skipna=True)
        max_=result2['weighted_average_vote'].max(skipna=True)
        min_=result2['weighted_average_vote'].min(skipna=True)
        
        
        max_1=result2[result2['weighted_average_vote']==result2['weighted_average_vote'].max()]
        min_1=result2[result2['weighted_average_vote']==result2['weighted_average_vote'].min()]
        title_max=max_1['original_title'].to_string(index=False)
        title_min=min_1['original_title'].to_string(index=False)
        
        complete_list=[] 
        for element in list_co_stars:
            l=element.split(',')
            complete_list=complete_list+l
        
        complete_list1=[]
        for element in complete_list: 
            complete_list1.append(element.strip())
        
        for element in complete_list1: 
            if element==name: 
                complete_list1.remove(element)
        
        complete_list1=list(set(complete_list1)) 
        nb_stars=len(complete_list1)
        liste="" 
        for element in complete_list1: 
            liste=liste+", "+element 
        liste_final_costars=liste[1:]
            
        liste_film_final=""
        for element in list_film: 
            liste_film_final=liste_film_final+"\n"+element
        
  # 3- On stock toute l'information récupéré dans une variable char appelé result
        result=""
        result=result+"Nom de l'acteur : "+name
        result=result+"\n"+"\nBiographie:\n"+biographie
        result=result+"\n"+"\nListes des films dans lequel il/elle a joué :"+liste_film_final
        result=result+"\n"+"\nNote moyenne sur IMDb des films dans lequel il a joué :"+str(round(moyenne,1))
        result=result+"\nNote maximum sur IMDb des films dans lequel il a joué :"+str(max_)+", Titre : "+title_max
        result=result+"\nNote minimum sur IMDb des films dans lequel il a joué :"+str(min_)+", Titre : "+title_min
        result=result+"\n"+"\nCet acteur / Cette actrice"+" a joué aux côtés de "+str(nb_stars)+" acteurs dans sa carrière dont :\n"+liste_final_costars
    return result


 
   
def get_best_movie(annee,genre):
 # 1 - Constitution de la dataframe pertinente
    df3=IMDb_movies.copy()
    df4=IMDb_ratings.copy()
    #Filtrage de l'année
    result=df3.loc[lambda df3:df3['year']==annee,:]

    #Filtrage genre on prend on compte le non respect des majuscules pour chaque genre
    genre1=genre.lower()  
    result["genre_low"]=result["genre"].str.lower()
    
    genre_liste=genre1.split(",")
    new_list=[]
    for element in genre_liste :
        new_list.append(element.strip())
    
    i=0 
    while i<len(new_list):
        result=result[result['genre_low'].str.contains(new_list[i])]
        i=i+1
    
    result2=result.copy()
    #On traite les cas différenment selon le nombre d'observations dans result2
    t1=result2.shape
    t=t1[0]
    
    #Erreutr de saisie
    if t==0:
        resulta="\n Aucun résultat pour les films répertoriés en "+str(annee)+" appartenant au genre "+genre+".\n"
        resulta=resulta+" Veuillez revoir la saisie et réécrire les genres an anglais séparées de virgules."

 # 2 - Extraction de l'information   
    elif t>=3 :
        #Récupération des notes
        final=pd.merge(result2,df4, how="left",on='imdb_title_id' )
    
        #Tri par note descending
        final=final.sort_values(by='avg_vote', ascending=False)
    
        #Recup des 3 premiers et classement
        top_3=final.iloc[0:3,:]
        classement=[1,2,3]
    
        pd.options.mode.chained_assignment = None #Evite les messages de warning
        top_3['Top_classement']=classement
    
        title=top_3['original_title'].reset_index(drop=True)
        note=top_3['avg_vote'].reset_index(drop=True)
        classe=top_3['Top_classement'].reset_index(drop=True)
    
        top_3=top_3.loc[:,lambda top_3: ['Top_classement','avg_vote','original_title']].to_string(index=False)
        
        #On stock toute l'information récupéré dans une variable char appelé result
        i=0
        resulta=""
        while i<3: 
            resulta=resulta+str(classe[i])+"- "+str(title[i])+", "+str(note[i])+"/10"+"\n"+"\n"
            i=i+1
        resulta="Top 3 des films ayant eu la meilleur note par les utilisateurs pour l'année "+str(annee)+" et le genre "+genre+":"+"\n"+"\n"+resulta
    
    else :
        #Récupération des notes
        final=pd.merge(result2,df4, how="left",on='imdb_title_id' )
    
        #Tri par note descending
        final=final.sort_values(by='avg_vote', ascending=False)
    
        #Recup du classement en fonction de la taille de result2
        top_3=final.iloc[0:t,:]
        classement=[]
        i=1
        while i<=t:
            classement.append(i)
            i=i+1
        pd.options.mode.chained_assignment = None #Evite les messages de warning
        top_3['Top_classement']=classement
    
        title=top_3['original_title'].reset_index(drop=True)
        note=top_3['avg_vote'].reset_index(drop=True)
        classe=top_3['Top_classement'].reset_index(drop=True)
    
        top_3=top_3.loc[:,lambda top_3: ['Top_classement','avg_vote','original_title']].to_string(index=False)
    
        #affichage resultat
        print("Top 3 des films ayant eu la meilleur note par les utilisateurs pour l'année",annee,"et le genre",genre,":" )
        i=0
        
  # 3 - On stock toute l'information récupéré dans une variable char appelé resulta
        resulta=""
        while i<t: 
            resulta=resulta+str(classe[i])+"- "+str(title[i])+", "+str(note[i])+"/10"+"\n"+"\n"
            i=i+1
        resulta="Top 3 des films ayant eu la meilleur note par les utilisateurs pour l'année "+str(annee)+" et le genre "+genre+":"+"\n"+"\n"+resulta
    return resulta



def get_commun_films(actor1,actor2):
 # 1 - Constitution de la dataframe pertinente
    df3=IMDb_movies.copy()
    #Filtrage film avec 1er acteur 
    df3=df3[df3['actors'].str.contains(actor1,na=False)]
    #Filtrage fim avec 2ème acteur
    df3= df3[df3['actors'].str.contains(actor2,na=False)]

 # 2 - Extraction de l'information    
    list_film=list(df3['original_title'])
    
    liste=""
    for element in list_film: 
        liste=liste+"- "+element+"\n"
    
 # 3- On stock toute l'information récupéré dans une variable char appelé result
    if liste=="" :
        result="Ces 2 acteurs n'ont pour l'instant joué dans aucun film ensemble."
    else:
        result="Ces 2 acteurs ont joué ensemble dans les films suivant :\n"+liste
    return result


