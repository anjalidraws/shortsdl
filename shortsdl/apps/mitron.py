"""
Mitron Short Video
Example Video: https://api.mitron.tv/v1/share?id=B4zmXogwGiJl2KT4O3
"""

import requests, json
from bs4 import BeautifulSoup
def video(video_link):
    video_link = video_link.replace("https://api.mitron.tv/v1/share?id=", "https://web.mitron.tv/video/")
    response = requests.get(video_link, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}).text
    scrape = BeautifulSoup(response, 'html.parser')
    data = json.loads(scrape.find_all("script", attrs={'id':"__NEXT_DATA__"})[0].text)
    return data['props']['pageProps']['video']['videoUrl']