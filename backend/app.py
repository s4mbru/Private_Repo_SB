from flask import Flask, request, jsonify
from flask_cors import CORS

from private import (
    drawLine,
    drawWavyLine,
    drawTriangle,
    drawCircle,
    reportWeather,
    obsCheck
)
from BirdBrain import Finch

app = Flask(__name__)
CORS(app)

# Set up Finch once
finch = Finch('A')
speed = 20
distance = 100

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    action = data.get("action")

    try:
        if action == "line":
            drawLine(finch, speed, distance)
        elif action == "wave":
            drawWavyLine(finch, speed, distance)
        elif action == "triangle":
            drawTriangle(finch, speed, distance)
        elif action == "circle":
            drawCircle(finch, speed, distance)
        elif action == "temperature":
            reportWeather(finch)
        elif action == "forward":
            obsCheck(finch)
            finch.setMove('F', speed, distance)
        elif action == "left":
            obsCheck(finch)
            finch.setTurn('L', 95, 30)
        elif action == "right":
            obsCheck(finch)
            finch.setTurn('R', 95, 30)
        elif action == "down":
            obsCheck(finch)
            finch.setTurn('R', 185, 30)
        else:
            return jsonify({"error": "Unknown action"}), 400

        return jsonify({"status": "success", "action": action})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
