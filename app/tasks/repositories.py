from copy import deepcopy
from typing import Any, Dict, List

from tasks.models import Task

import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
CONNECTION_URL = os.getenv('CONNECTION_URL')

# document = db.find()
# client.close()
# response = [document[i] for i in range(document.count())]


class InMemoryRepository:
    client = pymongo.MongoClient(CONNECTION_URL)
    db = client.FastApiDB.tasks
    _store: Dict[str, Any] = {}

    @classmethod
    def find_by_id(cls, id_: str) -> Task:
        task = cls._store.get(id_)
        if task is None:
            raise Exception("Not Found")

        return task

    @classmethod
    def find_all(cls) -> List[Task]:
        tasks = list(cls._store.values())
        # tasks = list(cls.db.find())
        # print(tasks[0])
        return tasks

    @classmethod
    def save(cls, task: Task) -> None:
        cls._store[str(task.id)] = deepcopy(task)

    @classmethod
    def delete(cls, task: Task) -> None:
        del cls._store[str(task.id)]
