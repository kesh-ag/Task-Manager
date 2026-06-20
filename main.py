from fastapi import FastAPI
from task_management.routes import router as task_router
from task_management.database import engine 
from sqlmodel import SQLModel

app = FastAPI(
title="Simple Task Management API",
version="0.1.0"
)

@app.on_event("startup") 
def on_startup(): 
    SQLModel.metadata.create_all(engine)

app.include_router(task_router)
@app.get("/health")
async def health():
    return {"status": "ok"}