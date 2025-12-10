from datetime import datetime
from pydantic import BaseModel


class LessonStepProgressBase(BaseModel):
    step_id: int
    status: str = "not_started"


class LessonStepProgressCreate(LessonStepProgressBase):
    pass


class LessonStepProgressUpdate(BaseModel):
    status: str


class LessonStepProgressResponse(LessonStepProgressBase):
    id: int
    user_id: int
    updated_at: datetime

    class Config:
        orm_mode = True
