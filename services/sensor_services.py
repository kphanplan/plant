import httpx

async def fetch_sensor_data():
    url = "http://your_microcontroller_api_url"
    try:
        response = await httpx.get(url)
        response.raise_for_status()
        data = response.json()
    except httpx.HTTPError as e:
        print(f"An error occurred while requesting sensor data: {e}")
        data = {}  # You can return an empty dictionary or provide default values as a fallback

    return data