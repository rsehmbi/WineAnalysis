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


def printbarplot(wine_df):
    grouped_countries_points = wine_df.groupby(
        ["country"], as_index=False)['points'].mean()
    grouped_countries_price = wine_df.groupby(
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


def DecisionTree(X_train, y_train, X_valid, y_valid):
    model = DecisionTreeClassifier(max_depth=30)
    model.fit(X_train, y_train)
    print("Score with Decision Tree Classifier" +
          str(model.score(X_valid, y_valid)))


def GB(X_train, y_train, X_valid, y_valid):
    modelGB = GradientBoostingClassifier(n_estimators=50,
                                         max_depth=50, min_samples_leaf=0.1)
    modelGB.fit(X_train, y_train)
    print("Score with Gradient Boosting"+str(modelGB.score(X_valid, y_valid)))


def KNN(X_train, y_train, X_valid, y_valid):
    modelKNN = KNeighborsClassifier(n_neighbors=1)
    modelKNN.fit(X_train, y_train)
    print(modelKNN.score(X_valid, y_valid))


def WithoutRegion2Analysis(wine_df):
    # Since there are limited number of countries, let's look at avg of each country's points and plot a graph for visualization
    printbarplot(wine_df)

    country_, country_unique_values = pd.factorize(wine_df.loc[:, 'country'])
    designation_, country_unique_values = pd.factorize(
        wine_df.loc[:, 'designation'])
    price_, price_unique_values = pd.factorize(wine_df.loc[:, 'price'])
    province_, province_unique_values = pd.factorize(
        wine_df.loc[:, 'province'])
    region_1_, region_unique_values = pd.factorize(wine_df.loc[:, 'region_1'])
    winery_, winery_unique_values = pd.factorize(
        wine_df.loc[:, 'winery'])
    points_, points_unique_values = pd.factorize(
        wine_df.loc[:, 'points'])

    wine_df['country_'] = country_
    wine_df['designation_'] = designation_
    wine_df['price_'] = price_
    wine_df['province_'] = province_
    wine_df['winery_'] = winery_
    wine_df['region_'] = region_1_
    wine_df['points_'] = points_

    X = wine_df[['country_', 'designation_',
                 'province_', 'region_', 'winery_']].values
    y = wine_df['points_'].values

    X_train, X_valid, y_train, y_valid = train_test_split(X, y)

    DecisionTree(X_train, X_valid, y_train, y_valid)
    GB(X_train, X_valid, y_train, y_valid)
    KNN(X_train, X_valid, y_train, y_valid)


def WithRegionAnalysis(wine_df):
    country_, country_unique_values = pd.factorize(wine_df.loc[:, 'country'])
    designation_, country_unique_values = pd.factorize(
        wine_df.loc[:, 'designation'])
    price_, price_unique_values = pd.factorize(wine_df.loc[:, 'price'])
    province_, province_unique_values = pd.factorize(
        wine_df.loc[:, 'province'])
    region_1_, region_unique_values = pd.factorize(wine_df.loc[:, 'region_1'])
    region_2_, region_unique_values = pd.factorize(wine_df.loc[:, 'region_2'])
    winery_, winery_unique_values = pd.factorize(
        wine_df.loc[:, 'winery'])
    points_, points_unique_values = pd.factorize(wine_df.loc[:, 'points'])

    wine_df['country_'] = country_
    wine_df['designation_'] = designation_
    wine_df['price_'] = price_
    wine_df['province_'] = province_
    wine_df['winery_'] = winery_
    wine_df['region1_'] = region_1_
    wine_df['region2_'] = region_2_
    wine_df['points_'] = points_

    X = wine_df[['country_', 'designation_',
                 'province_', 'region1_', 'region2_', 'winery_']].values
    y = wine_df['points_'].values

    X_train, X_valid, y_train, y_valid = train_test_split(X, y)

    DecisionTree(X_train, X_valid, y_train, y_valid)
    GB(X_train, X_valid, y_train, y_valid)
    KNN(X_train, X_valid, y_train, y_valid)


def main():
    print("****** Welcome to Location Analysis of Wine ****** \n")
    wine_dataset_without_region = loaddatasets("DataWithoutRegion2")
    wine_dataset_with_region = loaddatasets("DatawithRegion2")

    Analyze_withoutRegion = WithoutRegion2Analysis(wine_dataset_without_region)
    Analyze_withRegion = WithRegionAnalysis(wine_dataset_with_region)


if __name__ == "__main__":
    main()
