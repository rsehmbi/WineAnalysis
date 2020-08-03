import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


seaborn.set()


def loaddatasets(filepath):
    wine_dataset = pd.read_csv(f'{filepath}/DataSet.csv')
    return wine_dataset


def printbarplot(filepath, df):
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

    print(grouped_countries_points)
    print(grouped_countries_price)


def Analysis1(df):
    # Since there are limited number of countries, let's look at avg of each country's points and plot a graph for visualization
    printbarplot("hello", df)


def Analysis2(df):
    print(df)


def main():
    print("****** Welcome to Location Analysis of Wine ****** \n")
    wine_dataset_without_region = loaddatasets("DataWithoutRegion2")
    wine_dataset_with_region = loaddatasets("DatawithRegion2")

    Analyze_withoutRegion = Analysis1(wine_dataset_without_region)
    Analyze_withRegion = Analysis2(wine_dataset_with_region)


if __name__ == "__main__":
    main()
