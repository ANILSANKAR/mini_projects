import pytube

# Enter the URL of the YouTube video you want to download
#url = input('Enter the url of the video: ')
url ='https://youtu.be/zBjJUV-lzHo'
# Create a YouTube object and get the available streams
yt = pytube.YouTube(url)
streams = yt.streams

# Filter the streams based on file type and resolution

#video_streams = streams.filter(file_extension="mp4", res="720p")
audio_streams = streams.filter(only_audio=True)
'''
# Print information about the available streams
print("Video Streams:")
for stream in video_streams:
    print(stream)
'''
print("\nAudio Streams:")
for stream in audio_streams:
    print(stream,'\n')

tag = int(input('Enter the itag : '))
audio_streams = audio_streams.get_by_itag(itag=tag  )
#get_by_resolution(resolution=res)

# Download the first video and audio streams
#video_streams.first().download()
audio_streams.download()
