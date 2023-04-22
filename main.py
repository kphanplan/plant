from fastapi import FastAPI
from services.sensor_services import fetch_sensor_data

app = FastAPI()

@app.get("/sensor_data")
async def get_sensor_data():
    # Call a function from the service layer to get sensor data
    sensor_data = await fetch_sensor_data()
    return sensor_data