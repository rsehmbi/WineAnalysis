import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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


def main():
    redwine_df, whitewine_df = load_wine_dataset()
    # Plot the histograms
    plot_histograms(redwine_df, whitewine_df)


if __name__ == "__main__":
    main()
