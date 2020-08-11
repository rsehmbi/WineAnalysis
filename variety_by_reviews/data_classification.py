import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.svm import SVC
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.neural_network import MLPClassifier


def split_data(X, y):
    X_train, X_valid, y_train, y_valid = train_test_split(X, y)
    return X_train, X_valid, y_train, y_valid

def get_mnb_model():
    model = make_pipeline(
        CountVectorizer(stop_words=stopwords.words('english')),
        MultinomialNB()
    )
    return model

def get_logisticRegr_model():
    model = make_pipeline(
        CountVectorizer(stop_words=stopwords.words('english')),
        LogisticRegression(solver='saga', max_iter=300)
    )
    return model

def get_mlpclf_model():
    model = make_pipeline(
        CountVectorizer(stop_words=stopwords.words('english')),
        MLPClassifier(solver='lbfgs', hidden_layer_sizes=(4,3), activation='logistic')
    )
    return model

def get_svc_model():
    model = make_pipeline(
        CountVectorizer(stop_words=stopwords.words('english')),
        SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
    )
    return model

def get_randomforest_model():
    model = make_pipeline(
        CountVectorizer(stop_words=stopwords.words('english')),
        RandomForestClassifier(n_estimators=500, max_depth=13, min_samples_leaf=3)
    )
    return model

def classify_data(data):
    print("====> Running classification, this may take a while... <====")
    X_train, X_valid, y_train, y_valid = split_data(data['description'], data['variety'])
    logisticregr_model = get_logisticRegr_model()
    logisticregr_model.fit(X_train, y_train)
    # print("LogisticRegression train score = {}".format(logisticregr_model.score(X_train, y_train)))
    print("Validation score = {}".format(logisticregr_model.score(X_valid, y_valid)))


    # prediction = logisticregr_model.predict(X_valid)
    # df = pd.DataFrame({'truth': y_valid, 'prediction': prediction})
    # print(df[df['truth'] != df['prediction']])
