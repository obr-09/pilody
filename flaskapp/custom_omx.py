from omxplayer.player import OMXPlayer
from random import shuffle


class CustomOMX:

    def __init__(self):
        self.videos_data = None
        self.player = None

    def set_video(self, video_data):
        self.videos_data = {0: video_data}
        if self.player and self.player.can_quit():
            self.player.quit()
        self.player = OMXPlayer(video_data.audio_url)
        self.player.stopEvent = self.stop_listener

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

    def get_state(self):
        return self.player.playback_status() if self.player else 'stopped'

    def play(self):
        if self.player and self.player.can_play():
            self.player.play()

    def stop(self):
        if self.player and self.player.can_quit():
            self.player.quit()
            self.player = None

    def toggle_pause(self):
        if self.player and self.player.can_pause():
            self.player.play_pause()

    def previous(self):
        pass

    def next(self):
        pass

    def stop_listener(self):
        from flaskapp.youtube_utility import YoutubeUtility
        self.player = OMXPlayer(YoutubeUtility.get_youtube_video('https://www.youtube.com/watch?v=YixAD9GIAuY'))
