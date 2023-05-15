from pytube import YouTube
from threading import Thread 
from pydub import AudioSegment
import sys
import os


# Ask user for YouTube video URL
url = input("Enter the YouTube video URL: ")
url = url if "https://youtu" in url else sys.exit()
path = (
  '/storage/emulated/0/Music' ,
  '/storage/emulated/0/Music/English',
  '/storage/emulated/0/1_BOOKS/COURT/Law Books/CPC_Videos'
  )

def inputs():
  for n, p in enumerate(path):
      print(f"{n} : {p[20:]}")
      
  global des 
  des= int(input('Enter the path number : '))
  des = des if des else None
  
  global destination 
  destination = path[des] if des != None else des

  global choice 
  choice = 1 if des else input('\n1. Audio\n2. Video : ')

t1 = Thread(target=inputs)
t1.start()
def format(streams):
  print("=" * 62)    

  print(

  'SN'.rjust(3), 
  'itag'.center(4), 
  'res'.center(5), 
  'abr'.center(8), 
  'mime_type'.center(10), 
  'Prograssive'.center(12), 
  'type'.center(4),
  'size'.ljust(6)

  )

  print("=" * 62)


  for n, s in enumerate (streams):
    
      abr = s.abr if s.abr != None else  "-"
      resolution = s.resolution if s.resolution != None else "-"
      is_progressive = "T" if s.is_progressive == True else 'F'
      type = "V" if s.type == 'video' else "A" if s.type == 'audio' else 'o'
      size = f"{s.filesize_mb:0,.2f}-mb"
      #f'{str(s.filesize_mb)}MB'
      #f"{a:0,.2f}"
    
      #print("\n")
    
      print(
      str(n).rjust(3), 
      str(s.itag).rjust(4), 
      str(resolution).center(5), 
      str(abr).center(8), 
      s.mime_type.center(10), 
      str(is_progressive).center(12), 
      type.center(4),
      size.ljust(6)
    
      )
    
      print("_" * 62)
  
  
      


# Create a YouTube object and get the video stream with the highest resolution
#yt = YouTube(url)
yt = YouTube(url, use_oauth=True,allow_oauth_cache=True)
streams = yt.streams
format(streams)
index  = int(input("Enter the serial number : "))
stream = streams[index]
print("\nSelected stream is :")
print(stream)


# Display video information
'''
print("Title:", yt.title)
print("Author:", yt.author)
print("Length:", (yt.length)//60,'minutes',(yt.length)%60,"seconds")
print("Views:", yt.views)
'''
def video(stream):
  # Download the video to the current directory
  print("Downloading video...")
  stream.download(output_path=destination)
  print("Video downloaded successfully!")

def audio(stream):
  # Get the highest resolution audio stream
  audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()
  
  # Download the audio streams
  song = input("Enter filename (default = Ml_Eng_): ")
  song = f"Ml_Eng_" if song == "" else song
  print("Downloading audio......")
  audio_file = audio_stream.download(output_path=destination, filename
  =f'{song}.mp3')
  print("Audio has been downloaded \n")
  
  
  head, tail = os.path.split(audio_file)
  audio = AudioSegment.from_file(audio_file)
  print('increasing volume.......')
  segment = audio + 7
  f_name = f'new{tail}'
  f_path = os.path.join(head, f_name)  

  segment.export(f_path, format="mp3")
  
  # Delete the original audio file
  os.remove(audio_file)

  print("The video has been increased volume ")
t1.join()

if stream.type == 'video':
    video(stream)
else:
    audio(stream)

  