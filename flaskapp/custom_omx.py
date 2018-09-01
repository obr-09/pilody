from queue import Queue, Empty
from threading import Event, Thread
from time import sleep

from omxplayer.player import OMXPlayer


class CustomOMX:

    def __init__(self):
        self.music_queue = Queue()
        self.previous_queue = Queue()
        self.pause_event = Event()
        self.stop_event = Event()
        self.player_thread = Thread(target=CustomOMX.run_music,
                                    args=(self.music_queue, self.previous.queue, self.pause_event, self.stop_event))
        self.player_thread.start()

    def set_audio(self, url):
        self.empty_queue()
        self.stop_event.set()
        self.music_queue.put(url)

    def add_audio(self, url):
        self.music_queue.put(url)

    def set_playlist(self, url_list):
        self.empty_queue()
        self.stop_event.set()
        for url in url_list:
            self.music_queue.put(url)

    def stop(self):
        self.empty_queue()
        self.stop_event.set()

    def toggle_pause(self):
        self.pause_event.set()

    def previous(self):
        pass

    def next(self):
        self.stop_event.set()

    def empty_queue(self):
        try:
            while self.music_queue.get(False):
                pass
        except Empty:
            pass

    @staticmethod
    def run_music(music_queue, previous_queue, pause_event, stop_event):
        while True:
            music = music_queue.get(True)
            stop_event.clear()
            pause_event.clear()
            player = OMXPlayer(music)
            while player and (player.is_playing or player.can_play()):
                sleep(0.05)
                if pause_event.is_set():
                    player.play_pause()
                    pause_event.clear()
                if stop_event.is_set():
                    player.quit()
                    player = None
                    stop_event.clear()

