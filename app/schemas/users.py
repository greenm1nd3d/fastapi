from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def user_serializer(user) -> dict:
    #hashed_password = pwd_context.hash(user["password"])

    return {
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }

def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]
