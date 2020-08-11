import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords



def agg_description(data):
    data = data.groupby(['variety'])['description'].apply(' '.join).reset_index()
    return data

def get_count_table(data):
    cv = CountVectorizer(stop_words=stopwords.words('english'))
    description_cv = cv.fit_transform(data['description'])
    df = pd.DataFrame(description_cv.toarray(), columns=cv.get_feature_names())
    df.index = data['variety'].values
    return df

def get_top_twenty_words_helper(data):
    twenty = data.sort_values(ascending=False).head(30)
    return twenty

def get_top_twenty_words(data):
    twenty = data.apply(get_top_twenty_words_helper, axis=0)
    return twenty

def explore_data(data):
    corpus = agg_description(data)
    corpus_count = get_count_table(corpus)
    top_words = get_top_twenty_words(corpus_count.transpose())
    # print(top_words['Bordeaux-style Red Blend'].unique())
