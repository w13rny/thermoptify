from air_conditioner import set_air_conditioner, get_air_conditioner_status
from dht_sensor import get_indoor_temperature
from google_sheet import write_data_to_google_sheet
from weather import get_outdoor_temperature


def main():
    indoor_temperature = get_indoor_temperature()
    outdoor_temperature = get_outdoor_temperature()
    ac_status = get_air_conditioner_status()
    write_data_to_google_sheet(indoor_temperature, outdoor_temperature, ac_status)
    # if indoor_temperature < 19.0:
    #     set_air_conditioner(temperature=22, mode='hot', switch=True, turbo=False, fan_speed='auto')
    # if indoor_temperature > 20.5:
    #     set_air_conditioner(temperature=22, mode='hot', switch=False, turbo=False, fan_speed='auto')


if __name__ == "__main__":
    main()
