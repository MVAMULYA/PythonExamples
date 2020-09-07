#!usr/bin/python

import requests
from bs4 import BeautifulSoup
import json

page = requests.get("https://www.moneycontrol.com/news/business/economy/")
soup = BeautifulSoup(page.text, 'html.parser')


news_links = soup.findAll("li", {"id" : lambda n_list: n_list and n_list.startswith('newslist-')})
news_data = {'data' : []}
for link in news_links:
    news = {}
    a_tag = link.find('a')
    p_tag = link.find('p')
    span_tag = link.find('span')
    news['Address'] = a_tag['href']
    news['Text'] = p_tag.text
    news['Time'] = span_tag.text

    news_data['data'].append(news)

with open('news.json', 'w') as outfile:
    json.dump(news_data, outfile, indent=2)
