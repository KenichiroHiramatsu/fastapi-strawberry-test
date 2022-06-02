from datetime import datetime
from typing import Optional

import strawberry

from tasks.models import Status, Task

StatusType = strawberry.enum(Status, name="Status")


@strawberry.type(name="Task")
class TaskType:
    id: strawberry.ID
    title: str
    description: Optional[str]
    status: StatusType
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_instance(cls, instance: Task) -> "TaskType":
        data = instance.__dict__
        return cls(**data)
