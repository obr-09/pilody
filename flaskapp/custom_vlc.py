import pafy
import vlc


class CustomVLC():

    def __init__(self):
        self.video = None
        self.stream = None
        self.video_url = None
        self.player = None
        self.set_youtube_video('https://www.youtube.com/watch?v=YixAD9GIAuY')

    def set_youtube_video(self, url):
        self.youtube_url = url
        self.video = pafy.new(self.youtube_url)
        self.stream = self.video.getbest()
        self.video_url = self.stream.url
        if self.player:
            self.player.stop()
            self.play()

    def play(self):
        if self.video_url:
            self.player = vlc.MediaPlayer(self.video_url)
            self.player.play()

    def resume(self):
        if self.player:
            self.player.play()

    def pause(self):
        if self.player:
            self.player.pause()

    def stop(self):
        if self.player:
            self.player.stop()
        self.player = None
