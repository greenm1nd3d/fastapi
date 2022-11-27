from fastapi import APIRouter, Depends
from bson import ObjectId

from app.config.db import tasks_collection
from app.models.tasks import TaskSchema
from app.schemas.tasks import task_serializer, tasks_serializer
from app.auth.bearer import jwtBearer

task_router = APIRouter()

# Get all tasks
@task_router.get("/", tags=["Tasks"])
async def get_tasks():
    tasks = tasks_serializer(tasks_collection.find())
    return {
        "status": 200,
        "data": tasks
    }

# Get specific task with given id
@task_router.get("/{id}", dependencies=[Depends(jwtBearer())], tags=["Tasks"])
async def get_task(id: str):
    task = tasks_serializer(tasks_collection.find({"_id": ObjectId(id)}))
    return {
        "status": 200,
        "data": task
    }

# Create a new task
@task_router.post("/", tags=["Tasks"])
async def create_task(task: TaskSchema):
    _id = tasks_collection.insert_one(dict(task))
    task = tasks_serializer(tasks_collection.find({"_id": _id.inserted_id}))
    return {
        "status": 200,
        "data": task
    }

# Update a task with given id
@task_router.put("/{id}", tags=["Tasks"])
async def update_task(id: str, task: TaskSchema):
    tasks_collection.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(task)
    })
    task = tasks_serializer(tasks_collection.find({"_id": ObjectId(id)}))
    return {
        "status": 200,
        "data": task
    }

# Delete a task with given id
@task_router.delete("/{id}", tags=["Tasks"])
async def delete_task(id: str):
    tasks_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {
        "status": 200,
        "data": []
    }

# Mark a task with given id as completed
@task_router.patch("/complete/{id}", tags=["Tasks"])
async def complete_task(id: str, task: TaskSchema):
    tasks_collection.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": {"status": "C"}
    })
    task = tasks_serializer(tasks_collection.find({"_id": ObjectId(id)}))
    return {
        "status": 200,
        "data": task
    }
