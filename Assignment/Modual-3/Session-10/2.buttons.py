from tkinter import *

root = Tk()
root.title('My Playlist')

label = Label(root,text='Welcome to Your Music Playlist')
label.pack()
root.geometry("400x300")

def play():
    status_label.config(text='Playing')

def pause():
    status_label.config(text='Paused')

def next_music():
    status_label.config(text='Next Song')

play_btn = Button(root,text='Play', command=play)
pause_btn = Button(root,text='Pause',command=pause)
next_btn = Button(root, text='Next',command=next_music)

play_btn.pack()
pause_btn.pack()
next_btn.pack()

status_label = Label(root,text='Status')
status_label.pack()
root.mainloop()