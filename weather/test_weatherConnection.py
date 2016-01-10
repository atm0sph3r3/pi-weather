from unittest import TestCase
from weather.client import WeatherConnection

class TestWeatherConnection(TestCase):
    def test_make_request(self):
        connection = WeatherConnection()
        connection.get_current_temperature()


