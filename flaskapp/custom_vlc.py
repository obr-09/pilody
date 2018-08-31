import pafy
import vlc


class CustomVLC():

    def __init__(self):
        self.youtube_url = 'https://www.youtube.com/watch?v=YixAD9GIAuY'
        self.video = pafy.new(self.youtube_url)
        self.stream = self.video.getbest()
        self.video_url = self.stream.url
        self.player = None

    def play(self):
        self.player = vlc.MediaPlayer(self.video_url)
        self.resume()

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
