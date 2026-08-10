from playlist import add_song, remove_song

my_playlist = []
my_playlist = add_song('Kesariya', my_playlist)
my_playlist = add_song('Shape of You', my_playlist)
my_playlist = add_song('Believer', my_playlist)

# Remove song
my_playlist = remove_song('Shape of You', my_playlist)

print("Playlist after removal:", my_playlist)