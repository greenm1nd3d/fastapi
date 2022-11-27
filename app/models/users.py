from pydantic import BaseModel, Field, EmailStr
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserSchema(BaseModel):
    name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema = {
            "user": {
                "name": "Freddie",
                "email": "fred@pogi.com",
                "password": "pass!234"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_schema = {
            "login": {
                "email": "fred@pogi.com",
                "password": "pass!234"
            }
        }
