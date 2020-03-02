import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

df = pd.read_csv('../../data/new_data/final.csv')

punct_to_remove = string.punctuation
stop_words = set(stopwords.words('english'))
def remove_punctuation(text):
    return text.translate(str.maketrans('','', punct_to_remove))
def remove_stopwords(text):
    return ' '.join([word for word in str(text).split() if word not in stop_words])
df['description'] = df['description'].apply(lambda text: remove_stopwords(text))
df['title'] = df['title'].apply(lambda text: remove_punctuation(text))
df['director'] = df['director'].apply(lambda text: remove_punctuation(text))
df['description'] = df['description'].apply(lambda text: remove_punctuation(text))
df['title'] =df['title'].astype(str)
df['title'] =df['title'].str.lower()
df['description'] = df['description'].astype(str)
df['description'] = df['description'].str.lower()
df['director'] = df['director'].astype(str)
df['director'] = df['director'].str.lower()
df['text'] = df['title'] + ' ' + df['director'] + ' ' + df['description']
train_data, test_data = train_test_split(df, test_size =0.2, random_state=1)

vectorizer = CountVectorizer(ngram_range=(1, 2))
counts = vectorizer.fit_transform(df['text'].values)
classifier = MultinomialNB()
targets = df['profitable'].values
classifier.fit(counts, targets)


test = df['text']
example_counts = vectorizer.transform(test)
predictions = classifier.predict(example_counts)

df_nb = df.copy()
df_nb['nb_prediction'] = predictions

df_nb.to_csv('../../data/new_data/nb.csv')