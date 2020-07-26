import numpy as np
import pandas as pd


def load_wine_dataset():
    # Loading the data set in pandas Dataframe
    red_wine_data = pd.read_csv("cleanwineQualityReds.csv")
    white_wine_data = pd.read_csv("cleanwineQualityWhites.csv")
    return red_wine_data, white_wine_data


def main():
    redwine_df, whitewine_df = load_wine_dataset()
    print(redwine_df)


if __name__ == "__main__":
    main()
