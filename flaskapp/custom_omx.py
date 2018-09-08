from queue import Queue, Empty, LifoQueue
from threading import Event, Thread
from time import sleep

from dbus.exceptions import DBusException
from omxplayer.player import OMXPlayer, OMXPlayerDeadError


class CustomOMX:

    def __init__(self):
        self.previous_musics = LifoQueue()
        self.next_musics = Queue()
        self.current_music_queue = Queue()
        self.pause_event = Event()
        self.previous_event = Event()
        self.next_event = Event()
        self.stop_event = Event()
        self.exit_event = Event()
        self.omx_runner = OMXRunner(self.previous_musics, self.next_musics, self.current_music_queue, self.pause_event,
                                    self.previous_event, self.next_event, self.stop_event, self.exit_event)
        self.player_thread = Thread(target=self.omx_runner.run)
        self.player_thread.start()

    def __del__(self):
        self.exit_event.set()

    def set_audio(self, url, title, artist):
        self.empty_queue(self.next_musics)
        self.stop_event.set()
        self.next_musics.put({'url': url, 'title': title, 'artist': artist})
        self.pause_event.set()

    def add_audio(self, url, title, artist):
        self.next_musics.put({'url': url, 'title': title, 'artist': artist})

    def set_playlist(self, music_list):
        self.empty_queue(self.next_musics)
        self.stop_event.set()
        for music in music_list:
            self.next_musics.put({'url': music['url'], 'title': music['title'], 'artist': music['artist']})
        self.pause_event.set()

    def stop(self):
        self.stop_event.set()

    def toggle_pause(self):
        self.pause_event.set()

    def previous(self):
        try:
            previous_music = self.previous_musics.get(False)
        except Empty:
            previous_music = None
        if previous_music:
            next_musics = self.empty_queue(self.next_musics)
            next_musics.insert(0, previous_music)
            self.set_playlist(next_musics)
            self.previous_event.set()

    def next(self):
        self.next_event.set()

    def get_music(self):
        try:
            music = self.current_music_queue.get_nowait()
            self.current_music_queue.put(music)
        except Empty:
            music = None
        return music

    def empty_queue(self, queue):
        queue_content = []
        try:
            queue_element = queue.get(False)
            while queue_element:
                queue_content.append(queue_element)
                queue_element = queue.get(False)
        except Empty:
            pass
        return queue_content


class OMXRunner:

    def __init__(self, previous_musics, next_musics, current_music_queue, pause_event, previous_event, next_event,
                 stop_event, exit_event):
        self.previous_musics = previous_musics
        self.next_musics = next_musics
        self.current_music_queue = current_music_queue
        self.pause_event = pause_event
        self.previous_event = previous_event
        self.next_event = next_event
        self.stop_event = stop_event
        self.exit_event = exit_event
        self.player = None
        self.current_music = None

    def run(self):
        while not self.exit_event.is_set():
            sleep(0.05)
            if self.stop_event.is_set():
                self.stop()
            elif self.pause_event.is_set():
                self.play_pause()
            if self.previous_event.is_set():
                self.previous()
            if self.next_event.is_set():
                self.next()
            self.try_next()

    def play_pause(self):
        self.stop_event.clear()
        if self.player:
            self.player.play_pause()
        elif self.current_music:
            self.player = OMXPlayer(self.current_music['url'])
        self.pause_event.clear()

    def stop(self):
        if self.player:
            self.player.quit()
            self.player = None

    def previous(self):
        self.stop_event.clear()
        self.stop()
        musics_queued = [self.current_music] if self.current_music else []
        try:
            self.current_music = self.next_musics.get_nowait()
            # self.current_music_queue.get_nowait()
            music_queued = self.next_musics.get_nowait()
            while music_queued:
                musics_queued.append(music_queued)
                music_queued = self.next_musics.get_nowait()
        except Empty:
            pass
        for music in musics_queued:
            self.next_musics.put(music)
        if self.current_music:
            # self.current_music_queue.put(self.current_music)
            self.player = OMXPlayer(self.current_music['url'])
        self.previous_event.clear()

    def next(self):
        self.stop_event.clear()
        self.stop()
        if self.current_music:
            self.previous_musics.put_nowait(self.current_music)
        try:
            self.current_music = self.next_musics.get_nowait()
            # self.current_music_queue.get_nowait()
        except Empty:
            pass
        if self.current_music:
            self.player = OMXPlayer(self.current_music['url'])
            # self.current_music_queue.put(self.current_music)
        self.next_event.clear()

    def try_next(self):
        try:
            if (not self.player or self.player.playback_status() == 'Stopped') and not self.pause_event.is_set() and \
                    not self.stop_event.is_set():
                self.next()
        except (OMXPlayerDeadError, DBusException):
            self.next()
