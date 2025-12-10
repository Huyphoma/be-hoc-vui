from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    level: Optional[str] = None
    is_active: bool = True


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    level: Optional[str] = None
    is_active: Optional[bool] = None


class Course(CourseBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
