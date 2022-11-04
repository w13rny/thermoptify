import time
import adafruit_dht
from board import D18


def get_temperature_and_humidity() -> tuple:
    sensor = adafruit_dht.DHT22(D18)
    while True:
        try:
            temperature = sensor.temperature
            humidity = sensor.humidity
            return temperature, humidity
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            sensor.exit()
            raise error


def get_indoor_temperature() -> float:
    sensor = adafruit_dht.DHT22(D18)
    while True:
        try:
            temperature = sensor.temperature
            return temperature
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            sensor.exit()
            raise error
