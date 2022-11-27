import time
import jwt
from decouple import config

JWT_SECRET = config("SECRET")

# Return generated JWT token
def token_response(token: str):
    return {
        "access_token": token
    }

# Sign JWT string
def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token_response(token)

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm="HS256")
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}
