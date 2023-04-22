import os

import jwt
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi_users.db import BaseUserDatabase
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from app.database import get_db
from app.models.user import User, UserCreate, UserRead
from app.security import (auth_backend, fastapi_users, oauth2_authentication,
                          oauth2_scheme)
from services.sensor_services import fetch_sensor_data

from .models.message import Message

app = FastAPI()
load_dotenv()

JWT_SECRET = os.getenv('SECRET')
JWT_ALGORITHM = 'HS256'

########################
# Auth Endpoints
########################

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserCreate),
    prefix="/users",
    tags=["users"],
)


@app.post("/auth/google/callback")
async def auth_google_callback(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_info = await oauth2_authentication.get_user(token)

    if user_info:
        user = db.query(User).filter(User.email == user_info["email"]).first()
        if not user:
            new_user = UserCreate(email=user_info["email"], name=user_info.get("name"), google_id=user_info["sub"])
            user = User(**new_user.dict())
            db.add(user)
            db.commit()
            db.refresh(user)

        jwt_token = jwt.encode({"sub": str(user.id)}, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return {"access_token": jwt_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Could not authenticate with Google")


########################
# App Endpoints
########################
@app.get("/messages")
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = db.query(Message).offset(skip).limit(limit).all()
    return messages


@app.get("/sensor_data")
async def get_sensor_data():
    sensor_data = await fetch_sensor_data()
    return sensor_data

