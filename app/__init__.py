from pathlib import Path

from flasgger import Swagger
from flask import Flask, send_from_directory

from app.interface.api.health import health_bp
from app.interface.api.v1.routes import v1_bp


def create_app() -> Flask:
    app = Flask(__name__, static_folder=None)

    # Static files for the demo client
    public_dir = str(Path(__file__).parent.parent / "public")

    @app.route("/static/<path:path>")
    def send_static(path):
        return send_from_directory(public_dir, path)

    app.register_blueprint(health_bp)
    app.register_blueprint(v1_bp, url_prefix="/v1")

    Swagger(
        app,
        config={
            "headers": [],
            "specs": [
                {
                    "endpoint": "swagger",
                    "route": "/swagger.json",
                    "rule_filter": lambda rule: True,
                    "model_filter": lambda tag: True,
                }
            ],
            "static_url_path": "/flasgger_static",
            "swagger_ui": True,
            "specs_route": "/docs",
        },
    )

    return app


app = create_app()
