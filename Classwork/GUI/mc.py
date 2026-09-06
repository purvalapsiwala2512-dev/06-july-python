import tkinter as tk
from tkinter import filedialog
import winsound
import os

# Create window
root = tk.Tk()
root.title("🎵 Music Player")
root.geometry("500x400")
root.resizable(False, False)

song = ""


# Load song
def load_song():
    global song

    song = filedialog.askopenfilename(
        title="Select Music",
        filetypes=[("WAV Files", "*.wav")]
    )

    if song:
        name = os.path.basename(song)
        song_label.config(text=name)


# Play song
def play_song():
    if song:
        winsound.PlaySound(
            song,
            winsound.SND_FILENAME |
            winsound.SND_ASYNC
        )


# Stop song
def stop_song():
    winsound.PlaySound(
        None,
        winsound.SND_PURGE
    )


# Main title
title = tk.Label(
    root,
    text="🎵 MY MUSIC PLAYER",
    font=("Arial", 25, "bold")
)
title.pack(pady=30)


# Song name
song_label = tk.Label(
    root,
    text="No song selected",
    font=("Arial", 13),
    wraplength=400
)
song_label.pack(pady=20)


# Load button
load_button = tk.Button(
    root,
    text="📂 Load Song",
    font=("Arial", 13),
    width=15,
    command=load_song
)
load_button.pack(pady=10)


# Play button
play_button = tk.Button(
    root,
    text="▶ Play",
    font=("Arial", 13),
    width=15,
    command=play_song
)
play_button.pack(pady=5)


# Stop button
stop_button = tk.Button(
    root,
    text="⏹ Stop",
    font=("Arial", 13),
    width=15,
    command=stop_song
)
stop_button.pack(pady=5)


# Start application
root.mainloop()