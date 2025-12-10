from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate


def get_courses(db: Session, skip: int = 0, limit: int = 100) -> List[Course]:
    return db.query(Course).offset(skip).limit(limit).all()


def get_course(db: Session, course_id: int) -> Optional[Course]:
    return db.query(Course).filter(Course.id == course_id).first()


def create_course(db: Session, course_in: CourseCreate) -> Course:
    course = Course(**course_in.dict())
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


def update_course(db: Session, course: Course, course_in: CourseUpdate) -> Course:
    update_data = course_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(course, field, value)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


def delete_course(db: Session, course: Course) -> None:
    db.delete(course)
    db.commit()
