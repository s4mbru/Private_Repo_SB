from flask import Flask
from flask_socketio import SocketIO, emit
from private import (
    drawLine,
    drawWavyLine,
    drawTriangle,
    drawCircle,
    reportWeather,
    obsCheck,
)
from lib.BirdBrain import Finch

TOTALLY_SECURE_KEY = 'meow'
PORT = 5555

socketio = SocketIO(
    cors_allowed_origins='*',
    transports=['websocket'],
    ping_interval=3,
)

#Finch reference
FINCH_DEVICE = 'A'
DEFAULT_SPEED = 20
DEFAULT_DISTANCE = 100
finch = None


def configure():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = TOTALLY_SECURE_KEY
    socketio.init_app(app)

    return app


def get_finch():
    """Create the Finch only when needed"""

    global finch

    if finch is None:
        finch = Finch(FINCH_DEVICE)

    return finch


@socketio.on('connect')
def test_connect():

    emit('status', {'message': 'Frontend connected to backend'})
    print('Frontend connected')


@socketio.on('disconnect')
def test_disconnect():

    print('Frontend disconnected')


@socketio.on('finch_test')
def finch_test():
    """Optional quick test button"""

    try:
        robot = get_finch()
        robot.setMove('F', 100, 100)
        robot.setTurn('R', 360, 30)
        emit('status', {'message': 'Finch test completed'})

    except Exception as e:
        emit('error', {'message': f'Finch test failed: {str(e)}'})


@socketio.on('run_command')
def run_command(data):
    """Receives commands from the frontend
    Expected format: { "command": "line" }"""
    
    command = data.get('command') if data else None

    try:
        robot = get_finch()
        if command == 'line':
            drawLine(robot, DEFAULT_SPEED, DEFAULT_DISTANCE)
        elif command == 'wave':
            drawWavyLine(robot, DEFAULT_SPEED, DEFAULT_DISTANCE)
        elif command == 'triangle':
            drawTriangle(robot, DEFAULT_SPEED, DEFAULT_DISTANCE)
        elif command == 'circle':
            drawCircle(robot, DEFAULT_SPEED, DEFAULT_DISTANCE)
        elif command == 'temperature':
            reportWeather(robot)
        elif command == 'forward':
            obsCheck(robot)
            robot.setMove('F', DEFAULT_SPEED, DEFAULT_DISTANCE)
        elif command == 'left':
            obsCheck(robot)
            robot.setTurn('L', 95, 30)
        elif command == 'right':
            obsCheck(robot)
            robot.setTurn('R', 95, 30)
        elif command == 'turnaround':
            obsCheck(robot)
            robot.setTurn('R', 185, 30)
        else:
            emit('error', {'message': f'Unknown command: {command}'})
            return

        emit('status', {'message': f'Command "{command}" completed'})
        print(f'Ran command: {command}')

    except Exception as e:
        emit('error', {'message': f'Command failed: {str(e)}'})
        print(f'Command failed: {command} -> {e}')


if __name__ == '__main__':
    app = configure()
    socketio.run(app, host="0.0.0.0", port=PORT, debug=True)
