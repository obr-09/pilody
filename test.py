import pafy
import vlc


youtube_url = 'https://www.youtube.com/watch?v=YixAD9GIAuY'
video = pafy.new(youtube_url)
stream = video.getbest()
video_url = stream.url

# print(video_url)
# player = vlc.MediaPlayer(video_url)
# player.play()
# while True:
#     pass
