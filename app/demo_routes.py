from flask import Blueprint, jsonify

blueprint = Blueprint("Demo's routes", __name__)


@blueprint.route("/hello/<name>")
def get_message(name):
    return jsonify({"message": f"Hello, {name}!"})


@blueprint.route("/hello/<name>/<int:hour>")
def get_message_with_hour(name, hour):
    if hour >= 18 or hour < 6:
        greeting = "Good evening"
    elif hour >= 12:
        greeting = "Good afternoon"
    else:
        greeting = "Good morning"
    return jsonify({"message": f"{greeting}, {name}! Now it's {hour} o'clock."})
