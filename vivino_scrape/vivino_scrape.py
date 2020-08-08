import re
import requests
from time import sleep
from bs4 import BeautifulSoup
import csv

# DISCLAIMER: This code was taken from https://stackoverflow.com/questions/62440870/python-web-scraping-beautiful-soup-with-list-of-keywords-at-the-end-of-url,
# and has been modified to suit our needs.

url = 'https://www.vivino.com/search/wines?q={kw}&start={page}'
prices_url = 'https://www.vivino.com/prices'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0'
headers = {'User-Agent': user_agent}
search_words = ['red', 'white']
max_search = 608028
fields = ['wine', 'region', 'price', 'rating']

def get_wines(sw):
    with requests.session() as s:
        for page in range(1, max_search+1):
            soup = BeautifulSoup(s.get(url.format(kw=sw, page=page), headers=headers).content, 'html.parser')

            if not soup.select('.default-wine-card'):
                break

            params = {'vintages[]': [wc['data-vintage'] for wc in soup.select('.default-wine-card')]}
            prices_js = s.get(prices_url, params=params, headers={
                'User-Agent': user_agent,
                'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'
                }).text
            wine_prices = dict(re.findall(r"\$\('\.vintage-price-id-(\d+)'\)\.find\( '\.wine-price-value' \)\.text\( '(.*?)' \);", prices_js))

            for wine_card in soup.select('.default-wine-card'):
                title = wine_card.select_one('.header-smaller').get_text(strip=True, separator=' ')
                region = wine_card.select_one('.wine-card__region').get_text(strip=True, separator=' ')
                price = wine_prices.get(wine_card['data-vintage'], '-')
                average = wine_card.select_one('.average__number')
                average = average.get_text(strip=True) if average else '-'
                ratings = wine_card.select_one('.text-micro')
                ratings = ratings.get_text(strip=True) if ratings else '-'
                yield title, region, price, average, ratings

            sleep(3)


with open('vivino_red_white.csv', 'w') as f:
	csv_writer = csv.writer(f)
	csv_writer.writerow(fields)
	for sw in search_words:
	    for title, region, price, average, ratings in get_wines(sw):
	    	lst = region.split(' ')
	    	rating = ratings.split(' ')[0]
	    	subregion, country = lst[0], lst[len(lst)-1]
	    	csv_writer.writerow([title, subregion+'-'+country, price, average+'/'+rating])


