from pydub import AudioSegment
name = 'Ml_Eng_5.mp3'
# Load the audio file
audio_file = AudioSegment.from_file(name)
start = 45*1000
end = 13*60*1000 + 20*1000
# Extract a segment of the audio
segment = audio_file[start:end] # Extracts segment from 10s to 20s
segment = segment + 6
# Fade in the segment
#segment = segment.fade_in(5000) # Fades in the first 5 seconds of the segment

# Fade out the segment
#segment = segment.fade_out(5000) # Fades out the last 5 seconds of the segment

# Export the edited segment to a new file
segment.export('new'+name, format="mp3")
