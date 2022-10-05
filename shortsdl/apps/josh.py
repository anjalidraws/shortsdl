"""
Josh App
Example Video: https://share.myjosh.in/video/f729dd1e-5280-45d0-8d13-0fd82e31df39?u=0x9e95b100e75194ff
"""
import requests

def video(video_link):
    video_id = video_link.split("?")[0].replace("https://share.myjosh.in/video/","")
    data = {
            "method":"POST",
            "url":"https://feed.myjosh.in/feed/pwa/foryou?card_type=video",
            "body":{
                "clientId":"babf778a-5e63-4e2d-ba9b-397f26d7645e",
                "langs":"en",
                "userUuid":"",
                "itemId":video_id,
                "client_id":"babf778a-5e63-4e2d-ba9b-397f26d7645e"
            },
            "coolfie_debug_info":"appVersion=7.2.17.2208160803.2&clientId=babf778a-5e63-4e2d-ba9b-397f26d7645e&user_lang=en&nav_lang=en&device=josh_pwa",
            "platform":"PWA"
            }
    response = requests.get("https://share.myjosh.in/webview/apiwbody", data=data, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"})
    return response['data'][0]['mp4_url']