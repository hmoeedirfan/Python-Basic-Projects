# First Write download pip install pytube3 on terminal
from pytube import YouTube

# Getting url from User
video_link = str(input('Enter your youtube video URL: '))

# Add location where downloaded video goes 
saved_location = r'C:\Users\CUTY COMPUTER\Desktop'

# Downloading Youtube video using pytube3
try:
    # Converting yt video link to url
    url = YouTube(video_link)
    # Changing Youtube resolution
    video = url.streams.get_highest_resolution()
    # Adding location for savinvg video!
    video.download(saved_location)
    # Finally Successfull Message
    print('Congratulations, Your video is downloaded successfully!')
except:
    print('Something went wrong!')

