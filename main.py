from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.routes.tasks import task_router
from app.routes.users import user_router

app = FastAPI()
handler = Mangum(app)

origins = [
    "https://zkjfxwkzcpldgj2eolfdwytfba0sravc.lambda-url.us-west-2.on.aws",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Tasks API"}

app.include_router(task_router)
app.include_router(user_router)
