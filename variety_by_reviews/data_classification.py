from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB




def split_data(X, y):
    X_train, X_valid, y_train, y_valid = train_test_split(X, y)
    return X_train, X_valid, y_train, y_valid

def get_mnb_model():
    model = make_pipeline(
        CountVectorizer(stop_words='english'),
        MultinomialNB()
    )
    return model

def classify_data(data):
    X_train, X_valid, y_train, y_valid = split_data(data['description'], data['variety'])
    mnb_model = get_mnb_model()
    mnb_model.fit(X_train, y_train)
    print("train score = {}".format(mnb_model.score(X_train, y_train)))
    print("valid score = {}".format(mnb_model.score(X_valid, y_valid)))

    # df = pd.DataFrame({'truth': y_valid, 'prediction': prediction})
    # print(df[df['truth'] != df['prediction']])
