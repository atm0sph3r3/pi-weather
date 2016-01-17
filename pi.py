from client import WeatherConnection
import RPi.GPIO as GPIO
import time
import sys
import configparser

class Pi(object):
    def __init__(self):
        self.wunderground_connection = WeatherConnection(sys.argv[1], sys.argv[2])
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.temp_range = config['tr']
        self.pins = config['pins']
        self.setup_channels()

    def output_temperature(self):
        feelslike_temp = int(self.wunderground_connection.get_feelslike_temperature())
        try:
            if feelslike_temp >= self.temp_range.getint('ideal_low') and feelslike_temp <= self.temp_range.getint('ideal_high'):
                GPIO.output(self.pins.getint('green'), GPIO.HIGH)
            elif feelslike_temp >= self.temp_range.getint('tolerable_low') and feelslike_temp < self.temp_range.getint('tolerable_high'):
                GPIO.output(self.pins.getint('yellow'), GPIO.HIGH)
            else:
                GPIO.output(self.pins.getint('red'), GPIO.HIGH)
            
            time.sleep(10)
        finally:
            GPIO.cleanup()

    def setup_channels(self):
        GPIO.setmode(GPIO.BOARD)
        channels = (self.pins.getint('red'), self.pins.getint('yellow'), self.pins.getint('green'))
        GPIO.setup(channels, GPIO.OUT, initial=GPIO.LOW)

pi = Pi()
pi.output_temperature()
