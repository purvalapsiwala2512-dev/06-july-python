f=open("my_fav_songs.txt","r")
data = f.readlines()
for i in enumerate(data):
    print(i)

f.close()