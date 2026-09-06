file = open("playlist.txt", "r")
file.readline()
song3_position = file.tell()
file.seek(song3_position)
third_song = file.readline()
print("Third song:", third_song.strip())

file.close()