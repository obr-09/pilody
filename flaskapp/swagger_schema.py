from flask_restful_swagger_2 import Schema


class SuccessModel(Schema):
    type = 'object'
    properties = {
        'message': {
            'type': 'string'
        }
    }
