from os import path

from flask import Blueprint, jsonify, request

from app.user.database import UserDatabase
from app.user.models import UserRequest

blueprint = Blueprint("User's routes", __name__)


def get_database():
    data_folder = path.join(path.dirname(__file__), "..", "..", ".data")
    return UserDatabase(db_path=path.join(data_folder, "users.db"))


@blueprint.route("/", methods=["GET"])
def get_all():
    database = get_database()
    list = database.get_all()
    return jsonify([item.to_dict() for item in list])


@blueprint.route("/<int:id>", methods=["GET"])
def get(id):
    database = get_database()
    model = database.get(id)
    if model is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(model.to_dict())


@blueprint.route("/", methods=["POST"])
def create():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid request"}), 400
    database = get_database()
    if database.email_exists(data["email"]):
        return jsonify({"error": "Email already exists"}), 409

    rq = UserRequest(
        name=data["name"],
        email=data["email"],
    )
    model = database.create(rq)
    if model is None:
        return jsonify({"error": "User could not be created"}), 500
    return jsonify(model.to_dict()), 201


@blueprint.route("/<int:id>", methods=["PUT"])
def update(id):
    database = get_database()
    if not database.exists(id):
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    if not data or ("name" not in data and "email" not in data):
        return jsonify({"error": "Invalid request"}), 400
    if "email" in data and database.email_exists(data["email"], exclude_id=id):
        return jsonify({"error": "Email already exists"}), 409

    rq = UserRequest.from_dict(data)
    model = database.update(id, rq)
    if model is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(model.to_dict())


@blueprint.route("/<int:id>", methods=["DELETE"])
def delete(id):
    database = get_database()
    if not database.exists(id):
        return jsonify({"error": "User not found"}), 404
    database.delete(id)
    return jsonify({"message": "User deleted"})
