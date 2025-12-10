from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.db.base import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), index=True, nullable=False)
    order_index = Column(Integer, default=0)

    # Cột trong DB tên là "metadata", nhưng tránh đụng tên reserved của SQLAlchemy
    metadata_json = Column("metadata", JSON, default=dict)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    # Quan hệ với Course
    course = relationship("Course", back_populates="lessons")

    # Quan hệ với LessonProgress
    progresses = relationship(
        "LessonProgress",
        back_populates="lesson",
        cascade="all, delete-orphan",
    )

    # Quan hệ với LessonStep
    steps = relationship(
        "LessonStep",
        back_populates="lesson",
        cascade="all, delete-orphan",
    )
