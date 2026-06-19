from fastapi import FastAPI
from task_management.routes import router as task_router

app = FastAPI(
title="Simple Task Management API",
version="0.1.0"
)

app.include_router(task_router)
@app.get("/health")
async def health():
    return {"status": "ok"}