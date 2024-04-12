from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt

router = APIRouter()

JWT_SECRET = "your-secret-key"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_TIME_MINUTES = 30

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Example logic to validate username and password
    if form_data.username == "username" and form_data.password == "password":
        token = generate_token({"sub": form_data.username})
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

def generate_token(data: dict) -> str:
    payload = {
        "data": data,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
