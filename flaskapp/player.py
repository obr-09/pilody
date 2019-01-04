from queue import Empty, Queue, LifoQueue
from threading import Event, Thread

from flaskapp.omx_runner import OMXRunner


class Player:

    def __init__(self):
        # Events
        self.exit_event = Event()
        self.play_pause_event = Event()
        self.next_event = Event()
        self.previous_event = Event()
        # Music queues
        self.current_music_queue = Queue()
        self.next_musics_queue = Queue()
        self.previous_musics_queue = LifoQueue()
        # OMX Player instantiation
        self.omx_runner = OMXRunner(self.current_music_queue, self.next_musics_queue, self.previous_musics_queue,
                                    self.exit_event, self.play_pause_event, self.next_event, self.previous_event)
        self.runner_thread = Thread(target=self.omx_runner.run)
        self.runner_thread.start()

    def __del__(self):
        self.exit_event.set()

    def go_next(self):
        self.next_event.set()

    def go_previous(self):
        self.previous_event.set()

    def add_music(self, music):
        self.next_musics_queue.put(music)

    def get_music(self):
        music_queue = list(self.current_music_queue)
        return music_queue[0] if music_queue else None

    def set_music(self, music):
        Player.empty_queue(self.next_musics_queue)
        previous_music = self.current_music_queue.get_nowait()
        if previous_music:
            self.previous_musics_queue.put(previous_music)
        self.current_music_queue.put(music)

    def set_playlist(self, music_list):
        Player.empty_queue(self.next_musics_queue)
        for music in music_list:
            self.next_musics_queue.put(music)

    @staticmethod
    def empty_queue(queue):
        queue_content = []
        try:
            queue_element = queue.get(False)
            while queue_element:
                queue_content.append(queue_element)
                queue_element = queue.get(False)
        except Empty:
            pass
        return queue_content
