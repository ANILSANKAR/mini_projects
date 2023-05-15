#!/usr/bin/env python


from pytube import YouTube
import os 

print("Enter the destination address Number ")
des = int(input('0. Music \n1. English \n Numberis : '))
path = ('/storage/emulated/0/Music' ,'/storage/emulated/0/Music/English')

destination = path[des]


yt = YouTube(input("Enter URL of youtube video: \n "))
video = yt.streams.filter(only_audio=True).order_by('resolution').desc().first()
out_file = video.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print(yt.title + " has been successfully downloaded.")