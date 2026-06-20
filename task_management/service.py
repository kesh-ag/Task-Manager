from .schemas import TaskStatus, TaskUpdateRequest, TaskCreateRequest,TaskRecord
from fastapi import HTTPException
from sqlmodel import Session,select



def create_task(task_create: TaskCreateRequest,session:Session):
    task =TaskRecord(title= task_create.title,
        desc= task_create.desc,
        status= task_create.status,
        assigned_to=task_create.assigned_to)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_task(task_id:int,session:Session):
    task=session.get(TaskRecord,task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task ID not found")
    return task
    
def update_task(task_id: int, task_update: TaskUpdateRequest,session:Session):
    task=session.get(TaskRecord,task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task ID not found")
    updated_task = task_update.model_dump(exclude_unset=True)
    task.sqlmodel_update(updated_task)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def delete_task(task_id: int,session:Session):
    task=session.get(TaskRecord,task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task ID not found")
    if task.status == TaskStatus.completed:
        raise HTTPException(400, "Cannot delete completed task")
    session.delete(task)
    session.commit()
    return "Task Deleted"

def list_tasks(session:Session):
    return session.exec(select(TaskRecord)).all()