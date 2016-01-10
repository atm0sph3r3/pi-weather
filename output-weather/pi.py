from weather.client import WeatherConnection
import RPi.GPIO as GPIO
import time
import sys

class Pi(object):
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.setup_channels()
        self.wunderground_connection = WeatherConnection(sys.argv[1])

    def output_temperature(self):
        feelslike_temp = int(self.wunderground_connection.get_feelslike_temperature())
        try:
            if feelslike_temp > 65 or feelslike_temp < 40:
                GPIO.ouput(16, 1)
                GPIO.output(20, 0)
                GPIO.output(21, 0)
            elif feelslike_temp > 55 and feelslike_temp < 65:
                GPIO.ouput(16, 0)
                GPIO.output(20, 1)
                GPIO.output(21, 0)
            else:
                GPIO.ouput(16, 0)
                GPIO.output(20, 0)
                GPIO.output(21, 1)

            time.sleep(60)
            GPIO.cleanup()
        except Exception:
            GPIO.cleanup()

    def setup_channels(self):
        channels = [16, 20, 21]
        GPIO.setup(channels, GPIO.OUT)
