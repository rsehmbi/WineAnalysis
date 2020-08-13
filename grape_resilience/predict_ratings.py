#!/usr/bin/env python3
import re
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from internal_error import InternalError, print_error
from scipy import stats

def extract_vintage(data):
    split_vintage = data["title"].str.split(pat = '(\d{4})|(N.V)', expand = True)
    data["wine"] = split_vintage[0].astype(np.str_)
    data["vintage"] = split_vintage[1].astype(np.float)
    data = data.drop(columns = ["title"])
    data = data.dropna()
    return data

def extract_country(data):
    split_region = data["region"].str.split(pat = '·', expand = True)
    data["country"] = split_region[0]
    data["region"] = split_region[1]
    return data


def split(data, col, pattern, new_col1, sec1, type1, new_col2, sec2, type2, drop_col = True, drop_na = True):
    split = data[col].str.split(pat = pattern, expand = True)
    data[new_col1] = split[sec1].astype(type1)
    data[new_col2] = split[sec2].astype(type2)
    if drop_col:
        data = data.drop(columns = [col])
    if drop_na:
        data = data.dropna()
    return data



def scatter(data, x, y, n = ""):
    rcParams.update({'figure.autolayout': True})
    plt.figure(figsize = (30, 10))
    plt.scatter(data[x], data[y])
    title = n + " " + x + " vs. " + y
    plt.title(title)
    plt.xlabel(x)
    plt.xticks(rotation = 90)
    plt.ylabel(y)
    path = "figures/scatter/" + n + "_" + x + "_" + y
    plt.savefig(path)

def boxplot(data, x, n = ""):
    plt.boxplot(data[x], vert = False)
    title = n + " " + x + " boxplot"
    plt.title(title)
    plt.xlabel(x)
    plt.yticks([])
    path = "figures/boxplots/" + n + "_" + x
    plt.savefig(path)

def histogram(data, x, n = ""):
    plt.hist(data[x])
    title = n + " " + x + " histogram"
    plt.title(title)
    plt.xlabel(x)
    path = "figures/histograms/" + n + "_" + x
    plt.savefig(path)


def write_to_file(path, title, stat):
    path = "stats/" + path
    f = open(path, "a")
    text = title + ":\n" + str(stat) + "\n\n"
    f.write(text)
    f.close()

def main(in_file1, in_file2):
    # Read in files using schema
    vivino_dtypes = {
            "title":np.str_, 
            "winery":np.str_, 
            "region":np.str_, 
            "rating":np.float, 
            "number of ratings":np.float
            }
    vivino_data = pd.read_csv(
            in_file1, 
            dtype = vivino_dtypes
            )

    pro_dtypes = {
            "country":np.str_, 
            "description":np.str_, 
            "designation":np.str_, 
            "points":np.float, 
            "price":np.float, 
            "province":np.str_, 
            "region_1":np.str_, 
            "region_2":np.str_, 
            "taster_name":np.str_, 
            "taster_twitter_handle":np.str_, 
            "title":np.str_, 
            "variety":np.str_, 
            "winery":np.str_
            }
    pro_data = pd.read_csv(
            in_file2, 
            dtype = pro_dtypes,
            index_col = 0
            )

    # Clean data
    # vivino_data = extract_vintage(data)
    # vivino_data = extract_country(data)
    vivino_data = split(vivino_data, 
            "title", 
            '(\d{4})|(N.V)', 
            "wine", 0, np.str_, 
            "vintage", 1, np.float
            )
    vivino_data = split(
            vivino_data, 
            "region", 
            '·',
            "country", 0, np.str_, 
            "region", 1, np.str_,
            drop_col = False
            )
    pro_data = split(
            pro_data, 
            "title", 
            '(\d{4})', 
            "vintage", 1, np.float, 
            "area", 2, np.str_
            )
    pro_data = split(
            pro_data, 
            "area", 
            '(', 
            "wine", 0, np.str_, 
            "region", 1, np.str_
            )
    pro_data = split(
            pro_data, 
            "region", 
            ')', 
            "region", 0, np.str_, 
            "_", 1, np.str_,
            drop_col = False
            )
    pro_data["ratings"] = pro_data["points"] / 20
    pro_data = pro_data.drop(columns = [
        "designation", 
        "description", 
        "province", 
        "points", 
        "region_1", 
        "region_2", 
        "taster_name", 
        "taster_twitter_handle",
        "_"
        ])
    

    # Get some preliminary figures of the data
    scatter(vivino_data, "country", "ratings", "Vivino")
    scatter(vivino_data, "vintage", "ratings", "Vivino")
    countries = vivino_data["country"].unique()
    grouped_countries = vivino_data.groupby(by = "country")
    for country in countries:
        df = grouped_countries.get_group(country)
        scatter(df, "region", "ratings", "Vivino " + country)
    
    scatter(pro_data, "country", "ratings", "Professional")
    scatter(pro_data, "vintage", "ratings", "Professional")
    countries = pro_data["country"].unique()
    scatter(pro_data, "region", "ratings", "Professional United States")
    
    # Get some prelimary statistical graphs and figures
    boxplot(vivino_data, "ratings", "Vivino")
    histogram(vivino_data, "ratings", "Vivino")
    
    boxplot(pro_data, "ratings", "Professional")
    histogram(pro_data, "ratings", "Professional")

    # Preliminary stats data
    write_to_file("vivino_stats.txt", "Regression Data", vivino_data["ratings"].describe())
    write_to_file("vivino_stats.txt", "Covariance of Ratings and Number of Ratings", stats.linregress(vivino_data['ratings'], vivino_data['number of ratings']).rvalue)

    write_to_file("pro_stats.txt", "Regression Data", pro_data["ratings"].describe())
    write_to_file("pro_stats.txt", "Covariance of Ratings and Price", stats.linregress(pro_data['ratings'], pro_data['price']).rvalue)

    #Scale ratings from 0 - 1
    vivino_data["scaled_ratings"] = (vivino_data["ratings"] - vivino_data["ratings"].min()) / (vivino_data["ratings"].max() - vivino_data["ratings"].min())
    pro_data["scaled_ratings"] = (pro_data["ratings"] - pro_data["ratings"].min()) / (pro_data["ratings"].max() - pro_data["ratings"].min())

    # Check normality (test and histogram)
    write_to_file("vivino_stats.txt", "Normality Test for Scaled Ratings", stats.normaltest(vivino_data["scaled_ratings"]).pvalue)
    write_to_file("pro_stats.txt", "Normality Test for Scaled Ratings", stats.normaltest(pro_data["scaled_ratings"]).pvalue)
    write_to_file("comparison_stats.txt", "Normality Test for Vivino Scaled Ratings", stats.normaltest(vivino_data["scaled_ratings"]).pvalue)
    write_to_file("comparison_stats.txt", "Normality Test for Professional Scaled Ratings", stats.normaltest(pro_data["scaled_ratings"]).pvalue)

    histogram(vivino_data, "scaled_ratings", "Vivino")
    histogram(pro_data, "scaled_ratings", "Professional")
    
    # Check equal variance
    write_to_file("comparison_stats.txt", "Levene Test for Variance", stats.levene(vivino_data["scaled_ratings"], pro_data["scaled_ratings"]).pvalue)

    # Calculate means
    write_to_file("comparison_stats.txt", "Mean for Scaled Data of Vivino Ratings", vivino_data["scaled_ratings"].mean())
    write_to_file("comparison_stats.txt", "Mean for Scaled Data of Professional Ratings", pro_data["scaled_ratings"].mean())

    # T-test
    ttest = stats.ttest_ind(vivino_data["scaled_ratings"], pro_data["scaled_ratings"])
    write_to_file("comparison_stats.txt", "T Test results", ttest)

    # Mann Whitney Test
    mann = stats.mannwhitneyu(vivino_data["scaled_ratings"], pro_data["scaled_ratings"])
    write_to_file("comparison_stats.txt", "Mann Whitney U Test", mann)




if __name__=='__main__':
    try:
        in_file1 = sys.argv[1]
        in_file2 = sys.argv[2]
        main(in_file1, in_file2)
    except InternalError as error:
        print_error(error)
    except Exception as error:
        print("Unhandled exception: " + str(error))
