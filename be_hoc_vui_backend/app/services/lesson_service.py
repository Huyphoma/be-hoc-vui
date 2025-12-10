from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.lesson import Lesson
from app.schemas.lesson import LessonCreate, LessonUpdate


def get_lessons_by_course(db: Session, course_id: int) -> List[Lesson]:
    return (
        db.query(Lesson)
        .filter(Lesson.course_id == course_id)
        .order_by(Lesson.order_index.asc())
        .all()
    )


def get_lesson(db: Session, lesson_id: int) -> Optional[Lesson]:
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()


def create_lesson(db: Session, lesson_in: LessonCreate) -> Lesson:
    lesson = Lesson(**lesson_in.dict())
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson


def update_lesson(db: Session, lesson: Lesson, lesson_in: LessonUpdate) -> Lesson:
    update_data = lesson_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(lesson, field, value)
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson


def delete_lesson(db: Session, lesson: Lesson) -> None:
    db.delete(lesson)
    db.commit()
