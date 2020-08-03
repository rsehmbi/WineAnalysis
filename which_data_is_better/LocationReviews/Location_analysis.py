import numpy as np
import pandas as pd

# To display all the columns of the dataframe
pd.options.display.max_columns = None


def loaddatasets():
    wine_dataset = pd.read_csv("winemag-data-130k-v2.csv")
    return wine_dataset


def printdfInfo(df):
    print(df.columns)
    print(df.info())


def dropNaValues(df):
    return df.dropna(how='all')


def main():
    print("****** Welcome to Location Analysis of Wine ****** \n")
    wine_data_set = loaddatasets()

    # The dataset is really large with large number of columns
    # Printing only the columns
    printdfInfo(wine_data_set)

    # Dataset have uneven number of columns.
    # Data is missing from the columns

    # Can't do imputation on prices as one wine can be really cheap and other can be really pricy. This can add bias in results.
    wine_data_set = dropNaValues(wine_data_set)
    printdfInfo(wine_data_set)


if __name__ == "__main__":
    main()
