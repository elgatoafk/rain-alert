import requests

def get_weather_forecast(parameters: tuple) -> dict:
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters, timeout=20)
    response.raise_for_status()

    data = response.json()["response"]

