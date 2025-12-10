from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.course import Course, CourseCreate, CourseUpdate
from app.services.course_service import (
    create_course,
    delete_course,
    get_course,
    get_courses,
    update_course,
)

router = APIRouter()


@router.get("/", response_model=List[Course])
def list_courses(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_courses(db, skip=skip, limit=limit)


@router.post("/", response_model=Course)
def create_new_course(course_in: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db, course_in)


@router.get("/{course_id}", response_model=Course)
def get_course_detail(course_id: int, db: Session = Depends(get_db)):
    course = get_course(db, course_id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.put("/{course_id}", response_model=Course)
def update_course_detail(
    course_id: int, course_in: CourseUpdate, db: Session = Depends(get_db)
):
    course = get_course(db, course_id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return update_course(db, course, course_in)


@router.delete("/{course_id}", status_code=204)
def remove_course(course_id: int, db: Session = Depends(get_db)):
    course = get_course(db, course_id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    delete_course(db, course)
    return None
