from queue import Queue, LifoQueue
from threading import Event, Thread

from flaskapp.omx_runner import OMXRunner


class Player:

    def __init__(self):
        # Events
        self.exit_event = Event()
        self.next_event = Event()
        self.previous_event = Event()
        # Music queues
        self.current_music_queue = Queue()
        self.next_musics_queue = Queue()
        self.previous_musics_queue = LifoQueue()
        # OMX Player instantiation
        self.omx_runner = OMXRunner(self.current_music_queue, self.next_musics_queue, self.previous_musics_queue,
                                    self.exit_event, self.next_event, self.previous_event)
        self.runner_thread = Thread(target=self.omx_runner.run)
        self.runner_thread.start()

    def __del__(self):
        self.exit_event.set()

    def go_next(self):
        self.next_event.set()

    def go_previous(self):
        self.previous_event.set()
