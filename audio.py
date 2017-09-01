from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
print("Enter the link of the video")
url = input()
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])