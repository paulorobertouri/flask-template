import os

from flask import Flask, send_file
from flask_cors import CORS

from app.demo_routes import blueprint as demo_routes
from app.user_routes import blueprint as user_routes

app = Flask(__name__)
app.register_blueprint(demo_routes)
app.register_blueprint(user_routes, url_prefix="/user")
CORS(app)


# Serve index.html at the root


@app.route("/")
def index():
    return send_file(os.path.join(app.root_path, "..", "wwwroot", "index.html"))
