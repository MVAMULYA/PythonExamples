# !usr/bin/python

import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

with open("Bookmarks.json", 'r', encoding='utf-8') as in_file:
    bookmark_data = json.load(in_file)

    for folder in bookmark_data['roots']['bookmark_bar']['children']:
        if 'Internshala' in folder.values():
            bookmark_folder = folder['children']
            urls = []
            for item in bookmark_folder:
                urls.append(item['url'])
            
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    dates = soup.findAll(class_="item_body")
    name = soup.find('title')
    print(name.text)
    for date in dates:
        date = date.text.strip().split()
        if len(date) == 3:
            try:
                day = int(date[0])
                date = date[0] + ' '  + date[1].strip("'") + ' ' +  date[2].strip("'") + ' 23:59:59'
                date = datetime.strptime(date, "%d %b %y %H:%M:%S")
                today = datetime.now()         
                remain = date - today
                print('Number of days remaining to apply :', remain.days)
            except ValueError as err:
                pass
    print('*'*100)
