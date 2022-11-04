from datetime import datetime


def insert_data(indoor_temperature: float, outdoor_temperature: float):
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    file = open("data.txt", "a")
    file.write(f"{now}\t{indoor_temperature}°C\t{outdoor_temperature}°C\n")
    file.close()
