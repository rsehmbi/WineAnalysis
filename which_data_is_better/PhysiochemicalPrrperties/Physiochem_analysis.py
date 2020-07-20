import numpy as np
import pandas as pd

# Loading the data set in pandas Dataframe
red_wine_data = pd.read_csv("wineQualityReds.csv")
white_wine_data = pd.read_csv("wineQualityWhites.csv")

# **** Understanding the data set and their features ******
print("****** Welcome to Phsiochemical Analysis of Red and White Wine ****** \n")
# 1 What columns we have for the analysis

# Analyzing if both the data sets have same columns
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

# print("Description of acidity")
# print(red_wine_data['fixed.acidity'].describe())
# Cleaning the data

# print(red_wine_data)
# print(white_wine_data)
