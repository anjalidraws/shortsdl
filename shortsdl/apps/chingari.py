"""
Chingari App
Example Video: https://chingari.io/share/post?id=5fa02405ff5394099b239be5
"""

import requests

def postData(video_url):
    video_id = video_url.split("=")[1]
    try:
        postJSON = requests.get(f"https://api.chingari.io/post/post_details/{video_id}", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"}).json()
        try:
            video_link = postJSON['data']['mediaLocation']['base'] + postJSON['data']['mediaLocation']['path']
            return video_link
        except:
            print("Chingari JSON format changed. Please create an issue at https://github.com/w3Abhishek/shortsdl/issues so we can fix it.")
    except:
        print("Invalid URL or Chingari API is not accessible. Please create an issue at https://github.com/w3Abhishek/shortsdl/issues if the issue persists with other video URLs.")