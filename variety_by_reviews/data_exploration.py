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

def get_top_twenty_words(data):
    twenty = data.apply(lambda x: x.sort_values(ascending=False).head(30), axis=0)
    return twenty

def get_words_helper(data):
    count = data.dropna().sort_values(ascending=False)
    zipped = list(zip(count.index, count))
    return zipped

def get_words(data):
    words = data.apply(get_words_helper, axis=0)
    words = pd.DataFrame({'Bordeaux-style Red Blend':words[0], 'Cabernet Sauvignon':words[1], 'Chardonnay':words[2], 'Merlot':words[3],
            'Pinot Noir':words[4], 'Red Blend':words[5], 'Riesling':words[6], 'Rosé':words[7], 'Sauvignon Blanc':words[8], 'Syrah:':words[9]})
    return words

def explore_data(data):
    corpus = agg_description(data)
    corpus_count = get_count_table(corpus)
    twenty = get_top_twenty_words(corpus_count.transpose())
    print(twenty)
    words = get_words(twenty)
    print(words)
