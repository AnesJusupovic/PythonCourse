import requests

class FlightData:

    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.apikey = "BiVmX6A5ul0uQUNxkatnGHTZ_DcCFpSZ"
        self.headers = {
            "apikey": self.apikey
        }
        self.content = {
            "fly_from": "DE",
            "date_from": "28/08/2022",
            "date_to": "28/12/2022",
        }

    def get_data(self):
        response = requests.get(url=self.endpoint, params=self.content, headers=self.headers)
        print(response.json())
        print(response.status_code)