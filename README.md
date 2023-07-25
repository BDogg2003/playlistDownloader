# playlistDownloader
Downloads playlists off of youtube, turns audio only files into mp3

This is just something I made after getting frustrated at the plethora of spam and virus ads from tools on the internet.
Also because there's no limit on playlist size when you make it yourself.

While not included in the files, the programs looks for 2 subdirectories, 1 for music, 1 for video. The folder for music is needed since the program uses it to isolate files slated for extension changes (all downloads start off as mp4s).


The filestack should look like this:

```
root_Folder
    ├───main.py
    ├───mus
    │   └───(files)
    └───vid
        └───(files)
```
(Note: the folder names can be changed, but the variables containing folder names in the script must be updated accordingly)
(Note: The script will convert _all_ files in the music subdirectory into .mp3 files, so be careful with what you put in there)
