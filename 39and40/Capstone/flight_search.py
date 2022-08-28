import requests
from pprint import pprint
import data_manager
class FlightSearch:

    API_KEY = "BiVmX6A5ul0uQUNxkatnGHTZ_DcCFpSZ"
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            ''
        }
        self.endpoint = ""
        self.cities = []

    def connect(self):
        response = requests.get(url=self.endpoint, headers=self.headers)

    def add_city(self, city, index):
        self.cities.append(city)
        manager = data_manager.DataManager()
        manager.change(index)
