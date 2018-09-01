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
