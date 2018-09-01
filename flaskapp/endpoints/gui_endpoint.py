from flask import current_app, request, render_template
from flask_restful import Resource


class GuiEndpoint(Resource):

    def get(self):
        return render_template('player.html')
