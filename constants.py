import os

MY_LONGITUDE = 24.029716
MY_LATITUDE = 49.839684

PARAMETERS = {

    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": os.environ.get("OMW_API_KEY"),
    "cnt": 4
}

ACC_SID = os.environ.get("TWILIO_ACCOUNT_SID")

AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

TWILIO_PHONE = os.environ.get("TWILIO_PHONE")

MY_PHONE = os.environ.get("MY_PHONE")