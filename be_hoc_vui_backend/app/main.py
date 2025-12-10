from fastapi import FastAPI
from app.api.api_v1.api import api_router

app = FastAPI(title="BeHocVui API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api/v1")
