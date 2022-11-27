from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .handler import decodeJWT

class jwtBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_Error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code = 403, details="Invalid or expired token")
            return credentials.credentials
        else:
            raise HTTPException(status_code = 403, details="Invalid or expired token")

    def verifyJWT(self, jwt_token: str):
        payload = decodeJWT(jwt_token)
        if payload is True:
            return True
        return False
