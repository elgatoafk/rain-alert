from processing import *
from constants import *

weather_data = get_weather_forecast(PARAMETERS)

if will_rain(weather_data):
    send_sms()
