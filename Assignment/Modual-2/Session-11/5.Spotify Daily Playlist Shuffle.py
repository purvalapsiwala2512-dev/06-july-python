import random

playlist = [
    "Shape of You", "Blinding Lights", "Believer", "Levitating",
    "Kesariya", "Starboy", "Cold Mess", "Perfect"
]

daily_mix = random.sample(playlist, 3)

print("🎵 Today's Daily Mix:")
for pos, song in enumerate(daily_mix, start=1):
    print(f"{pos}. {song}")