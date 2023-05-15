import glob as gb  
from pydub import AudioSegment
import os

# Initialize a variable  
location = '/storage/emulated/0/Music/English/'
location2 = '/storage/emulated/0/tmp'
songs = gb.iglob(f'{ location }M*.mp3') 
songs2= gb.iglob(f'{ location2 }M*.mp3') # Set Pattern in glob() function  
# Printing list of names of all files that matched the pattern  
print("List of the all the files in the directory having extension .mp3 :  \n")  
for s in [songs,songs2]:
 for song in songs:   
    head, tail = os.path.split(song)
    audio_file = AudioSegment.from_file(song)
    print("Volume increasing.....")
    segment = audio_file + 8
    print("Volume increased")
    f_name = f'new{tail}'
    f_path = os.path.join(head, f_name)  

    segment.export(f_path, format="mp3")
    print(f'New file exported to {f_path}')
    os.remove(song)
    
 