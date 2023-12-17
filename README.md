# YouTube Url  List Downloader
##Python
###Module:
- pytube
- os

So the very first thing this is going to do is find all the `text` files with `txt` and scan through them and get the urls.
```bash
# Data finder
data_lst = []
for file in os.listdir():
    x, dist = os.path.splitext(file)
    if dist == ".txt":
        data_lst.append(file)
```
then it's going to scan through the file and get all the urls individually
```bash
for data in data_lst:
    # Grabbing list full of links...
    with open(f"{data}", "r") as file:
        lines = file.readlines()

    # Runs each line through YouTube downloader
    for num in range(len(lines)):
        try:
            # Grabbing link in list
            song = YouTube(lines[num])
```
then of course it will start the downloading process

```bash
# So because we only want the audio we need to make sure it does just that
# and what this does is streams the video, filter out only the audio, and then we just place it into a string
song = song.streams.filter(only_audio=True).first()

# This is going to create a folder to put your music in.
location = 'Playlist'
song = song.download(location)

# Splits "song" and ".mp4"
# Transforms to 'song.mp3'
# args a trash string it just holds the rest off '.mp4'
title, args = os.path.splitext(song)
new_title = title + '.mp3'
# Renames the file to the new name
os.rename(song, new_title)
print("Download complete!")
```
And Boom! Downloaded song complete! :) Throws it straight into your folder