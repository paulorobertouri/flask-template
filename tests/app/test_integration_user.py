import importlib
import os

import pytest
from flask import Flask


def get_db_file():
    # Match the app.user_routes.get_database() path logic
    data_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../.data"),
    )
    return os.path.join(data_folder, "users.db")


@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown_db():
    db_file = get_db_file()
    data_dir = os.path.dirname(db_file)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    # Remove DB before tests
    if os.path.exists(db_file):
        os.remove(db_file)
    yield
    # Remove DB after tests
    if os.path.exists(db_file):
        os.remove(db_file)


@pytest.fixture(scope="function")
def client(monkeypatch):
    """
    Flask test client fixture with patched user database for isolation.
    Uses monkeypatch to override get_database in app.user_routes,
    ensuring tests use a dedicated test DB file.
    """
    user_routes_mod = importlib.import_module("app.user_routes")

    def _get_database():
        return user_routes_mod.UserDatabase(get_db_file())

    # Use monkeypatch to safely patch get_database for the test
    monkeypatch.setattr(user_routes_mod, "get_database", _get_database)

    app = Flask(__name__)
    app.register_blueprint(user_routes_mod.blueprint, url_prefix="/users")
    app.config["TESTING"] = True
    client = app.test_client()
    yield client
    # Optionally, add teardown logic here if needed


def test_create_and_get_user(client):
    # Create user
    resp = client.post(
        "/users/",
        json={"name": "Integration", "email": "integration@example.com"},
    )
    assert resp.status_code == 201
    user = resp.get_json()
    # Get user
    resp2 = client.get(f"/users/{user['id']}")
    assert resp2.status_code == 200
    user2 = resp2.get_json()
    assert user2["email"] == "integration@example.com"


def test_get_all_users(client):
    resp = client.get("/users/")
    assert resp.status_code == 200
    users = resp.get_json()
    assert isinstance(users, list)
    assert any(u["email"] == "integration@example.com" for u in users)


def test_update_user(client):
    # Create user
    resp = client.post(
        "/users/",
        json={"name": "UpdateTest", "email": "update@example.com"},
    )
    assert resp.status_code == 201
    user = resp.get_json()
    # Update user name
    resp2 = client.put(f"/users/{user['id']}", json={"name": "UpdatedName"})
    assert resp2.status_code == 200
    updated = resp2.get_json()
    assert updated["name"] == "UpdatedName"
    # Update user email to duplicate (should fail)
    resp3 = client.put(
        f"/users/{user['id']}",
        json={"email": "integration@example.com"},
    )
    assert resp3.status_code == 409


def test_delete_user(client):
    # Create user
    resp = client.post(
        "/users/",
        json={"name": "DeleteTest", "email": "delete@example.com"},
    )
    assert resp.status_code == 201
    user = resp.get_json()
    # Delete user
    resp2 = client.delete(f"/users/{user['id']}")
    assert resp2.status_code == 200
    # Try to get deleted user
    resp3 = client.get(f"/users/{user['id']}")
    assert resp3.status_code == 404


def test_create_user_duplicate_email(client):
    # Create user
    resp = client.post(
        "/users/",
        json={"name": "DupTest", "email": "dup@example.com"},
    )
    assert resp.status_code == 201
    # Try to create another user with same email
    resp2 = client.post(
        "/users/",
        json={"name": "DupTest2", "email": "dup@example.com"},
    )
    assert resp2.status_code == 409


def test_create_user_invalid_input(client):
    # Missing name
    resp = client.post(
        "/users/",
        json={"email": "no_name@example.com"},
    )
    assert resp.status_code == 400
    # Missing email
    resp2 = client.post(
        "/users/",
        json={"name": "NoEmail"},
    )
    assert resp2.status_code == 400
    # No data (send empty dict, since json=None triggers 415)
    resp3 = client.post(
        "/users/",
        json={},
    )
    assert resp3.status_code == 400


def test_update_user_not_found(client):
    # Update non-existent user
    resp = client.put("/users/9999", json={"name": "Ghost"})
    assert resp.status_code == 404


def test_delete_user_not_found(client):
    # Delete non-existent user
    resp = client.delete("/users/9999")
    assert resp.status_code == 404
