from pytube import YouTube
import os

# Data finder
data_lst = []
for file in os.listdir():
    x, dist = os.path.splitext(file)
    if dist == ".txt":
        data_lst.append(file)

for data in data_lst:
    # Grabbing list full of links...
    with open(f"{data}", "r") as file:
        lines = file.readlines()

    # Runs each line through YouTube downloader
    for num in range(len(lines)):
        try:
            # Grabbing link in list
            song = YouTube(lines[num])

            # YouTube Title
            print(f"{num}/{len(lines)}")
            print("Title:")
            print(song.title)

            # Downloads the YouTube audio
            song = song.streams.filter(only_audio=True).first()

            # File location
            location = "Music"
            song = song.download(location)

            title, args = os.path.splitext(song)
            new_title = title + ".mp3"
            os.rename(song, new_title)

        except:
            print("This YouTube link is not real:" + lines[num])
