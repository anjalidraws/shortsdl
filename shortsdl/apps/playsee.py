"""
Playsee - Short Video App
Example Video: https://share.playsee.co/post/%21EIq7EhJut%7E
"""

def video(video_url):
    video_id = video_url.split("/post/")[1]
    video_file = f"https://g-pst.playsee.co/vdo/{video_id}.mp4"
    return video_file