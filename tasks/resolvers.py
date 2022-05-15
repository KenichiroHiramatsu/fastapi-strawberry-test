from typing import List
import strawberry

from tasks.inputs import AddTaskInput, UpdateTaskInput
from tasks.repositories import InMemoryRepository
from tasks.services import TaskService
from tasks.types import TaskType

import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
CONNECTION_URL = os.getenv('CONNECTION_URL')


def get_task(id: strawberry.ID) -> TaskType:
    db = InMemoryRepository
    service = TaskService(db)
    task = service.find(id)

    return TaskType.from_instance(task)


def get_tasks() -> List[TaskType]:
    # client = pymongo.MongoClient(CONNECTION_URL)
    # db = client.FastApiDB.tasks
    # print(db)
    # document = db.find()
    # client.close()
    # response = [document[i] for i in range(document.count())]

    db = InMemoryRepository
    service = TaskService(db)
    tasks = service.find_all()

    return [TaskType.from_instance(task) for task in tasks]


def add_task(task_input: AddTaskInput) -> TaskType:
    db = InMemoryRepository
    service = TaskService(db)
    task = service.create(**task_input.__dict__)
    print(TaskType.from_instance(task))
    return TaskType.from_instance(task)


def update_task(task_input: UpdateTaskInput) -> TaskType:
    db = InMemoryRepository
    service = TaskService(db)
    task = service.update(**task_input.__dict__)

    return TaskType.from_instance(task)


def delete_task(id: strawberry.ID) -> TaskType:
    db = InMemoryRepository
    service = TaskService(db)
    task = service.delete(id)

    return TaskType.from_instance(task)
