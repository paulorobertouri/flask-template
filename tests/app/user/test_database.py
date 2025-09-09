import pytest

from app.user.database import UserDatabase
from app.user.models import UserRequest


@pytest.fixture
def db():
    # Use in-memory SQLite DB for isolation
    return UserDatabase(":memory:")


def test_create_and_get_user(db):
    req = UserRequest(name="Alice", email="alice@example.com")
    user = db.create(req)
    assert user is not None
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    # Test get by id
    fetched = db.get(user.id)
    assert fetched is not None
    assert fetched.email == "alice@example.com"


def test_get_all_users(db):
    db.create(UserRequest(name="A", email="a@a.com"))
    db.create(UserRequest(name="B", email="b@b.com"))
    users = db.get_all()
    assert len(users) == 2
    emails = {u.email for u in users}
    assert "a@a.com" in emails and "b@b.com" in emails


def test_update_user(db):
    user = db.create(UserRequest(name="C", email="c@c.com"))
    updated = db.update(user.id, UserRequest(name="C2", email="c2@c.com"))
    assert updated.name == "C2"
    assert updated.email == "c2@c.com"


def test_update_nonexistent_user(db):
    updated = db.update(
        999,
        UserRequest(name="NoOne", email="noone@example.com"),
    )
    assert updated is None


def test_delete_user(db):
    user = db.create(UserRequest(name="D", email="d@d.com"))
    db.delete(user.id)
    assert db.get(user.id) is None


def test_exists_and_email_exists(db):
    user = db.create(UserRequest(name="E", email="e@e.com"))
    assert db.exists(user.id)
    assert db.email_exists("e@e.com")
    assert not db.email_exists("notfound@e.com")


def test_email_exists_exclude_id(db):
    user1 = db.create(UserRequest(name="F", email="f@f.com"))
    db.create(UserRequest(name="G", email="g@g.com"))
    # Should not find user1's email if excluding user1's id
    assert not db.email_exists("f@f.com", exclude_id=user1.id)
    # Should find user1's email if not excluding
    assert db.email_exists("f@f.com")
