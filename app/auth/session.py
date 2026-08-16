"""
auth/session.py  —  UAT-LOCKED
Session handling for the internal dashboard. Signed off UAT 2024-Q2.
DO NOT MODIFY during Day 1-3 exercises — this is the file used in the
Module 2 "junior dev keeps touching a locked file" scenario.
"""
import secrets
import time

_SESSIONS = {}
_SESSION_TTL_SECONDS = 3600


def create_session(user_id: str) -> str:
    token = secrets.token_hex(16)
    _SESSIONS[token] = {"user_id": user_id, "created_at": time.time()}
    return token


def validate_session(token: str) -> bool:
    session = _SESSIONS.get(token)
    if not session:
        return False
    if time.time() - session["created_at"] > _SESSION_TTL_SECONDS:
        del _SESSIONS[token]
        return False
    return True


def get_user_for_session(token: str):
    session = _SESSIONS.get(token)
    return session["user_id"] if session else None
