#!/usr/bin/env python3
import re
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from internal_error import InternalError, print_error


def extract_vintage(data):
    split_vintage = data["title"].str.split(pat = '(\d{4})|(N.V)', expand = True)
    data["wine"] = split_vintage[0]
    data["vintage"] = split_vintage[1]
    data = data.drop(columns = ["title"])
    data = data.dropna()
    return data

def extract_country(data):
    split_region = data["region"].str.split(pat = '·', expand = True)
    data["country"] = split_region[0]
    data["region"] = split_region[1]
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



def main(in_file):
    # Read in file using schema above
    data = pd.read_csv(in_file)

    # Clean data
    data = extract_vintage(data)
    data = extract_country(data)
    
    # Get some preliminary figures of the data
    scatter(data, "country", "ratings")
    countries = data["country"].unique()
    grouped_countries = data.groupby(by = "country")
    for country in countries:
        df = grouped_countries.get_group(country)
        scatter(df, "region", "ratings", country)


if __name__=='__main__':
    try:
        in_file = sys.argv[1]
        main(in_file)
    except InternalError as error:
        print_error(error)
    except Exception as error:
        print("Unhandled exception: " + str(error))
