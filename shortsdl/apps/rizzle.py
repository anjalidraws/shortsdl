"""
Rizzle App
Example Video: https://rizzle.tv/post/615ec4d9778b325b98dcc3b3
"""

import requests
from bs4 import BeautifulSoup

def video(video_link):
    response = requests.get(video_link, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}).text
    scrape = BeautifulSoup(response, 'html.parser')
    print(scrape.source['src'])