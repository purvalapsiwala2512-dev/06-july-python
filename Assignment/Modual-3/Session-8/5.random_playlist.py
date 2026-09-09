import random
from songs import song_list


shuffled = song_list.copy()
random.shuffle(shuffled)

print("Shuffled Playlist:")
for index,song in enumerate(shuffled,start=1):
    print(f"{index}.{song}")