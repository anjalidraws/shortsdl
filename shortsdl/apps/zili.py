"""
Zili Video
Example Video: https://h5.zilivideo.com/puri/share/video/index/950761516795330567c94353b45a95ee/4/IN/hi/20210130
"""

import requests
from bs4 import BeautifulSoup

def video(video_link):
    response = requests.get(video_link, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}).text
    scrape = BeautifulSoup(response, 'html.parser')
    return scrape.video['src']