from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.models.lesson_step import LessonStep
from app.models.lesson_step_progress import LessonStepProgress
from app.schemas.progress import (
    LessonStepProgressCreate,
    LessonStepProgressUpdate,
    LessonStepProgressResponse,
)

router = APIRouter(prefix="/progress", tags=["Progress"])


# TẠM THỜI: fake current_user cho dev (user_id = 1)
class _FakeUser:
    def __init__(self, id: int):
        self.id = id


def get_current_user():
    # Sau này sẽ thay bằng auth thật
    return _FakeUser(id=1)


# Lấy DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =====================================================
# 1) Lấy tiến độ theo STEP_ID
#    GET /api/v1/progress/steps/{step_id}
# =====================================================
@router.get("/steps/{step_id}", response_model=LessonStepProgressResponse)
def get_step_progress(
    step_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    progress = (
        db.query(LessonStepProgress)
        .filter(
            LessonStepProgress.step_id == step_id,
            LessonStepProgress.user_id == current_user.id,
        )
        .first()
    )

    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")

    return progress


# =====================================================
# 2) Tạo tiến độ mới cho 1 step
#    POST /api/v1/progress/steps/
# =====================================================
@router.post("/steps/", response_model=LessonStepProgressResponse)
def create_step_progress(
    data: LessonStepProgressCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    # Check step có tồn tại không
    step = db.query(LessonStep).filter(LessonStep.id == data.step_id).first()
    if not step:
        raise HTTPException(status_code=404, detail="Step not found")

    # Nếu đã có progress -> trả luôn, không tạo trùng
    existing = (
        db.query(LessonStepProgress)
        .filter(
            LessonStepProgress.step_id == data.step_id,
            LessonStepProgress.user_id == current_user.id,
        )
        .first()
    )
    if existing:
        return existing

    progress = LessonStepProgress(
        step_id=data.step_id,
        user_id=current_user.id,
        status=data.status,
        updated_at=datetime.utcnow(),
    )

    db.add(progress)
    db.commit()
    db.refresh(progress)

    return progress


# =====================================================
# 3) Cập nhật tiến độ 1 step
#    PUT /api/v1/progress/steps/{step_id}
# =====================================================
@router.put("/steps/{step_id}", response_model=LessonStepProgressResponse)
def update_step_progress(
    step_id: int,
    data: LessonStepProgressUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    progress = (
        db.query(LessonStepProgress)
        .filter(
            LessonStepProgress.step_id == step_id,
            LessonStepProgress.user_id == current_user.id,
        )
        .first()
    )

    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")

    progress.status = data.status
    progress.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(progress)

    return progress
