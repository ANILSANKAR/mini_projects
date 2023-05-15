import urllib.request

url = input ('Enter the url : ') # Replace with the URL of the file you want to download
filename = input('Enter file name : ') # Replace with the name you want to save the file as

# Use urllib.request.urlretrieve() to download the file from the URL
urllib.request.urlretrieve(url, filename)
