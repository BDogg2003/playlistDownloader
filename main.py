from pytube import YouTube
from pytube import Playlist as pl
from pytube.exceptions import RegexMatchError

import tkinter as tk
from tkinter import *

import os


class YouTubeVideo:
    def __init__(self, givenURL) -> None:
        self.givenURL = givenURL
    
    def download_audio(self, prefix: str) -> None:
        try:
            yt = YouTube(self.givenURL)
            print(yt.streams.filter(only_audio = 'True').asc().first())
            video = yt.streams.filter(only_audio = 'True').asc().first()
            video.download("mus/", filename_prefix=prefix)  
        except RegexMatchError:
            print('url not found')
        except Exception as e:
            print(e)
            
            
    def download_video(self, prefix: str) -> None:
        try:
            yt = YouTube(self.givenURL)
            video = yt.streams.filter(progressive = 'True').desc().first()
            print(video)
            video.download("vids/", filename_prefix=prefix)
        except RegexMatchError:
            print('url not found')
        except Exception as e:
            print(e)
            
            
def want_audio(url: str, mode: int) -> None:
    
    if(mode == 0):
        audio = YouTubeVideo(url)
        audio.download_audio("")
    else:
        p = pl(url)
        i = 1
        for vid in p.video_urls:
            audio = YouTubeVideo(vid)
            audio.download_audio("{}. ".format(i))
            print("next")
            i += 1
        print("done")
        
        
    #Rename files to mp3
    path = "mus/"
    dir_list = os.listdir(path)

    for dir in dir_list:
        my_file = 'mus/{}'.format(dir)
        base = os.path.splitext(my_file)[0]
        os.rename(my_file, base + '.mp3')
    
def want_video(url: str, mode: int) -> None:
    if(mode == 0):
        video = YouTubeVideo(url)
        video.download_video("")
    else:
        p = pl(url)
        i = 1
        for vid in p.video_urls:
            video = YouTubeVideo(vid)
            video.download_video("{}. ".format(i))
            print("next")
            i += 1
        print("done")
            
#Kinter gui
def GUI() -> None:
    req = tk.Tk()
    req.title("YouTube Video")
    
    top = Label(req, text = "YouTube Downloader")
    top.config(font = ("Ariel", 20))
    top.grid(row = 0, columnspan = 5)
        
    f3 = Frame(req)
    Label(f3, text="|").grid(row = 0, column = 0)
    f3.grid(row = 3, column = 1)
    
    #single vid
    sv = Frame(req, padx = 2, pady = 2)
    
    
    Label(sv, text = "Single Video", font = ("Ariel", 14)).grid(row = 1, columnspan = 2)
    
    instrctions = Label(sv, text = "Enter a yt VIDEO url")
    instrctions.grid(row = 5, columnspan = 2)
    
    url = Entry(sv)
    url.grid(row = 6, columnspan=2)
    
    Mp3 = Button(sv, text = "Download Mp3" ,command= lambda : want_audio(url.get(), 0))
    Mp4 = Button(sv, text = "Download Mp4" ,command= lambda : want_video(url.get(), 0))
    
    Mp3.grid(row = 7, column = 0, padx = 2, pady = 2)
    Mp4.grid(row = 7, column = 1, padx = 2, pady = 2)
    sv.grid(row = 3, column = 0)
    
    #playlist
    playlist = Frame(req, padx = 2, pady = 2)
    
    Label(playlist, text = "Playlist", font = ("Ariel", 14)).grid(row = 1, column = 4, columnspan = 2)
    
    instrctions2 = Label(playlist, text = "Enter a yt PLAYLIST url")
    instrctions2.grid(row = 5, column = 4, columnspan = 2)
    
    url2 = Entry(playlist)
    url2.grid(row = 6, column = 4, columnspan=2)
    
    Mp32 = Button(playlist, text = "Download Mp3" ,command= lambda : want_audio(url2.get(), 1))
    Mp42 = Button(playlist, text = "Download Mp4" ,command= lambda : want_video(url2.get(), 1))
    
    Mp32.grid(row = 7, column = 4, padx = 2, pady = 2)
    Mp42.grid(row = 7, column = 5, padx = 2, pady = 2)
    playlist.grid(row = 3, column = 2)
    
    req.mainloop()


def main():
    GUI()
    print("Good Bye")
    
if __name__ == "__main__":
    main()