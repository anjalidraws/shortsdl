"""
Triller App
Example Video: https://triller.co/@keshavtyoharofficial/video/8c946428-8df5-4ed5-b85e-595657154ca3
"""

import requests

def video(video_link):
    video_api = "https://social.triller.co/v1.5/api/videos/" + video_link.split("/video/")[1]
    response = requests.get(video_api, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}).json()
    return response['videos'][0]['video_url']