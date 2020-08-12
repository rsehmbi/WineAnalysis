import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import re



def agg_description(data):
    data = data.groupby(['variety'])['description'].apply(' '.join).reset_index()
    return data

def get_count_table(data):
    cv = CountVectorizer(stop_words=stopwords.words('english'))
    description_cv = cv.fit_transform(data['description'])
    df = pd.DataFrame(description_cv.toarray(), columns=cv.get_feature_names())
    df.index = data['variety'].values
    return df

def get_top_thirty_words(data):
    thirty = data.apply(lambda x: x.sort_values(ascending=False).head(30), axis=0)
    return thirty

def get_words_helper(data):
    count = data.dropna().sort_values(ascending=False)
    zipped = list(zip(count.index, count))
    return zipped

def get_words(data):
    words = data.apply(get_words_helper, axis=0)
    words = pd.DataFrame({'Bordeaux-style Red Blend':words[0], 'Cabernet Sauvignon':words[1], 'Chardonnay':words[2], 'Merlot':words[3],
            'Pinot Noir':words[4], 'Red Blend':words[5], 'Riesling':words[6], 'Rosé':words[7], 'Sauvignon Blanc':words[8], 'Syrah':words[9]})
    return words

def get_freq_dict(data):
    freq_dict = {}
    for column in data.columns:
        words = data[column].sort_values(ascending=False).head(60)
        freq_dict[column] = list(zip(words.index, words.values))
    return freq_dict

def plot_wordcloud(data):
    print("Creating word cloud plots...", end='')
    wc = WordCloud(background_color='black', colormap='Set1', max_font_size=100, random_state=353)
    plot_id = 1
    keys = list(data.keys())
    plt.figure(figsize=(10,12))
    for k in keys:
        wc.generate_from_frequencies(dict(data[k]))
        plt.subplot(5, 2, plot_id)
        plot_id += 1
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title(k)
    # plt.show()
    plt.savefig('output/wordcloud_by_variety.png')
    print("  done")

def plot_bar(data):
    print("Creating barplots...", end='')
    sns.set()
    fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(16,13))
    plt.subplots_adjust(hspace=0.9)
    keys = list(data.keys())
    k = 0
    for r in axes:
        for c in r:
            x = [x[0] for x in data[keys[k]]]
            ax = sns.barplot(x, [x[1] for x in data[keys[k]]], ax=c)
            ax.set_title(keys[k])
            ax.set_xticklabels(x, rotation=90, fontsize=8)
            k += 1
    # plt.show()
    plt.savefig('output/barplots_by_variety.png')
    print("  done")

def explore_data(data):
    corpus = agg_description(data)
    corpus_count = get_count_table(corpus)
    # thirty = get_top_thirty_words(corpus_count.transpose())
    # words = get_words(thirty)
    freq_list = get_freq_dict(corpus_count.transpose())
    plot_wordcloud(freq_list)
    plot_bar(freq_list)



