from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    level = Column(String(50), nullable=True)  # ví d?: "m?m non", "l?p 1"
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Quan h? 1-n: 1 Course có nhi?u Lesson
    lessons = relationship(
        "Lesson",
        back_populates="course",
        cascade="all, delete-orphan",
    )
