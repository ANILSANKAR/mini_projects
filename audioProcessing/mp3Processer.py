from pydub import AudioSegment
import os
os.environ["PATH"] += os.pathsep + "/data/data/com.termux/files/usr/bin"



path = input('Enter the path of the mp3 file : ')
song = AudioSegment.from_mp3(path)
name = input('Enter the new name of the mp3 file : ')

# start and end NotImplemented
start_min = int(input('Enter the start minutes : '))
start_sec = int(input('Enter the start second : ')) 
end_min = int(input('Enter the end minutes : '))
end_sec = int(input('Enter the end second : '))


# Time to milliseconds conversion
strt = StrtMin*60*1000+StrtSec*1000
end = StrtMin*60*1000+EndSec*1000
# song clip from start
newSong = song[start:end]
newSong = newSong + 6

# Save file
newSong.export('f{name}.mp3', format='mp3')

print('New Audio file is created and saved')