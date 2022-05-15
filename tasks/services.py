from datetime import datetime
from typing import List, Optional, Type

from tasks.models import Status, Task
from tasks.repositories import InMemoryRepository


class TaskService:
    def __init__(self, repo: Type[InMemoryRepository]) -> None:
        self._repo = repo

    @property
    def repo(self) -> Type[InMemoryRepository]:
        return self._repo

    def find(self, id: str) -> Task:
        task = self.repo.find_by_id(id)

        return task

    def find_all(self) -> List[Task]:
        tasks = self.repo.find_all()

        return tasks

    def create(self, *, title: str, description: Optional[str] = None) -> Task:
        task = Task(title=title, description=description)
        self.repo.save(task)

        return task

    def update(self, *, id: str, status: Status) -> Task:
        task = self.repo.find_by_id(id)
        task.status = status
        task.updated_at = datetime.utcnow()
        self.repo.save(task)

        return task

    def delete(self, id: str) -> Task:
        task = self.repo.find_by_id(id)
        self.repo.delete(task)

        return task
