"""
Hipi (Zee5 Short Video)
Example Video: https://www.hipi.co.in/feed/for-you?videoId=a539c359-2656-4235-a423-2a2269582d6f
https://www.hipi.co.in/video/a539c359-2656-4235-a423-2a2269582d6f
"""

import requests

def video(video_link):
    videoId = ""
    if "/video/" in video_link:
        videoId = video_link.split("/video/")[1]
    else:
        videoId = video_link.split("=")[1]
    headers = {"guest-token": "1", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}
    response = requests.get(f"https://hipigwapi.zee5.com/api/v1/shorts/video/detail?id={videoId}", headers=headers).json()
    download_link = response['responseData']['videos'][0]['playback_urls'][-1]['url'][-1]
    return download_link