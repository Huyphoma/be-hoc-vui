from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, Float, Enum, DateTime
from sqlalchemy.orm import relationship
import enum

from app.db.base import Base


class LessonProgressStatus(str, enum.Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class LessonProgress(Base):
    __tablename__ = "lesson_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), index=True, nullable=False)

    status = Column(
        Enum(LessonProgressStatus),
        nullable=False,
        default=LessonProgressStatus.NOT_STARTED,
    )

    last_position_seconds = Column(Float, nullable=True)
    score = Column(Float, nullable=True)

    completed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    user = relationship("User", back_populates="lesson_progresses")
    lesson = relationship("Lesson", back_populates="progresses")
