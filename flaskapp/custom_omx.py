from queue import Queue, Empty, LifoQueue
from threading import Event, Thread
from time import sleep

from omxplayer.player import OMXPlayer


class CustomOMX:

    def __init__(self):
        self.music_queue = Queue()
        self.previous_queue = LifoQueue()
        self.pause_event = Event()
        self.stop_event = Event()
        self.player_thread = Thread(target=CustomOMX.run_music,
                                    args=(self.music_queue, self.previous_queue, self.pause_event, self.stop_event))
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
        previous_music = self.previous_queue.get(False)
        if previous_music:
            next_musics = self.empty_queue()
            next_musics.insert(0, previous_music)
            self.set_playlist(next_musics)

    def next(self):
        self.stop_event.set()

    def empty_queue(self):
        queue_content = []
        try:
            queue_element = self.music_queue.get(False)
            while queue_element:
                queue_content.append(queue_element)
        except Empty:
            pass
        return queue_content

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
            previous_queue.put(music)
