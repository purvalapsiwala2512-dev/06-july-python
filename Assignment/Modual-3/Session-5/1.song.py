class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

song1 = Song("Kesariya", "Arijit Singh", 268)
song2 = Song("Chaleya", "Anirudh Ravichander", 200)

print(song1.title,f"({song1.duration}s)")
print(song2.title,f"({song2.duration}s)")