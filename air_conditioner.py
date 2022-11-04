import logging
import os
from typing import Dict, Any

from dotenv import load_dotenv
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

TUYA_LOGGER.setLevel(logging.DEBUG)

load_dotenv()
ACCESS_ID = os.environ.get('TUYA_ACCESS_ID')
ACCESS_KEY = os.environ.get('TUYA_ACCESS_KEY')
API_ENDPOINT = os.environ.get('TUYA_API_ENDPOINT')
MQ_ENDPOINT = os.environ.get('TUYA_MQ_ENDPOINT')
AIR_CONDITIONER_ID = os.environ.get('TUYA_AIR_CONDITIONER_DEVICE_ID')


def get_air_conditioner_status() -> Dict[str, Any]:
    openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
    openapi.connect()
    response = openapi.get("/v1.0/iot-03/devices/{}".format(AIR_CONDITIONER_ID))
    return response


def set_air_conditioner(temperature: int, mode: str, switch: bool, turbo: bool, fan_speed: str):
    openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
    openapi.connect()
    commands = {'commands': [
        {
            "code": "temp_set",
            "value": temperature
        },
        {
            "code": "mode",
            "value": mode
        },
        {
            "code": "switch",
            "value": switch
        },
        {
            "code": "turbo",
            "value": turbo
        },
        {
            "code": "fan_speed_enum",
            "value": fan_speed
        }
    ]}
    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(AIR_CONDITIONER_ID), commands)
