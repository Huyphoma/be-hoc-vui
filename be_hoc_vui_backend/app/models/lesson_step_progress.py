from datetime import datetime
from enum import Enum

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class LessonStepStatusEnum(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class LessonStepProgress(Base):
    __tablename__ = "lesson_step_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    step_id = Column(Integer, ForeignKey("lesson_steps.id"), nullable=False, index=True)

    status = Column(
        String(20),
        nullable=False,
        default=LessonStepStatusEnum.NOT_STARTED.value,
    )

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    # Quan hệ với LessonStep
    step = relationship("LessonStep", back_populates="progresses")
