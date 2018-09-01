from omxplayer.player import OMXPlayer
from random import shuffle


class CustomOMX:

    def __init__(self):
        self.videos_data = None
        self.player = None

    def set_audio(self, url):
        if self.player and self.player.can_quit():
            self.player.quit()
        self.player = OMXPlayer(url)
        self.player.pause()

    def get_state(self):
        return self.player.playback_status() if self.player else 'stopped'

    def play(self):
        if self.player and self.player.can_play():
            self.player.play_sync()

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
