"""Starter tests for users.py — safe to extend."""
from app.users import get_user, list_users_by_region


def test_get_user_found():
    user = get_user("u1")
    assert user is not None
    assert user["name"] == "Asha Rao"


def test_get_user_not_found():
    assert get_user("nonexistent") is None


def test_list_users_by_region():
    users = list_users_by_region("IN-North")
    assert len(users) == 1
    assert users[0]["id"] == "u1"
