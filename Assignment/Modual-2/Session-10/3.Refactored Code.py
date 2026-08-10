def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist

def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)
    else:
        print(f"'{song_name}' is not in the playlist.")
    return playlist

def display_playlist(playlist):
    if not playlist:
        print("\nYour playlist is empty.")
        return
    
    print("\n--- Current Queue ---")
    for position, song in enumerate(playlist, start=1):
        print(f"{position}. {song}")