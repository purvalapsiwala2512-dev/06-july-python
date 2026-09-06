def get_song_duration(song_name):
    spotify_tracks = {
        "Kesariya": "4:28",
        "Apna Bana Le": "4:21",
        "Chaleya": "3:20",
        "Heeriye": "3:14"
    }
    try:
        duration = spotify_tracks[song_name]
        return duration
    except KeyError:
        print("Song not found on Spotify!")

print("Duration:", get_song_duration("Kesariya"))
get_song_duration("Unknown Song")