from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Database session
from app.db.session import get_db

# Models
from app.models.lesson import Lesson
from app.models.lesson_step import LessonStep
from app.models.lesson_step_progress import (
    LessonStepProgress,
    LessonStepStatusEnum
)

# Router g?c
api_router = APIRouter()


# ===============================
#   API: L?Y FLOW CHI TI?T BÀI H?C
# ===============================
@api_router.get("/lessons/{lesson_id}/flow")
def get_lesson_flow(
    lesson_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):

    # L?y thông tin bài h?c
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    # L?y danh sách step c?a bài
    steps = (
        db.query(LessonStep)
        .filter(LessonStep.lesson_id == lesson_id)
        .order_by(LessonStep.order_index.asc())
        .all()
    )

    step_ids = [s.id for s in steps]

    # L?y ti?n d? step
    progresses = (
        db.query(LessonStepProgress)
        .filter(
            LessonStepProgress.user_id == user_id,
            LessonStepProgress.step_id.in_(step_ids)
        )
        .all()
    )

    progress_map = {p.step_id: p.status for p in progresses}

    total_steps = len(steps)
    completed = sum(1 for s in steps if progress_map.get(s.id) == "done")
    percent = round((completed / total_steps) * 100) if total_steps > 0 else 0

    # Chu?n hoá d? li?u tr? v?
    flow = {
        "lesson_id": lesson.id,
        "title": lesson.title,
        "progress_percent": percent,
        "total_steps": total_steps,
        "completed_steps": completed,
        "steps": [
            {
                "step_id": s.id,
                "order_index": s.order_index,
                "type": s.step_type,
                "title": s.title,
                "metadata": s.metadata,
                "status": progress_map.get(s.id, "not_started")
            }
            for s in steps
        ]
    }

    return flow


# ========================================
#   API: UPDATE STATUS CHO M?T STEP
# ========================================
@api_router.post("/lessons/{lesson_id}/steps/{step_id}/status")
def update_step_status(
    lesson_id: int,
    step_id: int,
    new_status: str,
    user_id: int,
    db: Session = Depends(get_db),
):

    # Ki?m tra step có thu?c bài h?c không
    step = (
        db.query(LessonStep)
        .filter(
            LessonStep.id == step_id,
            LessonStep.lesson_id == lesson_id,
        )
        .first()
    )

    if not step:
        raise HTTPException(status_code=404, detail="Step not found")

    # L?y ho?c t?o ti?n d? step
    progress = (
        db.query(LessonStepProgress)
        .filter(
            LessonStepProgress.step_id == step_id,
            LessonStepProgress.user_id == user_id
        )
        .first()
    )

    if not progress:
        # T?o b?n ghi m?i
        progress = LessonStepProgress(
            step_id=step.id,
            user_id=user_id,
            status=new_status
        )
        db.add(progress)
    else:
        # Update tr?ng thái
        progress.status = new_status

    db.commit()
    db.refresh(progress)

    return {
        "step_id": step_id,
        "user_id": user_id,
        "status": progress.status
    }
