import numpy as np
import pandas as pd
# from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer


def get_description(data):
    data = data[['variety', 'description']].copy()
    return data

def get_lowercase(data):
    data = data.str.lower()
    return data

def remove_num_punctuation(data):
    data = data.str.replace(r'\d+', '')
    data = data.str.replace(r'[^\w\s]', '')
    return data

def get_popular_variety(data):
    variety = data.value_counts()[:30]
    return variety

def join_variety(data, variety):
    variety = pd.DataFrame({'variety': variety.index.values})
    joined = pd.merge(data, variety, on='variety')
    return joined

def agg_description(data):
    data = data.groupby(['variety'])['description'].apply(' '.join).reset_index()
    return data


def clean_description(data):
    data = get_description(data)
    data['description'] = get_lowercase(data['description'])
    data['description'] = remove_num_punctuation(data['description'])
    # print(data)
    variety = get_popular_variety(data['variety'])
    data = join_variety(data, variety)
    # print(data)
    data = agg_description(data)
    print(data)
    data['description'] = data['description'].apply(remove_description)
