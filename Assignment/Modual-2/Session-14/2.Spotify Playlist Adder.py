def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    playlists.setdefault(user, {}).setdefault(playlist_name, []).append({
        "title": song_title,
        "artist": artist
    })
    return playlists

spotify_data = {}

add_song_to_playlist(spotify_data, "user_1", "Workout", "Eye of the Tiger", "Survivor")
add_song_to_playlist(spotify_data, "user_1", "Workout", "Stronger", "Kanye West")

print(spotify_data)