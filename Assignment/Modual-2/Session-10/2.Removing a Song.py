def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)
    else:
        print(f"'{song_name}' is not in the playlist.")
    return playlist