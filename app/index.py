from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/me/<name>/<int:hour>")
def get_message(name, hour):
    if not hour:
        greeting = "Hello"
    elif hour >= 18 or hour < 6:
        greeting = "Good evening"
    elif hour >= 12:
        greeting = "Good afternoon"
    else:
        greeting = "Good morning"

    if not hour:
        return jsonify({"message": f"{greeting}, {name}!"})
    return jsonify(
        {
            "message": f"{greeting}, {name}! Now it's {hour} o'clock.",
        },
    )
