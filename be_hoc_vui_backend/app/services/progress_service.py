from datetime import datetime
from typing import List, Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.course import Course
from app.models.lesson import Lesson
from app.models.progress import LessonProgress
from app.schemas.progress import LessonProgressCreate, CourseProgressSummary


def get_progress_for_user(
    db: Session, user_id: int, course_id: Optional[int] = None
) -> List[LessonProgress]:
    query = db.query(LessonProgress).filter(LessonProgress.user_id == user_id)
    if course_id is not None:
        query = query.join(Lesson, Lesson.id == LessonProgress.lesson_id).filter(
            Lesson.course_id == course_id
        )
    return query.all()


def get_progress(db: Session, user_id: int, lesson_id: int) -> Optional[LessonProgress]:
    return (
        db.query(LessonProgress)
        .filter(
            LessonProgress.user_id == user_id,
            LessonProgress.lesson_id == lesson_id,
        )
        .first()
    )


def mark_lesson_progress(
    db: Session, progress_in: LessonProgressCreate
) -> LessonProgress:
    existing = get_progress(
        db, user_id=progress_in.user_id, lesson_id=progress_in.lesson_id
    )
    now = datetime.utcnow()
    if existing:
        existing.last_viewed_at = now
        if progress_in.is_completed:
            existing.is_completed = True
            existing.completed_at = existing.completed_at or now
        db.add(existing)
        db.commit()
        db.refresh(existing)
        return existing

    progress = LessonProgress(
        user_id=progress_in.user_id,
        lesson_id=progress_in.lesson_id,
        is_completed=progress_in.is_completed,
        last_viewed_at=now,
        completed_at=now if progress_in.is_completed else None,
    )
    db.add(progress)
    db.commit()
    db.refresh(progress)
    return progress


def get_course_progress_summary(
    db: Session, user_id: int, course_id: int
) -> CourseProgressSummary:
    total_lessons = (
        db.query(func.count(Lesson.id))
        .filter(Lesson.course_id == course_id, Lesson.is_active.is_(True))
        .scalar()
        or 0
    )

    completed_lessons = (
        db.query(func.count(LessonProgress.id))
        .join(Lesson, Lesson.id == LessonProgress.lesson_id)
        .filter(
            Lesson.course_id == course_id,
            LessonProgress.user_id == user_id,
            LessonProgress.is_completed.is_(True),
        )
        .scalar()
        or 0
    )

    if total_lessons == 0:
        completion_percent = 0.0
    else:
        completion_percent = round(completed_lessons * 100.0 / total_lessons, 2)

    is_completed = total_lessons > 0 and completed_lessons >= total_lessons

    next_lesson = (
        db.query(Lesson)
        .filter(Lesson.course_id == course_id, Lesson.is_active.is_(True))
        .outerjoin(
            LessonProgress,
            (LessonProgress.lesson_id == Lesson.id)
            & (LessonProgress.user_id == user_id)
            & (LessonProgress.is_completed.is_(True)),
        )
        .filter(LessonProgress.id.is_(None))
        .order_by(Lesson.order_index.asc())
        .first()
    )
    next_lesson_id = next_lesson.id if next_lesson else None

    return CourseProgressSummary(
        course_id=course_id,
        total_lessons=total_lessons,
        completed_lessons=completed_lessons,
        completion_percent=completion_percent,
        is_completed=is_completed,
        next_lesson_id=next_lesson_id,
    )


def get_user_progress_overview(db: Session, user_id: int):
    courses = db.query(Course).filter(Course.is_active.is_(True)).all()
    summaries = []
    for course in courses:
        summaries.append(
            get_course_progress_summary(db, user_id=user_id, course_id=course.id)
        )
    return summaries
