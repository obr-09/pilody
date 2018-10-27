import pafy
from youtube_dl.utils import YoutubeDLError


class YoutubeUtility:

    @staticmethod
    def get_youtube_video(youtube_url):
        video = pafy.new(youtube_url)
        video.audio_url = video.getbestaudio().url
        return video

    @staticmethod
    def get_youtube_playlist(playlist_url):
        video_list = pafy.get_playlist2(playlist_url)
        for video in video_list:
            try:
                video.audio_url = video.getbestaudio().url
            except Exception:
                video.audio_url = None
        return video_list
