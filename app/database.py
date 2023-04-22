import os

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from .db_utils import get_db

def create_tables():
    from .models.user import User

    print(f"Tables: {Base.metadata.tables}")  # Add this line to print the tables
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()