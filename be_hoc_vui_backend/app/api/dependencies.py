from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.models.user import User


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class _FakeUser:
    def __init__(self, id: int):
        self.id = id


def get_current_user():
    # TODO: thay b?ng JWT sau này
    return _FakeUser(id=1)
