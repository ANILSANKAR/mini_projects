from pytube import YouTube
from threading import Thread

url = input("Paste video link : ")
location = {1:'/storage/emulated/0/1_BOOKS/COURT/Law Books/CPC_Videos'}
def path(url):
    for n ,s in location.items():
        print(f"{n} : {s}")
    loc = int(input('Location Number : '))
    global f.path
    f_path = location[loc]
    


yt = YouTube(url, use_oauth=True,allow_oauth_cache=True)
yt =yt.streams

'\n\n'
for i in yt:
    print(f'{i} \n')

itag = int(input('Enter the itag : '))

print('Downloading.......')
stream = yt.get_by_itag(itag)
stream.download(output_path=f_path)
print('Video downloaded')