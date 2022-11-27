from fastapi import APIRouter, Body

from app.config.db import users_collection
from app.models.users import UserSchema, UserLoginSchema
from app.schemas.users import user_serializer, users_serializer
from app.auth.handler import signJWT

user_router = APIRouter()

# User signup
@user_router.post("/user/signup", tags=["Users"])
def user_signup(user: UserSchema):
    _id = users_collection.insert_one(dict(user))
    user = users_serializer(users_collection.find({"_id": _id.inserted_id}))

    return {
        "status": 200,
        "data": user[0],
        "token": signJWT(user[0]["email"])
    }

# User signin
@user_router.post("/user/signin", tags=["Users"])
def user_signin(user: UserLoginSchema = Body(default=None)):
    found = users_serializer(users_collection.find({"email": user.email}))

    if found:
        data = found[0]
        if data["password"] == user.password:
            return signJWT(user.email)

    return {
        "error": "Invalid sign in credentials"
    }
