from time import sleep


class OMXRunner:

    def __init__(self, current_queue, next_queue, previous_queue, exit_event, next_event, previous_event):
        # Setting events
        self.exit_event = exit_event
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
            if self.next_event.is_set():
                self.go_next()
                self.next_event.clear()
            if self.previous_event.is_set():
                self.go_back()
                self.previous_event.clear()


    def go_next(self):
        next_music = self.next_musics.get_nowait()
        if next_music:
            current_music = self.current_music.get_nowait()
            if current_music:
                self.previous_musics.put(current_music)
            self.current_music.put(next_music)

    def go_back(self):
        previous_music = self.previous_musics.get_nowait()
        if previous_music:
            current_music = self.current_music.get_nowait()
            if current_music:
                # Need reordering here
                self.next_musics.put(current_music)
            self.current_music.put(previous_music)
