import pandas as pd


def get_description(data):
    data = data[['variety', 'description']].copy()
    return data

def get_lowercase(data):
    data = data.str.lower()
    return data

def remove_num_punctuation(data):
    data = data.str.replace(r'\d+', '')
    data = data.str.replace(r'(wine|flavor|flavors|drink|finish|shows)', '')
    data = data.str.replace(r'(riesling|pinor|noir|cabernet|sauvignon|chardonnary|merlot|blanc|bordeaux|bordeaux-style|rosé|syrah)', '')
    data = data.str.replace(r'[^\w\s]', '')
    return data

def get_popular_variety(data):
    variety = data.value_counts()[:10]
    return variety

def join_variety(data, variety):
    variety = pd.DataFrame({'variety': variety.index.values})
    joined = pd.merge(data, variety, on='variety')
    return joined

def clean_description(data):
    data = get_description(data)
    data['description'] = get_lowercase(data['description'])
    data['description'] = remove_num_punctuation(data['description'])
    variety = get_popular_variety(data['variety'])
    data = join_variety(data, variety)
    varieties = pd.Series(data['variety'].unique())
    print("The 10 varieties of wine to be classified are:\n{}".format(varieties.to_string(index=False)))
    return data
