import yt_dlp

url = input("Enter YouTube URL:https://youtu.be/E22Zxi06l3c?si=U0N3kskRvjzCa1yZ")

options = {
    "format": "bestvideo+bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s"
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])

print("Download completed!")