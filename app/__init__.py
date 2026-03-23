import os

from flasgger import Swagger
from flask import Flask, jsonify, send_file
from flask_cors import CORS

from app.api.v1_routes import blueprint as v1_routes
from app.demo_routes import blueprint as demo_routes
from app.user_routes import blueprint as user_routes

app = Flask(__name__)
app.register_blueprint(demo_routes)
app.register_blueprint(user_routes, url_prefix="/user")
app.register_blueprint(v1_routes)
CORS(app)
Swagger(
    app,
    config={
        "specs": [{"endpoint": "swagger", "route": "/swagger.json"}],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs",
        "headers": [],
    },
)


# Serve index.html at the root


@app.route("/")
def index():
    file_path = os.path.join(app.root_path, "..", "wwwroot", "index.html")
    return send_file(file_path)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})
