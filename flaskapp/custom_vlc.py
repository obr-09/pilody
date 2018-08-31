import pafy
from random import shuffle
from vlc import Instance


class CustomVLC:

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
        self.player = Instance()
        self.media_list_player = self.player.media_list_player_new()

    def set_video(self, video_data):
        self.videos_data = [video_data]
        media_list = self.player.media_list_new()
        media_list.add_media(self.player.media_new(video_data.url))
        self.media_list_player.set_media_list(media_list)

    def set_playlist(self, videos_data):
        self.videos_data = videos_data
        media_list = self.player.media_list_new()
        videos_url = []
        for video_data in videos_data:
            videos_url.append(video_data.getbest().url)
        shuffle(videos_url)
        for video_url in videos_url:
            media_list.add_media(self.player.media_new(video_url))
        self.media_list_player.set_media_list(media_list)

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
        self.media_list_player.play()

    def stop(self):
        self.media_list_player.stop()

    def toggle_pause(self):
        self.media_list_player.pause()

    def previous(self):
        self.media_list_player.previous()

    def next(self):
        self.media_list_player.next()
