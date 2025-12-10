from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class LessonBase(BaseModel):
    course_id: int
    title: str
    content_url: Optional[str] = None
    order_index: int = 0
    is_active: bool = True


class LessonCreate(LessonBase):
    pass


class LessonUpdate(BaseModel):
    title: Optional[str] = None
    content_url: Optional[str] = None
    order_index: Optional[int] = None
    is_active: Optional[bool] = None


class Lesson(LessonBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
