f = open("my_fav_songs.txt","r")

data=f.readlines()
print("Total Songs:",len(data))

f.close()