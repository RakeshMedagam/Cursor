"""
users.py  —  editable
User lookup/profile helpers. Safe to modify during exercises.
"""

_USERS = {
    "u1": {"id": "u1", "name": "Asha Rao", "region": "IN-North", "tier": "gold"},
    "u2": {"id": "u2", "name": "Ben Cole", "region": "US-East", "tier": "silver"},
}


def get_user(user_id: str):
    return _USERS.get(user_id)


def list_users_by_region(region: str):
    return [u for u in _USERS.values() if u["region"] == region]
