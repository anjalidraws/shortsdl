"""
Roposo Video
Example Video: https://www.roposo.com/story/a870a6c9-6b60-4dba-85be-64100911b68e
"""

import requests
from bs4 import BeautifulSoup

def video(video_link):
    response = requests.get(video_link, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}).text
    scrape = BeautifulSoup(response, "html.parser")
    return scrape.source['src']