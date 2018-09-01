import pafy


class YoutubeUtility:

    @staticmethod
    def get_youtube_video(youtube_url):
        video = pafy.new(youtube_url)
        audio_stream = video.getbestaudio()
        video.audio_url = audio_stream.url
        return video

    @staticmethod
    def get_youtube_playlist(playlist_url):
        video_list = pafy.get_playlist2(playlist_url)
        for video in video_list:
            video.audio_url = video.getbestaudio().url
        return video_list
