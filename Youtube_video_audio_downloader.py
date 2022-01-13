from pytube import YouTube

# Taking Video url
url = input("Enter Url : ")

# Getting data of video
yt = YouTube(url)

my_streams = yt.streams

# # Formating file name
bad_character = '|'
name = yt.title.replace(bad_character,"")
name = " ".join(name.split())
print(name)

# for stream in my_streams:  # progressive = True, both video and audio
#     print(stream)          # progressive = False, only video or audio

v_a = int(input("1. Video\n2. Audio\n----> "))

if v_a == 1:
    v = int(input("1. 720p\n2. 360p\n----> "))
    if v == 1:
        my_streams.get_by_itag(22).download(filename=f"Download/{name}")
    elif v == 2:
        my_streams.get_by_itag(18).download(filename=f"Download/{name}")
    else :
        print("invalid input")

elif v_a == 2:
    my_streams.get_by_itag(140).download(filename=f"Download/{name}.mp4")


else:
    print("Invalid input")