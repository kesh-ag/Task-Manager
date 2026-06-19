from .schemas import TaskStatus, TaskUpdateRequest, TaskCreateRequest
from datetime import datetime,UTC
from fastapi import HTTPException

tasks={}
task_id=0


def create_task(task_create: TaskCreateRequest):
    global task_id
    task_id+=1
    task = {
        "id": task_id,
        "title": task_create.title,
        "desc": task_create.desc,
        "status": task_create.status,
        "assigned_to": task_create.assigned_to,
        "created_at": datetime.now(UTC)
    }
    tasks[task_id]=task
    return task

def get_task(task_id:int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task ID not found")
    return tasks[task_id]
    
def update_task(task_id: int, task_update: TaskUpdateRequest):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task ID not found")
    task = tasks[task_id]
    updates = task_update.model_dump(exclude_unset=True)
    for key, value in updates.items():
        task[key] = value
    tasks[task_id] = task
    return task

def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404,detail="Task ID not found")
    if tasks[task_id]["status"] == TaskStatus.completed:
        raise HTTPException(400, "Cannot delete completed task")
    del tasks[task_id]
    return "Task Deleted"

def list_tasks():
    return list(tasks.values())