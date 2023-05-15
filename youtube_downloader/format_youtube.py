from pytube import YouTube

#link = input('Enter youtube video link')
link = "https://youtube.com/shorts/aM29U4J4yvY?feature=share"
yt = YouTube(link)
streams = yt.streams
def format(s):
  print("=" * 65)    

  print(

  'SN'.rjust(3), 
  'itag'.center(4), 
  'res'.center(5), 
  'abr'.center(8), 
  'mime_type'.center(11), 
  'Prograssive'.center(12), 
  'type'.center(4),
  'size'.ljust(6)

  )

  print("=" * 65)



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
      s.mime_type.center(11), 
      str(is_progressive).center(12), 
      type.center(4),
      size.ljust(6)
    
      )
    
      print("_" * 65)
      
format(streams)
    