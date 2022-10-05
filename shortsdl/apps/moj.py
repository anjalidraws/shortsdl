"""
Moj Video
Example Video: https://mojapp.in/@nature_and_mountains/video/2739208269?referrer=web
"""

from bs4 import BeautifulSoup
import requests, json

def video(video_link):
    response = requests.get(video_link, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}).text
    scrape = BeautifulSoup(response, "html.parser")
    data = json.loads(scrape.find_all("script", attrs={"type":"application/json"})[0].text)
    data = json.loads(data['body'].replace("\\",""))
    print(data['payload']['d']['bandwidthParsedVideos'][-1]['url'])

video("https://mojapp.in/@nature_and_mountains/video/2739208269?referrer=web")