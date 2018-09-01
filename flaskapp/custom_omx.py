import pafy
from omxplayer.player import OMXPlayer
from random import shuffle
from vlc import Instance


class CustomOMX:

    @staticmethod
    def get_youtube_video(youtube_url):
        video = pafy.new(youtube_url)
        stream = video.getbest()
        video.url = stream.url
        return video

    @staticmethod
    def get_youtube_playlist(playlist_url):
        return pafy.get_playlist2(playlist_url)

    def __init__(self):
        self.videos_data = None
        self.player = None

    def set_video(self, video_data):
        self.videos_data = {0: video_data}
        self.player = OMXPlayer(video_data.url)

    def set_playlist(self, videos_data):
        pass

    def get_playlist_info(self):
        return {
            'title': self.videos_data.title if self.videos_data.title else '',
            'author': self.videos_data.author if self.videos_data.author else '',
            'description': self.videos_data.description if self.videos_data.description else '',
            'length': len(self.videos_data)
        }

    def get_music_info(self):
        raise NotImplementedError

    def play(self):
        if self.player:
            self.player.play()

    def stop(self):
        if self.player:
            self.player.quit()

    def toggle_pause(self):
        if self.player:
            self.player.play_pause()

    def previous(self):
        pass

    def next(self):
        pass
