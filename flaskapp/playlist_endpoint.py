from flask import current_app, request, abort
from flask_restful import Resource

from flaskapp.custom_vlc import CustomVLC


class PlaylistEndpoint(Resource):

    def get(self):
        return current_app.config['vlc'].get_playlist_info()

    def post(self):
        playlist_url = request.form['playlist_url']
        if playlist_url:
            videos_data = CustomVLC.get_youtube_playlist(playlist_url)
            current_app.config['vlc'].set_playlist(videos_data)
            return current_app.config['vlc'].get_playlist_info()
        else:
            return {'error': 'Expected "playlist_url" parameter'}, 400
