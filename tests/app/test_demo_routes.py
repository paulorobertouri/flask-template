import pytest
from flask import Flask

from app.demo_routes import blueprint


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(blueprint, url_prefix="/demo")
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_message_morning(client):
    response = client.get("/demo/hello/Alice/8")
    assert response.status_code == 200
    assert response.get_json()["message"].startswith("Good morning, Alice!")


def test_get_message_afternoon(client):
    response = client.get("/demo/hello/Bob/14")
    assert response.status_code == 200
    assert response.get_json()["message"].startswith("Good afternoon, Bob!")


def test_get_message_evening(client):
    response = client.get("/demo/hello/Carol/20")
    assert response.status_code == 200
    assert response.get_json()["message"].startswith("Good evening, Carol!")


def test_get_message_evening_at_midnight(client):
    response = client.get("/demo/hello/Carol/0")
    assert response.status_code == 200
    assert response.get_json()["message"].startswith("Good evening, Carol!")


def test_get_message_hour_zero(client):
    response = client.get("/demo/hello/Dave")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello, Dave!"
