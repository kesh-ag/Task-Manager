from enum import Enum
from pydantic import BaseModel,EmailStr
from datetime import datetime,UTC
from sqlmodel import Field, SQLModel

class TaskStatus(str,Enum):
    pending = "Pending"
    in_progress = "In_progress"
    completed = "Completed"

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

class TaskRecord(SQLModel,table=True):
    __tablename__="Tasks"
    id: int|None= Field(default=None,primary_key=True)
    title: str=Field(index=True)
    desc: str | None=Field(default="Blank")
    status: TaskStatus=Field(index=True)
    assigned_to: EmailStr|None=Field(index=True)
    created_at:datetime=Field(default_factory=lambda:datetime.now(UTC))

