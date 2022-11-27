from typing import Union
from fastapi import FastAPI, Body, Depends
from pydantic import BaseModel
from pymongo import MongoClient

from app.routes.tasks import task_router
from app.routes.users import user_router

app = FastAPI()

app.include_router(task_router)
app.include_router(user_router)
