import asyncio, httpx, os, time
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("weather_api_key")


async def fetch(city):
    async with httpx.AsyncClient(
        timeout=2
    ) as client:  # Built-in timeout for httpx calls!
        try:
            resp = await client.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}"
            )
            response = resp.json()
            return response["main"]["temp"]
        except httpx.ReadTimeout:
            return "Timed out!"


async def main(cities: str):
    start = time.time()

    tasks = [asyncio.create_task(fetch(city)) for city in cities]
    results = await asyncio.gather(*tasks)
    print(results)

    elapsed_time = time.time() - start
    print(f"Took {elapsed_time:.2f} seconds")


asyncio.run(main(["Chennai", "Mumbai", "Kolkata", "Delhi"]))
