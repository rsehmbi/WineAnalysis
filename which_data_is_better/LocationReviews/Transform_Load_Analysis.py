import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
pd.options.display.max_columns = None

seaborn.set()


def loaddatasets(filepath):
    wine_dataset = pd.read_csv(f'{filepath}/DataSet.csv')
    return wine_dataset


def printbarplot(df):
    grouped_countries_points = df.groupby(
        ["country"], as_index=False)['points'].mean()
    grouped_countries_price = df.groupby(
        ["country"], as_index=False)['price'].mean()

    plt.barh(grouped_countries_points.points,
             grouped_countries_points.country, color=(0.2, 0.4, 0.6, 0.6))
    plt.xlabel('Country', fontsize=5)
    plt.ylabel('Points(from 100)', fontsize=5)
    plt.title('Country VS Points')
    plt.savefig('BarPlotPoints/points.png')
    plt.clf()

    plt.barh(grouped_countries_price.price,
             grouped_countries_price.country, color=(0.2, 0.4, 0.6, 0.6))
    plt.xlabel('Country', fontsize=5)
    plt.ylabel('Price', fontsize=5)
    plt.title('Country VS Price')
    plt.savefig('BarPlotPrice/price.png')
    plt.clf()


def Analysis1(df):
    # Since there are limited number of countries, let's look at avg of each country's points and plot a graph for visualization
    printbarplot(df)

    country_, country_unique_values = pd.factorize(df.loc[:, 'country'])
    designation_, country_unique_values = pd.factorize(
        df.loc[:, 'designation'])
    price_, price_unique_values = pd.factorize(df.loc[:, 'price'])
    province_, province_unique_values = pd.factorize(
        df.loc[:, 'province'])
    region_1_, region_unique_values = pd.factorize(df.loc[:, 'region_1'])
    winery_, winery_unique_values = pd.factorize(
        df.loc[:, 'winery'])

    df['country_'] = country_
    df['designation_'] = designation_
    df['price_'] = price_
    df['province_'] = province_
    df['winery_'] = winery_
    df['region_'] = region_1_

    X = df[['country_', 'designation_', 'province_', 'region_', 'winery_']].values

    points_, points_unique_values = pd.factorize(
        df.loc[:, 'points'])
    df['points_'] = points_
    y = df['points_'].values

    X_train, X_valid, y_train, y_valid = train_test_split(X, y)

    model = DecisionTreeClassifier(max_depth=30)
    model.fit(X_train, y_train)
    print(model.score(X_train, y_train))
    print(model.score(X_valid, y_valid))

    modelGB = GradientBoostingClassifier(n_estimators=50,
                                         max_depth=50, min_samples_leaf=0.1)
    modelGB.fit(X_train, y_train)
    print(modelGB.score(X_train, y_train))
    print(modelGB.score(X_valid, y_valid))

    modelRF = RandomForestClassifier(n_estimators=100,
                                     max_depth=30, min_samples_leaf=30)

    modelRF.fit(X_train, y_train)
    print(modelRF.score(X_train, y_train))
    print(modelRF.score(X_valid, y_valid))

    SVC_model = make_pipeline(
        StandardScaler(),
        SVC(kernel='linear', C=2.0)
    )

    SVC_model.fit(X_train, y_train)
    print(SVC_model.score(X_valid, y_valid))

    modelKNN = KNeighborsClassifier(n_neighbors=1)
    modelKNN.fit(X_train, y_train)
    print(modelKNN.score(X_valid, y_valid))


def Analysis2(df):
    country_, country_unique_values = pd.factorize(df.loc[:, 'country'])
    designation_, country_unique_values = pd.factorize(
        df.loc[:, 'designation'])
    price_, price_unique_values = pd.factorize(df.loc[:, 'price'])
    province_, province_unique_values = pd.factorize(
        df.loc[:, 'province'])
    region_1_, region_unique_values = pd.factorize(df.loc[:, 'region_1'])
    region_2_, region_unique_values = pd.factorize(df.loc[:, 'region_2'])
    winery_, winery_unique_values = pd.factorize(
        df.loc[:, 'winery'])

    df['country_'] = country_
    df['designation_'] = designation_
    df['price_'] = price_
    df['province_'] = province_
    df['winery_'] = winery_
    df['region1_'] = region_1_
    df['region2_'] = region_2_

    X = df[['country_', 'designation_',
            'province_', 'region1_', 'region2_', 'winery_']].values

    points_, points_unique_values = pd.factorize(df.loc[:, 'points'])
    df['points_'] = points_
    y = df['points_'].values

    X_train, X_valid, y_train, y_valid = train_test_split(X, y)

    model = DecisionTreeClassifier(max_depth=30)
    model.fit(X_train, y_train)
    print(model.score(X_train, y_train))
    print(model.score(X_valid, y_valid))

    modelGB = GradientBoostingClassifier(n_estimators=50,
                                         max_depth=50, min_samples_leaf=0.1)
    modelGB.fit(X_train, y_train)
    print(modelGB.score(X_train, y_train))
    print(modelGB.score(X_valid, y_valid))

    modelRF = RandomForestClassifier(n_estimators=100,
                                     max_depth=30, min_samples_leaf=30)

    modelRF.fit(X_train, y_train)
    print(modelRF.score(X_train, y_train))
    print(modelRF.score(X_valid, y_valid))

    SVC_model = make_pipeline(
        StandardScaler(),
        SVC(kernel='linear', C=2.0)
    )

    SVC_model.fit(X_train, y_train)
    print(SVC_model.score(X_valid, y_valid))

    modelKNN = KNeighborsClassifier(n_neighbors=1)
    modelKNN.fit(X_train, y_train)
    print(modelKNN.score(X_valid, y_valid))


def main():
    print("****** Welcome to Location Analysis of Wine ****** \n")
    wine_dataset_without_region = loaddatasets("DataWithoutRegion2")
    wine_dataset_with_region = loaddatasets("DatawithRegion2")

    Analyze_withoutRegion = Analysis1(wine_dataset_without_region)
    Analyze_withRegion = Analysis2(wine_dataset_with_region)


if __name__ == "__main__":
    main()
