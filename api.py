from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def test():
    return 'interface'


@app.route('/state', methods=['GET'])
def get_state():
    return 'playing'


@app.route('/state', methods=['POST'])
def change_state():
    action = request.form['action']
    if action == 'play':
        pass
    elif action == 'pause':
        pass
    elif action == 'stop':
        pass
    else:
        pass
    return action
