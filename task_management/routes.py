from fastapi import APIRouter
from .service import get_task,update_task,create_task,list_tasks,delete_task
from .schemas import TaskResponse, TaskUpdateRequest, TaskCreateRequest


router=APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_route(task:TaskCreateRequest):
    return create_task(task)

@router.get("/")
def list_route():
    return list_tasks()

@router.get("/{task_id}", response_model=TaskResponse)
def get_route(task_id:int):
    return get_task(task_id)

@router.put("/{task_id}", response_model=TaskResponse)
def update_route(task_id: int, task_update: TaskUpdateRequest):
    return update_task(task_id, task_update)

@router.delete("/{task_id}")
def delete_route(task_id:int):
    return delete_task(task_id)