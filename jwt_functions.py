# jwt_functions.py

from fastapi import HTTPException
import jwt
from jwt import ExpiredSignatureError, DecodeError

JWT_SECRET = "your-secret-key"
JWT_ALGORITHM = "HS256"

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload["data"]
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token")
