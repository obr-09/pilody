from flask_restful_swagger_2 import Schema


class MessageModel(Schema):
    type = 'object'
    properties = {
        'message': {
            'type': 'string'
        }
    }


class YoutubeUrlSchema(Schema):
    type = 'object'
    properties = {
        'youtube_url': {
            'type': 'string'
        }
    }


class PlaylistUrlSchema(Schema):
    type = 'object'
    properties = {
        'playlist_url': {
            'type': 'string'
        }
    }


class MusicActionSchema(Schema):
    type = 'object'
    properties = {
        'action': {
            'type': 'string'
        }
    }


class MusicInfoSchema(Schema):
    type = 'object',
    properties = {
        'url': {
            'type': 'string'
        },
        'title': {
            'type': 'string'
        },
        'artist': {
            'type': 'string'
        }
    }
