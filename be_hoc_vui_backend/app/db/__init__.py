# app/db/__init__.py

from .session import SessionLocal, engine
from .base import Base

# Import các model để SQLAlchemy/Alembic nhận ra
from app.models.user import User          # model User (file app/models/user.py)
from app.models.lesson import Lesson      # model Lesson (file app/models/lesson.py)
from app.db.models.lesson_progress import LessonProgress  # model tiến độ bài học

__all__ = [
    "SessionLocal",
    "engine",
    "Base",
    "User",
    "Lesson",
    "LessonProgress",
]
