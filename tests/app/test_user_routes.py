from unittest.mock import MagicMock, patch

import pytest
from flask import Flask

from app.user.models import User, UserRequest
from app.user_routes import blueprint


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(blueprint, url_prefix="/users")
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_all_users(client):

    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.get_all.return_value = [
            User(id=1, name="Test", email="test@test.com"),
        ]
        mock_get_db.return_value = mock_db
        resp = client.get("/users/")
        assert resp.status_code == 200
        assert resp.get_json() == [
            {"id": 1, "name": "Test", "email": "test@test.com"},
        ]


def test_get_user_not_found(client):
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.get.return_value = None
        mock_get_db.return_value = mock_db
        resp = client.get("/users/123")
        assert resp.status_code == 404
        assert resp.get_json()["error"] == "User not found"


def test_create_user_invalid_request(client):
    resp = client.post("/users/", json={})
    assert resp.status_code == 400
    assert resp.get_json()["error"] == "Invalid request"


def test_create_user_duplicate_email(client):
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.email_exists.return_value = True
        mock_get_db.return_value = mock_db
        resp = client.post(
            "/users/",
            json={"name": "Test", "email": "test@test.com"},
        )
        assert resp.status_code == 409
        assert resp.get_json()["error"] == "Email already exists"


def test_delete_user_not_found(client):
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.exists.return_value = False
        mock_get_db.return_value = mock_db
        resp = client.delete("/users/123")
        assert resp.status_code == 404
        assert resp.get_json()["error"] == "User not found"


def test_get_database_returns_user_database():
    with patch("app.user_routes.UserDatabase") as mock_user_db:
        from app.user_routes import get_database

        db_instance = MagicMock()
        mock_user_db.return_value = db_instance
        db = get_database()
        assert db is db_instance


def test_get_user_success(client):
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.get.return_value = User(
            id=1,
            name="Test",
            email="test@test.com",
        )
        mock_get_db.return_value = mock_db
        resp = client.get("/users/1")
        assert resp.status_code == 200
        assert resp.get_json() == {
            "id": 1,
            "name": "Test",
            "email": "test@test.com",
        }


def test_create_user_success(client):
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.email_exists.return_value = False
        mock_db.create.return_value = User(
            id=2,
            name="Test2",
            email="test2@test.com",
        )
        mock_get_db.return_value = mock_db
        resp = client.post(
            "/users/",
            json={"name": "Test2", "email": "test2@test.com"},
        )
        assert resp.status_code == 201
        assert resp.get_json() == {
            "id": 2,
            "name": "Test2",
            "email": "test2@test.com",
        }


def test_update_user_not_found(client):
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.exists.return_value = False
        mock_get_db.return_value = mock_db
        resp = client.put("/users/123", json={"name": "New Name"})
        assert resp.status_code == 404
        assert resp.get_json()["error"] == "User not found"


def test_update_user_invalid_request(client):
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.exists.return_value = True
        mock_get_db.return_value = mock_db
        resp = client.put("/users/1", json={})
        assert resp.status_code == 400
        assert resp.get_json()["error"] == "Invalid request"


def test_update_user_email_exists(client):
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.exists.return_value = True
        mock_db.email_exists.return_value = True
        mock_get_db.return_value = mock_db
        resp = client.put("/users/1", json={"email": "exists@test.com"})
        assert resp.status_code == 409
        assert resp.get_json()["error"] == "Email already exists"


def test_update_user_success(client):
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.exists.return_value = True
        mock_db.email_exists.return_value = False
        mock_db.update.return_value = User(
            id=1,
            name="Updated",
            email="updated@test.com",
        )
        mock_get_db.return_value = mock_db
        resp = client.put(
            "/users/1",
            json={"name": "Updated", "email": "updated@test.com"},
        )
        assert resp.status_code == 200
        assert resp.get_json() == {
            "id": 1,
            "name": "Updated",
            "email": "updated@test.com",
        }


def test_userrequest_from_dict():
    data = {"name": "Test", "email": "test@test.com"}
    req = UserRequest.from_dict(data)
    assert req.name == "Test"
    assert req.email == "test@test.com"


def test_delete_user_success(client):
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.exists.return_value = True
        mock_get_db.return_value = mock_db
        resp = client.delete("/users/1")
        assert resp.status_code == 200
        assert resp.get_json()["message"] == "User deleted"


def test_create_user_failure(client):
    """Test user creation returns 500 if database.create returns None."""
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.email_exists.return_value = False
        mock_db.create.return_value = None
        mock_get_db.return_value = mock_db
        resp = client.post(
            "/users/",
            json={"name": "Fail", "email": "fail@test.com"},
        )
        assert resp.status_code == 500
        assert resp.get_json()["error"] == "User could not be created"


def test_update_user_update_returns_none(client):
    """Test update returns 404 if database.update returns None."""
    with patch("app.user_routes.get_database") as mock_get_db:
        mock_db = MagicMock()
        mock_db.exists.return_value = True
        mock_db.email_exists.return_value = False
        mock_db.update.return_value = None
        mock_get_db.return_value = mock_db
        resp = client.put(
            "/users/1",
            json={"name": "NoUpdate", "email": "nouser@test.com"},
        )
        assert resp.status_code == 404
        assert resp.get_json()["error"] == "User not found"
