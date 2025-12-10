from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.progress import (
    LessonProgress,
    LessonProgressCreate,
    CourseProgressSummary,
)
from app.services.progress_service import (
    get_progress_for_user,
    mark_lesson_progress,
    get_course_progress_summary,
    get_user_progress_overview,
)

router = APIRouter()


@router.get("/user/{user_id}", response_model=List[LessonProgress])
def get_user_progress(
    user_id: int,
    course_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    return get_progress_for_user(db, user_id=user_id, course_id=course_id)


@router.post("/", response_model=LessonProgress)
def update_progress(progress_in: LessonProgressCreate, db: Session = Depends(get_db)):
    return mark_lesson_progress(db, progress_in)


@router.get(
    "/user/{user_id}/course/{course_id}",
    response_model=CourseProgressSummary,
)
def get_course_summary(
    user_id: int,
    course_id: int,
    db: Session = Depends(get_db),
):
    return get_course_progress_summary(db, user_id=user_id, course_id=course_id)


@router.get(
    "/user/{user_id}/overview",
    response_model=List[CourseProgressSummary],
)
def get_user_overview(
    user_id: int,
    db: Session = Depends(get_db),
):
    return get_user_progress_overview(db, user_id=user_id)
