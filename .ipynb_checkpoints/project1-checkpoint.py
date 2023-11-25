import pandas as pd
import numpy as np
import ast

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')
movies.shape,credits.shape
movies=movies.merge(credits,on='title',how='inner')

movies= movies[['movie_id','title','keywords','overview','genres','cast','crew']]
movies.head(2)
movies['genres'][0]

def convert(object):
    L = []
    for i in ast.literal_eval(object):
        L.append(i['name'])
    return L
movies['genres'].apply(convert)


movies['genres']=movies['genres'].apply(convert)
movies.head(2)


movies['keywords'].apply(convert)
movies.head(2)



def convert(object):
    L = []
    counter = 0
    for i in ast.literal_eval(object):
        L.append(i['name'])
        counter+=1
        if counter ==3:
            break
    return L


movies['cast'].apply(convert)
movies['cast']=movies['cast'].apply(convert)
movies.head(2)


def convert_crew(object):
    L = []
    for i in ast.literal_eval(object):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L

movies['crew'].apply(convert_crew)
movies['crew']=movies['crew'].apply(convert_crew)
movies.head(2)



