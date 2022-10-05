"""
FunXD App
Example Video: https://funxd.co/video/HaOZe8Xh9
"""

import requests
from bs4 import BeautifulSoup

def video(video_link):
    response = requests.get(video_link, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}).text
    scrape = BeautifulSoup(response, 'html.parser')
    print(scrape.video['data-src'])