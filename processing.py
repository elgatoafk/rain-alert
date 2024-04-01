import requests

def get_weather_forecast(parameters: tuple) -> dict:
    # gets data for next 12 hours
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters, timeout=20)
    response.raise_for_status()

    return response.json()["list"]

def will_rain(weather_data: list[dict]) -> bool:

    for one_stamp in weather_data:
        if int(one_stamp["weather"][0]["id"]) <700:
            return True
    else:
        return False

