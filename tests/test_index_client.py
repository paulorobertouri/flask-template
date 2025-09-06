import pytest

from app.index import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.data == b"Hello, World!"


def test_get_message(client):
    response = client.get("/me/Alice/10")
    assert response.json == {
        "message": "Good morning, Alice! Now it's 10 o'clock.",
    }

    response = client.get("/me/Bob/15")
    assert response.json == {
        "message": "Good afternoon, Bob! Now it's 15 o'clock.",
    }

    response = client.get("/me/Charlie/20")
    assert response.json == {
        "message": "Good evening, Charlie! Now it's 20 o'clock.",
    }

    response = client.get("/me/Diana/5")
    assert response.json == {
        "message": "Good evening, Diana! Now it's 5 o'clock.",
    }

    response = client.get("/me/Eve/0")
    assert response.json == {"message": "Hello, Eve!"}
