import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

class Status(Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"

@dataclass
class Task:
    title: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    description: Optional[str] = None
    status: Status = Status.TODO
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)