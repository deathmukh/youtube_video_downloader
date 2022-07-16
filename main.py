from pytube import YouTube

youtube_link = input('Paste the link you want to download ====>>')

yt=YouTube(youtube_link)
# yt= YouTube('https://www.youtube.com/watch?v=Ls3Eorw10uU')
print(yt.title)

streams_dict = {}
index=1
for stream in yt.streams:
    streams_dict[index]=stream
    print(index,stream)
    index += 1
    
stream_to_download = int(input('PLEASE ENTER A NUMBER =====>'))


if streams_dict.get(stream_to_download) == None:
    print('enter a valid key')
else:
    url = streams_dict[stream_to_download]
    url.download()


    
    