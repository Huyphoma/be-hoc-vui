from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.db.base import Base


class LessonStep(Base):
    __tablename__ = "lesson_steps"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False, index=True)
    order_index = Column(Integer, default=0)
    step_type = Column(String(50), nullable=False)
    title = Column(String(255), nullable=False)

    # Cột DB tên "metadata"
    metadata_json = Column("metadata", JSON, default=dict)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    # Quan hệ ngược lại với Lesson
    lesson = relationship("Lesson", back_populates="steps")

    # Quan hệ với LessonStepProgress
    progresses = relationship(
        "LessonStepProgress",
        back_populates="step",
        cascade="all, delete-orphan",
    )
