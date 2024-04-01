import requests
from twilio.rest import Client
from constants import *

def get_weather_forecast(parameters: tuple):
    # gets data for next 12 hours
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters, timeout=20)
    response.raise_for_status()

    return response.json()["list"]

def will_rain(weather_data) -> bool:

    for one_stamp in weather_data:
        if int(one_stamp["weather"][0]["id"]) <700:
            return True
    else:
        return False

def send_sms():
    client = Client(ACC_SID, AUTH_TOKEN)

    message = client.messages \
                    .create(
                        body="Bring an umbrella",
                        from_= TWILIO_PHONE,
                        to= MY_PHONE
                    )




