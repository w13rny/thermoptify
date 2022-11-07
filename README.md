# thermoptify

This is a simple program designed for Rasperry Pi single-board computer.
Application changes the settings of the heating device (Tuya Air Conditioner) based on the data collected from DHT22 sensor (indoor temperature) and OpenWeatherAPI (outdoor temperature).

# Prerequisites

## Raspberry Pi

This project was originally designed for **Raspberry Pi 2 model B** working on the **Raspberry Pi OS (32-bit)** released on **2022-09-22**.

## DHT22 temperature & humidity sensor

This project requires **DHT22 sensor** connected as shown in the diagram below.

```
              ┌─┬─┐
VCC pin - 3V3 │●│○│ 5V
          #00 │○│○│ 5V
          #01 │○│●│ GND - GND pin
          #04 │○│○│ #14
          GND │○│○│ #15
          #17 │○│●│ #18 - OUT pin (through 4.7-10K pull-up resistor)
          #21 │○│○│ GND
          #22 │○│○│ #23
          3V3 │○│○│ #24
          #10 │○│○│ GND
          #09 │○│○│ #25
          #11 │○│○│ #08
          GND │○│○│ #07
              └─┴─┘
```

## Tuya Air Conditioner

This project is developed for a specific model of air conditioner working in Tuya Cloud.
Whole process of registering an account, creating the project, adding the Tuya device and working with Tuya API is described here: https://developer.tuya.com/en/demo/python-iot-development-practice

## OpenWeatherMap API

This project require API key for OpenWeatherMap. Create the free account and get your API key here:
https://openweathermap.org/api

# Installation

1. Clone this repository.

```
git clone https://github.com/w13rny/thermoptify.git
```

2. Go to the project directory and install all dependencies.

```
cd thermoptify
pip3 install -r requirements.txt
```

3. Install the `libgpoid2` (required to correctly read the values from the GPIO pins).

```
sudo apt-get install libgpiod2
```

# Configuration

Create .env configuration file and fill it with proper data.

```
TUYA_ACCESS_ID=''
TUYA_ACCESS_KEY=''
TUYA_API_ENDPOINT=''
TUYA_MQ_ENDPOINT=''
TUYA_AIR_CONDITIONER_DEVICE_ID=''
OPENWEATHERMAP_API_KEY=''
HOME_LATITUDE=''
HOME_LONGITUDE=''
```

# Run

## Run once

Run the `main.py` file.

```
python3 main.py
```

## Run periodically

Add following line to `crontab`:

```
10 * * * * python3 /path/to/main.py
```