import requests
from pprint import pprint

class DataManager:

    endpoint = "https://api.sheety.co/9c4fc2f5b38685218944133b2f967b9c/flightDeals/prices"
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def connect(self) -> map:
        response = requests.get(url=self.endpoint)
        return response.json()

    def change(self, row):
        new_endpoint = f"{self.endpoint}/{row}"
        print(new_endpoint)
        body = requests.get(url=new_endpoint).json()
        body["price"]["iataCode"] = "Testing"
        response_two = requests.put(url=new_endpoint, json=body)