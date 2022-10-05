"""
Tiki Video
Example Video: https://l.tiki.video/v/tJ1mVN
"""

import requests, json
from bs4 import BeautifulSoup

def video(video_link):
    response = requests.get(video_link).text
    scrape = BeautifulSoup(response, 'html.parser')
    return json.loads(scrape.find_all("script")[4].text.replace(";","").replace("window.data = ",""))['video_url'].split("?")[0]