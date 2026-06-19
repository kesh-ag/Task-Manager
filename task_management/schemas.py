from enum import Enum
from pydantic import BaseModel,EmailStr
from datetime import datetime

class TaskStatus(str,Enum):
    pending = "Pending"
    in_progress = "in_progress"
    completed = "completed"

class TaskCreateRequest(BaseModel):
    title: str
    desc: str="Blank"
    status: TaskStatus=TaskStatus.pending
    assigned_to: EmailStr | None=None

class TaskUpdateRequest(BaseModel):
    title: str | None=None
    desc: str | None=None
    status: TaskStatus | None=None
    assigned_to: EmailStr | None=None

class TaskResponse(BaseModel):
    id: int
    title: str
    desc: str
    status: TaskStatus=TaskStatus.pending
    assigned_to: EmailStr | None=None
    created_at: datetime


