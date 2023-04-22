from fastapi import FastAPI, Depends, HTTPException
from services.sensor_services import fetch_sensor_data
from database import SessionLocal
from models.message import Message
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/messages")
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = db.query(Message).offset(skip).limit(limit).all()
    return messages

@app.get("/sensor_data")
async def get_sensor_data():
    # Call a function from the service layer to get sensor data
    sensor_data = await fetch_sensor_data()
    return sensor_data