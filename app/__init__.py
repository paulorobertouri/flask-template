import os
from flask import Flask, send_from_directory
from app.interface.api.v1.routes import v1_bp
from app.interface.api.health import health_bp


def create_app() -> Flask:
    app = Flask(__name__)

    # Static files for the demo client
    @app.route("/static/<path:path>")
    def send_static(path):
        return send_from_directory("../public", path)

    app.register_blueprint(health_bp)
    app.register_blueprint(v1_bp, url_prefix="/api/v1")

    return app
