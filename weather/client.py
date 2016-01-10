import requests
import json


class WeatherConnection(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "http://api.wunderground.com"

    def get_current_conditions(self):
        response = requests.get("{baseurl}/api/{key}/conditions/q/21784.json".format(baseurl=self.url, key=self.api_key))
        return response.text

    def get_feelslike_temperature(self):
        output = self.get_current_conditions()
        json_loaded = json.loads(output)
        return json_loaded['current_observation']['feelslike_f']
