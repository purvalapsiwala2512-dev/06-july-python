playlists = {'user1': {'Favourites': ['Song1', 'Song2']}}

playlists.setdefault('user2', {}).setdefault('Chill', []).append('Song3')

print(playlists)