import os, time, requests
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("weather_api_key")


def fetch(city):
    resp = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}"
    )
    response = resp.json()
    return response["main"]["temp"]


def main(cities: str):
    start = time.time()

    results = [fetch(city) for city in cities]
    print(results)

    elapsed_time = time.time() - start
    print(f"Took {elapsed_time:.2f} seconds")


main(["Chennai", "Mumbai", "Kolkata", "Delhi"])
