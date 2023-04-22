from app.models.user import User
from app.database import get_db
from fastapi_users.db import SQLAlchemyUserDatabase

def get_user_db():
    return SQLAlchemyUserDatabase(User, get_db())