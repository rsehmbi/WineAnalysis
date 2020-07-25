import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_wine_dataset():
    # Loading the data set in pandas Dataframe
    red_wine_data = pd.read_csv("wineQualityReds.csv")
    white_wine_data = pd.read_csv("wineQualityWhites.csv")
    return red_wine_data, white_wine_data


def cleaning_wine_dataset(red_wine_data, white_wine_data):
    # 1 What columns we have for the analysis
    # Analyzing if both the data-sets have same columns
    print("--- Column Names of Red Wine Data Set ----")
    for column_name in red_wine_data.columns:
        print(column_name, end=' ')

    print("\n")
    print("--- Column Names of White Wine Data Set ---")
    for column_name in white_wine_data.columns:
        print(column_name, end=' ')
    print("\n")

    # Cleaning 1: Cleaning the column names of the Data-Frames

    # Observed :
    # 1. Columns have names like citric.acid which can cause problems as sometimes dataframes are accessed with syntax like df.columnname
    # 2. Un-named column 0, We have a un-named column, looking deeper into the column by explicitly opening the CSV file

    # Changing the column names
    red_wine_data = red_wine_data.copy()
    red_wine_data.rename(columns={'Unnamed: 0': 'Wine_Number',
                                  'fixed.acidity': 'Fixed_Acidity',
                                  'volatile.acidity': 'Volatile_Acidity',
                                  'citric.acid': 'Citric_Acid',
                                  'residual.sugar': 'Residual_Sugar',
                                  'chlorides': 'Chlorides',
                                  'free.sulfur.dioxide': 'Free_Sulphur_Dioxide',
                                  'total.sulfur.dioxide': 'Total_Sulphur_Dioxide',
                                  'density': 'Density',
                                  'sulphates': 'Sulphates',
                                  'alcohol': 'Alcohol',
                                  'quality': 'Quality'}, inplace=True)

    white_wine_data = white_wine_data.copy()
    white_wine_data.rename(columns={'Unnamed: 0': 'Wine_Number',
                                    'fixed.acidity': 'Fixed_Acidity',
                                    'volatile.acidity': 'Volatile_Acidity',
                                    'citric.acid': 'Citric_Acid',
                                    'residual.sugar': 'Residual_Sugar',
                                    'chlorides': 'Chlorides',
                                    'free.sulfur.dioxide': 'Free_Sulphur_Dioxide',
                                    'total.sulfur.dioxide': 'Total_Sulphur_Dioxide',
                                    'density': 'Density',
                                    'sulphates': 'Sulphates',
                                    'alcohol': 'Alcohol',
                                    'quality': 'Quality'}, inplace=True)

    print("--- Modified Column Names of Red Wine Data Set ----")
    for column_name in red_wine_data.columns:
        print(column_name, end=' ')

    print("\n")
    print("--- Modified Column Names of White Wine Data Set ---")
    for column_name in white_wine_data.columns:
        print(column_name, end=' ')

    print("\n")
    return red_wine_data, white_wine_data


def scatter_plot(red_wine_data, white_wine_data):
    # Next Step
    # Looking at the scatter plot of the data set to observe the general trends and see if we have any outliers
    # Plots for Red Wine data set and description of every column of dataframe
    print("-------------------Description of Read Wine Data Set-----------------------------\n")
    for column_name in red_wine_data.columns:
        print(column_name)
        print(red_wine_data[column_name].describe())
        plt.scatter(red_wine_data.Wine_Number,
                    red_wine_data[column_name], alpha=0.5)
        plt.xlabel("Wine Number")
        plt.ylabel(column_name)
        plt.savefig('RedWineScatterPlots/{}.png'.format(column_name))
        # Clears the old plot so plt don't overwrite
        plt.clf()
        print('\n')

    print('\n')
    # Plots for White Wine data set and description of every column of dataframe
    print("---------------------Description of White Wine Data Set--------------------------\n")
    for column_name in white_wine_data.columns:
        print(column_name)
        print(white_wine_data[column_name].describe())
        plt.scatter(white_wine_data.Wine_Number,
                    white_wine_data[column_name], alpha=0.5)
        plt.xlabel("Wine Number")
        plt.ylabel(column_name)
        plt.savefig('WhiteWineScatterPlots/{}.png'.format(column_name))
        # Clears the old plot so plt don't overwrite
        plt.clf()
        print('\n')

    # print(red_wine_data)
    # print(white_wine_data)


def remove_whiteSO2_outlier(white_wine_df):
    wine_df = white_wine_df[white_wine_df['Total_Sulphur_Dioxide'] < 400]
    return wine_df


def remove_redSO2_outlier(red_wine_df):
    wine_df = red_wine_df[red_wine_df['Total_Sulphur_Dioxide'] < 250]
    return wine_df


def main():
    # **** Understanding the data set and their features ******
    print("****** Welcome to Physiochemical Analysis of Red and White Wine ****** \n")

    redwine_df, whitewine_df = load_wine_dataset()

    clean_redwine_df, clean_whitewine_df = cleaning_wine_dataset(
        redwine_df, whitewine_df)

    scatter_plot(clean_redwine_df, clean_whitewine_df)

    clean_redwine_df = remove_redSO2_outlier(clean_redwine_df)
    clean_whitewine_df = remove_whiteSO2_outlier(clean_whitewine_df)


if __name__ == "__main__":
    main()
