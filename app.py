#Script for frontend to backend taken from sample repository app.py
from flask import Flask
from flask_socketio import SocketIO
from lib.BirdBrain import Finch

TOTALLY_SECURE_KEY = 'meow'
PORT = 5555

socketio = SocketIO(cors_allowed_origins='*', transport=['websocket'], ping_interval=3)

def configure():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = TOTALLY_SECURE_KEY
    socketio.init_app(app)
    return app

@socketio.on('connect')
def test_connect():
    socketio.emit('connected?')

@socketio.on('disconnect')
def test_disconnect():
    socketio.emit('disconnected?')

@socketio.on('finch_test')
def finch_test():
    finch = Finch('A')
    finch.setMove('F', 100, 100)
    finch.setTurn('R', 360, 30)

if __name__ == '__main__':
    app = configure()
    socketio.run(app, port=PORT)
