import os
import uuid
from typing import Optional

from dotenv import load_dotenv
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin, schemas
from fastapi_users.authentication import (AuthenticationBackend,
                                          BearerTransport, JWTStrategy)
from fastapi_users_db_sqlalchemy import (SQLAlchemyBaseUserTableUUID,
                                         SQLAlchemyUserDatabase)
from pydantic import BaseModel, EmailStr
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from base import Base 
from ..db_utils import get_db

load_dotenv()

SECRET = os.getenv('SECRET')

# the actual user object
class User(Base, SQLAlchemyBaseUserTableUUID):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    google_id = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

# google auth
class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    async def get_user_db(self):
        from models.user import User
        return SQLAlchemyUserDatabase(User, get_db())

async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_db)):
    yield UserManager(user_db)


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
