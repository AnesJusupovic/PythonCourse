import requests

KEY = "7c9c4cc77213028265aa0484f2b120b1"
MY_LAT = 35
MY_LONG = 139

if __name__ == "__main__":
    parameter = {
        "lat" : MY_LAT,
        "lon": MY_LONG,
        "exclude": "current,minutely,daily",
        "appid": KEY,
    }
    response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall?", params=parameter)
    print(response.json())