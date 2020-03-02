import pandas as pd
import numpy as np

df = pd.read_csv('../../data/new_data/cleaned_movies.csv')

x = list(df['genre'].unique())
genres = []
for i in x:
    y = i.split(', ')
    for g in y:
        genres.append(g)
genres_set = set(genres)

def genre_determine(g, row):
    if g in row['genre']:
        return 1
    else:
        return 0

for genre in genres_set:
    col_name = 'is_' + genre
    df[col_name] = df.apply(lambda row: genre_determine(genre, row), axis = 1)

df.to_csv('../../data/New_Data/final.csv')
