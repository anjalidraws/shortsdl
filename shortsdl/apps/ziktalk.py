"""
ZikTalk Video App
Example Video: https://ziktalk.com/post/view/c9f8b4d4-f47d-4095-a2bc-b6db89dea4c5?userId=38eaf5fc-353c-4c3b-a316-573623d55f0c
"""

import requests

def video(video_link):
    video_api = video_link.replace("https://ziktalk.com/post/view/","https://api.zigu.world/api/v1.0/Post/view/")
    response = requests.get(video_api, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}).json()
    return response['data']['mediaPath']