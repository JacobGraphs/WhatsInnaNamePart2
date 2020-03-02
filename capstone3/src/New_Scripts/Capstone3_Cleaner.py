import pandas as pd
import numpy as np

movies = pd.read_csv('/Users/jacobtryba/DSI/assignments/capstone2/data/imdb-extensive-dataset/IMDb movies.csv')
movies_subset = ['description','director','genre','imdb_title_id', 'title', 'year','duration', 'country','budget', 'usa_gross_income', 'worlwide_gross_income']
movies_subbed = movies[movies_subset]
movies_current = movies_subbed
movies_current_usa = movies_current.query('country == "USA"')
movies_current_usa_nonnull_ugi = movies_current_usa[(movies_current_usa.usa_gross_income.notnull())]
movies_current_usa_nonnull_ugi_budget = movies_current_usa_nonnull_ugi[(movies_current_usa_nonnull_ugi.budget.notnull())]
final_set = movies_current_usa_nonnull_ugi_budget.sort_values('year', ascending = True)
final_set['budget'] = final_set['budget'].str.replace('$', '')
final_set['budget'] = final_set['budget'].str.replace('$ ', '')
final_set['budget'] = final_set['budget'].str.replace('GBP ', '')
final_set['budget'] = final_set['budget'].str.replace('AUD ', '')
final_set['budget'] = final_set['budget'].str.replace('EUR ', '')
final_set['budget'] = final_set['budget'].str.replace('ESP ', '')
final_set['budget'] = final_set['budget'].str.replace('CAD ', '')
final_set['usa_gross_income'] = final_set['usa_gross_income'].str.replace('$ ', '')
final_set['usa_gross_income'] = final_set['usa_gross_income'].str.replace('$', '').astype('int')
final_set['worlwide_gross_income_gross_income'] = final_set['worlwide_gross_income'].str.replace('$ ', '')
final_set['worlwide_gross_income'] = final_set['worlwide_gross_income'].str.replace('$', '').astype('int')
final_set['international_gross_income'] = (final_set['worlwide_gross_income'] - final_set['usa_gross_income'])
final_set['returns'] = (final_set['worlwide_gross_income'] - final_set['budget'].astype('int'))
final_set['profitable'] = [1 if x > 0 else 0 for x in final_set['returns']]

subset = ['title', 'director', 'description', 'duration', 'year', 'budget', 'genre', 'profitable']
cleaned_data = final_set[subset]

cleaned_data.to_csv('../../data/New_Data/cleaned_movies.csv')