from processing import *
from constants import *

weather_data = get_weather_forecast(PARAMETERS)

print(will_rain(weather_data))
