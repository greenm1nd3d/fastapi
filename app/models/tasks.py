from pydantic import BaseModel, Field, EmailStr

class TaskSchema(BaseModel):
    title: str = Field(default=None)
    content: str = Field(default=None)
    status: str = Field(default="N")
    class Config:
        the_schema = {
            "task": {
                "title": "Say Hello",
                "content": "Say hello to everyone"
            }
        }
