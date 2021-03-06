import pandas as pd
import numpy as np

# To display all the columns of the dataframe
pd.options.display.max_columns = None


def loaddatasets():
    wine_dataset = pd.read_csv("winemag-data-130k-v2.csv")
    return wine_dataset


def printdfInfo(df):
    print(df.columns)
    print(df.info())


def dftocsv(filepath, df):
    df = df.to_csv(f'{filepath}/DataSet.csv', index=False,)


def dropNaValues(df):
    df = df.dropna()
    return df


def dropUnwantedColumn(df):
    return df.drop(columns=['title', 'description', 'taster_name', 'taster_twitter_handle'])


def describepricepoints(df):
    print(df.price.describe())
    print(df.points.describe())


def dropRegion2column(df):
    return df.drop(columns=['region_2'])


def main():
    print("****** Welcome to Location Analysis of Wine ****** \n")
    wine_data_set = loaddatasets()

    # The dataset is really large with large number of columns
    # Printing only the columns
    printdfInfo(wine_data_set)

    # Dataset have uneven number of columns.
    # Data is missing from the columns

    # With the kind of question we are asking we are more interested in predicting the points from georgraphics of the wine
    # Not from the descriotion of comments made by the sommelier
    # Its safe to remove the description column
    wine_data_set = dropUnwantedColumn(wine_data_set)

    # Can't do imputation on prices as one wine can be really cheap and other can be really pricy. This can add bias in results.
    # Region 2 have approximately half the number of rows as compared to any other column.
    #
    # Question to ask should be drop the Region2 column and deal with all the other values
    # or should we drop around 50,000 rows and deal with the data
    # or we can do both.. ?
    Clean_data_1 = dropNaValues(wine_data_set)
    dftocsv("DatawithRegion2", Clean_data_1)
    # Interesting finding, all the datasets now have country = US.
    # Verify if that's true
    grouped_country = Clean_data_1.groupby("country")
    grouped_country = grouped_country.agg({"country": "nunique"})
    print("The country after dropping Region2")
    print(grouped_country)
    # Yes, there is only one country, can do dropna on all. Result would be only from US

    # Drop Region 2 column and then drop NA values
    Clean_data_2 = dropRegion2column(wine_data_set)
    Clean_data_2 = dropNaValues(Clean_data_2)
    dftocsv("DataWithoutRegion2", Clean_data_2)

    grouped_country_2 = Clean_data_2.groupby("country")
    grouped_country_2 = grouped_country_2.agg({"country": "nunique"})
    print(grouped_country_2)

    # The only numerical values we have for dataset is points and price.
    # Describing that information
    # Checking the if the points are greater >100 and less <0 to check for the outliers.
    # Checking the price as well to check for outliers since the price can't be less than 0
    describepricepoints(Clean_data_1)
    describepricepoints(Clean_data_2)


if __name__ == "__main__":
    main()
