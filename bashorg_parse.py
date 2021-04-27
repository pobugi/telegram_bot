import json
import requests
import unidecode
import csv
from bs4 import BeautifulSoup

url = "https://bash.im/random"


def get_html(address):
    try: 
        result = requests.get(address)
    except requests.exceptions.ConnectionError:
        return 'Connection refused'
    return result.text

def get_data(html):
    result = []
    try:
        soup = BeautifulSoup(html, 'lxml')

        quotes_section = soup.find('section', class_='quotes')

        quotes = quotes_section.find_all('article', class_='quote')

        for quote in quotes:
            quote_frame = quote.find('div', class_='quote__frame')
            quote_footer = quote_frame.find('footer', class_='quote__footer')

            quote = quote_footer.find('div', class_='quote__button share').get('data-share')
            
            result.append(quote)
    except:
        return 'Error'
    
    return result[0]


def get_anecdote():
    q = get_data(get_html(url))
    r = json.loads(q)
    res = r['description'].replace('<br>', '\n')
    res = res.replace('<br />', '\n')
    res = res.replace('&quot;', '"')
    link = "https://bash.im/" + r["url"]
    return res + "\n" + link

