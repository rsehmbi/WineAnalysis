import time
from selenium import webdriver
import copy
from bs4 import BeautifulSoup
import csv


# url = 'https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NTBQS660dXZUSwYSLmoFQNn0NNuyxKLM1JLEHLX8JNuixJLMvPTi-MSy1KLE9FS1fNuU1OJktfKS6FigYjBlBACsPByG'
url = 'https://www.vivino.com/explore?e=eJwdisEKgCAQBf_mna37HqL-IiI220RIjVWs_j7pMnOYCUodgo9kEPihzsC-NA6wDROuFt1BldVL4RNpI-Xio8srV1F2gkS7ZIu7zEubf_UfmQEcUg=='
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get(url)
prev_height = driver.execute_script("return document.body.scrollHeight")
fields = ['title', 'winery', 'region', 'ratings', 'number of ratings']
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(6)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == prev_height:
        break
    prev_height = new_height
html = BeautifulSoup(driver.page_source, 'lxml')
div = html.find("div", {"class": "explorerPage__results--3wqLw"})
rows = html.find_all("div", {"class": "explorerCard__explorerCard--3Q7_0"})
wine = {"title": None, "winery": None, "region": None, "ratings": None, "number of ratings": None}

with open("vivino_data.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)
    for r in rows:
        row = copy.copy(wine)
        row['title'] = r.find("span", {"class": "vintageTitle__wine--U7t9G"}).text
        row['winery'] = r.find("span", {"class": "vintageTitle__winery--2YoIr"}).text
        row['region'] = r.find("div", {"class": "vintageLocation__vintageLocation--1DF0p"}).text
        row['ratings'] = r.find("div", {"class": "vivinoRatingWide__averageValue--1zL_5"}).text
        row['number of ratings'] = int(r.find("div", {"class": "vivinoRatingWide__basedOn--s6y0t"}).text.split()[0])
        csv_writer.writerow([row['title'], row['winery'], row['region'], row['ratings'], row['number of ratings']])