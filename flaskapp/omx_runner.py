from time import sleep

from dbus.exceptions import DBusException
from omxplayer.player import OMXPlayer, OMXPlayerDeadError

from flaskapp.youtube_utility import YoutubeUtility


class OMXRunner:

    def __init__(self, current_queue, next_queue, previous_queue, exit_event, play_pause_event, next_event, previous_event):
        # Setting events
        self.exit_event = exit_event
        self.play_pause_event = play_pause_event
        self.next_event = next_event
        self.previous_event = previous_event
        # Setting music queues
        self.current_music = current_queue
        self.next_musics = next_queue
        self.previous_musics =  previous_queue
        # Setting OMX
        self.omx = None

    def run(self):
        while not self.exit_event.is_set():
            sleep(0.1)
            if self.play_pause_event.is_set():
                self.play_pause()
                self.play_pause_event.clear()
            if self.next_event.is_set():
                self.go_next()
                self.next_event.clear()
            if self.previous_event.is_set():
                self.go_back()
                self.previous_event.clear()
            self.try_next()

    def stop(self):
        if self.omx:
            self.omx.quit()
            self.omx = None

    def play_pause(self):
        if self.omx:
            self.omx.play_pause()
        else:
            current_music_queue = list(self.current_music)
            current_music = current_music_queue[0] if current_music_queue else None
            if current_music:
                self.omx = OMXPlayer(current_music['url'])

    def go_next(self):
        next_music = self.next_musics.get_nowait()
        if next_music:
            self.stop()
            current_music = self.current_music.get_nowait()
            if current_music:
                self.previous_musics.put(current_music)
            self.current_music.put(next_music)
            self.play_pause()
        else:
            current_music = self.current_music.get_nowait()
            if current_music:
                next_video_url = YoutubeUtility.get_youtube_next_video_url(current_music['url'])
                video_data = YoutubeUtility.get_youtube_video(next_video_url)
                if video_data:
                    self.current_music.put({'url': video_data.audio_url, 'title': video_data.title, 'author': video_data.author})

    def go_back(self):
        previous_music = self.previous_musics.get_nowait()
        if previous_music:
            self.stop()
            current_music = self.current_music.get_nowait()
            if current_music:
                # TODO: Need reordering here
                self.next_musics.put(current_music)
            self.current_music.put(previous_music)
            self.play_pause()

    def try_next(self):
        try:
            if (not self.omx or self.omx.playback_status() == 'Stopped'):
                self.go_next()
        except (OMXPlayerDeadError, DBusException):
            self.go_next()
