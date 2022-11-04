import os

import requests
import json

from dotenv import load_dotenv

load_dotenv()
OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
HOME_LATITUDE = os.environ.get('HOME_LATITUDE')
HOME_LONGITUDE = os.environ.get('HOME_LONGITUDE')


def get_outdoor_temperature() -> float:
    url = f"https://api.openweathermap.org/data/2.5/weather?" \
          f"lat={HOME_LATITUDE}&lon={HOME_LONGITUDE}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)
    return float(data['main']['temp'])
