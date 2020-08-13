#!/usr/bin/env python3
import re
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from internal_error import InternalError, print_error
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd


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
    pro_data = pro_data[pro_data["vintage"] <= 2020]

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

    # Means of regions
    agg_regions = vivino_data.groupby("region").agg({"ratings":"count"})
    agg_regions = agg_regions[agg_regions["ratings"] > 40]
    agg_regions = pd.DataFrame(agg_regions.index)
    reg_join = agg_regions.merge(vivino_data, on = "region")

    scatter(reg_join, "region", "ratings", "Top 40 reviewed regions")
    means = reg_join.groupby("region").agg({"ratings":"mean"})
    write_to_file("comparison_stats.txt", "Means for Top 40 Reviewed Regions", means)

    reg_join = reg_join.drop(columns = ["winery", "number of ratings", "wine", "vintage", "country", "scaled_ratings"])
    ale = reg_join[reg_join["region"] == "Alentejano"]["ratings"]
    als = reg_join[reg_join["region"] == "Alsace"]["ratings"]
    bar = reg_join[reg_join["region"] == "Barbera d'Alba"]["ratings"]

    bao = reg_join[reg_join["region"] == "Barolo"]["ratings"]
    bas = reg_join[reg_join["region"] == "Barossa Valley"]["ratings"]
    bol = reg_join[reg_join["region"] == "Bolgheri"]["ratings"]

    bru = reg_join[reg_join["region"] == "Brunello di Montalcino"]["ratings"]
    cal = reg_join[reg_join["region"] == "California"]["ratings"]
    chi = reg_join[reg_join["region"] == "Chianti Classico"]["ratings"]

    cha = reg_join[reg_join["region"] == "Châteauneuf-du-Pape"]["ratings"]
    cot = reg_join[reg_join["region"] == "Côtes-du-Rhône"]["ratings"]
    dou = reg_join[reg_join["region"] == "Douro"]["ratings"]

    dao = reg_join[reg_join["region"] == "Dão"]["ratings"]
    lan = reg_join[reg_join["region"] == "Langhe"]["ratings"]
    mar = reg_join[reg_join["region"] == "Marlborough"]["ratings"]

    mcl = reg_join[reg_join["region"] == "McLaren Vale"]["ratings"]
    men = reg_join[reg_join["region"] == "Mendoza"]["ratings"]
    mon = reg_join[reg_join["region"] == "Montefalco"]["ratings"]

    nap = reg_join[reg_join["region"] == "Napa Valley"]["ratings"]
    nia = reg_join[reg_join["region"] == "Niagara Peninsula"]["ratings"]
    oka = reg_join[reg_join["region"] == "Okanagan Valley"]["ratings"]

    pas = reg_join[reg_join["region"] == "Paso Robles"]["ratings"]
    pau = reg_join[reg_join["region"] == "Pauillac"]["ratings"]
    pes = reg_join[reg_join["region"] == "Pessac-Léognan"]["ratings"]

    pom = reg_join[reg_join["region"] == "Pomerol"]["ratings"]
    rio = reg_join[reg_join["region"] == "Rioja"]["ratings"]
    rus = reg_join[reg_join["region"] == "Russian River Valley"]["ratings"]

    sai = reg_join[reg_join["region"] == "Saint-Julien"]["ratings"]
    sae = reg_join[reg_join["region"] == "Saint-Émilion Grand Cru"]["ratings"]
    san = reg_join[reg_join["region"] == "Sancerre"]["ratings"]

    son = reg_join[reg_join["region"] == "Sonoma Coast"]["ratings"]
    soc = reg_join[reg_join["region"] == "Sonoma County"]["ratings"]
    sou = reg_join[reg_join["region"] == "South Australia"]["ratings"]

    ste = reg_join[reg_join["region"] == "Stellenbosch"]["ratings"]
    sud = reg_join[reg_join["region"] == "Südtirol - Alto Adige"]["ratings"]
    ter = reg_join[reg_join["region"] == "Terre Siciliane"]["ratings"]

    tor = reg_join[reg_join["region"] == "Toro"]["ratings"]
    tos = reg_join[reg_join["region"] == "Toscana"]["ratings"]
    ven = reg_join[reg_join["region"] == "Veneto"]["ratings"]

    wil = reg_join[reg_join["region"] == "Willamette Valley"]["ratings"]

    anova = stats.f_oneway(ale,als,bar,bao,bas,bol,bru,cal,chi,cha,cot,dou,dao,lan,mar,mcl,men,mon,nap,nia,oka,pas,pau,pes,pom,rio,rus,sai,sae,san,son,soc,sou,ste,sud,ter,tor,tos,ven,wil)
    write_to_file("comparison_stats.txt", "ANOVA comparison of regions", anova)

    pd.melt(reg_join)
    x_data = pd.DataFrame({
        'Alentejano':ale, 'Alsace':als, "Barbera d'Alba":bar, 'Barolo':bao,
        'Barossa Valley':bas, 'Bolgheri':bol, 'Brunello di Montalcino':bru,
        'California':cal, 'Chianti Classico':chi, 'Châteauneuf-du-Pape':cha,
        'Côtes-du-Rhône':cot, 'Douro':dou, 'Dão':dao, 'Langhe':lan, 'Marlborough':mar,
        'McLaren Vale':mcl, 'Mendoza':men, 'Montefalco':mon, 'Napa Valley':nap,
        'Niagara Peninsula':nia, 'Okanagan Valley':oka, 'Paso Robles':pas, 'Pauillac':pau,
        'Pessac-Léognan':pes, 'Pomerol':pom, 'Rioja':rio, 'Russian River Valley':rus,
        'Saint-Julien':sai, 'Saint-Émilion Grand Cru':sae, 'Sancerre':san,
        'Sonoma Coast':son, 'Sonoma County':soc, 'South Australia':sou, 'Stellenbosch':ste,
        'Südtirol - Alto Adige':sud, 'Terre Siciliane':ter, 'Toro':tor, 'Toscana':tos,
        'Veneto':ven, 'Willamette Valley':wil})
    x_melt = pd.melt(x_data)
    x_melt = x_melt.dropna()
    posthoc = pairwise_tukeyhsd(x_melt['value'], x_melt['variable'],alpha=0.05)
    
    write_to_file("comparison_stats.txt", "Tukey HSD PostHoc Analysis of Top 40 Regions", posthoc)
    fig = posthoc.plot_simultaneous(figsize = (25, 20), xlabel = "ratings", ylabel = "Top 40 reviewes regions")
    fig.savefig("figures/posthoc")

if __name__=='__main__':
    try:
        in_file1 = sys.argv[1]
        in_file2 = sys.argv[2]
        main(in_file1, in_file2)
    except InternalError as error:
        print_error(error)
    except Exception as error:
        print("Unhandled exception: " + str(error))
