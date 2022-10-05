"""
Tick: watch to earn
Example Video: 
"""
import requests

def postData(video_link):
    data = getLinkData(video_link)
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0',
    'device-id': data['device_id'],
    'language': 'en',
    'utm-source': 'undefined',
    'platform': 'Linux x86_64',
    'client-v': '4.11.1'
    }
    response = requests.post("https://landing.tickvideo.com/api//Share/GetShareInfo", headers=headers, data=data).json()
    return response

def video(video_link):
    post = postData(video_link)
    download_link = post['data']['video']['videoInfo'][0]['url']
    return download_link


def getLinkData(video_link):
    video_links = video_link.split("?")[1].split("&")
    data = {}
    for values in video_links:
        value = values.split("=")
        data[value[0]] = value[1]
    data['scene'] = '20'
    return data