from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.lesson import Lesson, LessonCreate, LessonUpdate
from app.services.lesson_service import (
    create_lesson,
    delete_lesson,
    get_lesson,
    get_lessons_by_course,
    update_lesson,
)

router = APIRouter()


@router.get("/course/{course_id}", response_model=List[Lesson])
def list_lessons_by_course(course_id: int, db: Session = Depends(get_db)):
    return get_lessons_by_course(db, course_id=course_id)


@router.post("/", response_model=Lesson)
def create_new_lesson(lesson_in: LessonCreate, db: Session = Depends(get_db)):
    return create_lesson(db, lesson_in)


@router.get("/{lesson_id}", response_model=Lesson)
def get_lesson_detail(lesson_id: int, db: Session = Depends(get_db)):
    lesson = get_lesson(db, lesson_id=lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson


@router.put("/{lesson_id}", response_model=Lesson)
def update_lesson_detail(
    lesson_id: int, lesson_in: LessonUpdate, db: Session = Depends(get_db)
):
    lesson = get_lesson(db, lesson_id=lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return update_lesson(db, lesson, lesson_in)


@router.delete("/{lesson_id}", status_code=204)
def remove_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = get_lesson(db, lesson_id=lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    delete_lesson(db, lesson)
    return None
