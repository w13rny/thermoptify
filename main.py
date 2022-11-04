from air_conditioner import set_air_conditioner
from database import insert_data
from dht_sensor import get_indoor_temperature
from weather import get_outdoor_temperature


def main():
    indoor_temperature = get_indoor_temperature()
    outdoor_temperature = get_outdoor_temperature()
    insert_data(indoor_temperature, outdoor_temperature)
    # if indoor_temperature < 19.0:
    #     set_air_conditioner(temperature=22, mode='hot', switch=True, turbo=False, fan_speed='auto')
    # if indoor_temperature > 20.5:
    #     set_air_conditioner(temperature=22, mode='hot', switch=False, turbo=False, fan_speed='auto')


if __name__ == "__main__":
    main()
