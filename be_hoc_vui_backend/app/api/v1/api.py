from fastapi import APIRouter

from app.api.v1.endpoints import auth, system, courses, lessons, progress

api_router = APIRouter()

api_router.include_router(system.router, tags=["system"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(courses.router, prefix="/courses", tags=["courses"])
api_router.include_router(lessons.router, prefix="/lessons", tags=["lessons"])
api_router.include_router(progress.router, prefix="/progress", tags=["progress"])
