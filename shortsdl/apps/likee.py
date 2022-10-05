"""
Likee Video App
Example Video: https://likee.video/@NilibethZambrano/video/7147888591790507636
"""

import requests, json
from bs4 import BeautifulSoup

def video(video_link):
    response = requests.get(video_link, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}).text
    scrape = BeautifulSoup(response, 'html.parser')
    return json.loads(scrape.find_all("script")[4].text.replace(";","").replace("window.data = ", ""))['videoUrl'].split("_4.mp4")[0]+".mp4"