from dotenv import load_dotenv
import requests
import os

load_dotenv()
API = os.getenv("API_KEY")


def get_data(date):
    hazardous_asteroids = dict()

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key={API}"
    result = requests.get(url=url).json()["near_earth_objects"]
    if result == {}:
        return "Немає даних."
    result = result[date]
    for i in range(len(result)):
        if result[i]["is_potentially_hazardous_asteroid"] is True:
            hazardous_asteroids[i] = result[i]

    return hazardous_asteroids
