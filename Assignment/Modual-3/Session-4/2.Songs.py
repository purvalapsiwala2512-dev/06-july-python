class SongAlreadyExistsError(Exception):
    pass

playlist =["imiimiimi","Apna Bana Le","Heeriye"]
song = input("Enter song name:")

def add_song_to_playlist(song):
    try:
        if song in playlist:
            raise SongAlreadyExistsError(song)
        else:
            print("Song Added")
    except SongAlreadyExistsError as l:
        print(l,",Song already exists in playlists")

add_song_to_playlist(song)