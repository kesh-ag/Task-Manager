from fastapi import APIRouter
from sqlmodel import Session,Depends
from .database import get_session
from .service import get_task,update_task,create_task,list_tasks,delete_task
from .schemas import TaskResponse, TaskUpdateRequest, TaskCreateRequest


router=APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_route(task:TaskCreateRequest,session:Session=Depends(get_session)):
    return create_task(task,session)

@router.get("/")
def list_route():
    return list_tasks()

@router.get("/{task_id}", response_model=TaskResponse)
def get_route(task_id:int,session:Session=Depends(get_session)):
    return get_task(task_id,session)

@router.patch("/{task_id}", response_model=TaskResponse)
def update_route(task_id: int, task_update: TaskUpdateRequest,session:Session=Depends(get_session)):
    return update_task(task_id, task_update,session)

@router.delete("/{task_id}")
def delete_route(task_id:int,session:Session=Depends(get_session)):
    return delete_task(task_id,session)