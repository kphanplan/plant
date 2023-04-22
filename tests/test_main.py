from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_sensor_data():
    response = client.get("/sensor_data")
    print('response', response)
    assert response.status_code == 200
    assert "soilMoisture" in response.json()
    assert "humidity" in response.json()
    assert "temperature" in response.json()
    assert "motionDetected" in response.json()