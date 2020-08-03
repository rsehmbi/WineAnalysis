import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier


def load_wine_dataset():
    # Loading the data set in pandas Dataframe
    red_wine_data = pd.read_csv("cleanwineQualityReds.csv")
    white_wine_data = pd.read_csv("cleanwineQualityWhites.csv")
    return red_wine_data, white_wine_data


def plot_histograms(redwine_df, whitewine_df):
    # Observing the data using histogram for normality
    # Checking for normality as GaussianNB ML technique requires data to be normal
    for column in redwine_df.columns:
        plt.hist(redwine_df[column])
        plt.savefig('RedWineHistogram/{}.png'.format(column))
        plt.clf()

    for column in whitewine_df.columns:
        plt.hist(whitewine_df[column])
        plt.savefig('WhiteWineHistogram/{}.png'.format(column))
        plt.clf()


def GNB(wine_dataframe):
    y = wine_dataframe.Quality.values
    wine_df = wine_dataframe.drop(columns=['Quality'])

    X = wine_df.values

    X_train, X_valid, y_train, y_valid = train_test_split(X, y)

    model = make_pipeline(
        StandardScaler(),
        GaussianNB()
    )

    model.fit(X_train, y_train)
    print(model.score(X_train, y_train))
    print(model.score(X_valid, y_valid))


def GBC(wine_dataframe):
    y = wine_dataframe.Quality.values

    wine_dataframe.drop(columns=['Quality'], inplace=True)

    X = wine_dataframe.values

    X_train, X_valid, y_train, y_valid = train_test_split(X, y)

    model = make_pipeline(
        StandardScaler(),
        GradientBoostingClassifier(n_estimators=500,
                                   max_depth=10, min_samples_leaf=1),
    )

    model.fit(X_train, y_train)
    print(model.score(X_train, y_train))
    print(model.score(X_valid, y_valid))


def main():
    redwine_df, whitewine_df = load_wine_dataset()
    # Plot the histograms
    plot_histograms(redwine_df, whitewine_df)

    # GNB(redwine_df) # Gives the accuracy score of 56%

    # Gives the accuracy score of 70%

    GBC(redwine_df)  # 0.68
    GBC(whitewine_df)  # 0.7001
    # Analyzing histogram gives a hint
    # Can we compare alcohols to chlorides?
    # or pH to Sulphates or SO2

    # Scale the data using Standard Scalar before applying the GaussianNB and other ML technique.

    # We want to train the data to predict the ratings


if __name__ == "__main__":
    main()
