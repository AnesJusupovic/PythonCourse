import data_manager
import flight_search
import flight_data
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

if __name__ == "__main__":
    data = data_manager.DataManager()
    sheet_data = data.connect()
    flight = flight_search.FlightSearch()
    for i in range(0, len(sheet_data['prices'])):
        now = sheet_data["prices"][i]
        if len(now["iataCode"]) == 0:
            flight.add_city(now["city"], i+2)
            sheet_data["prices"][i]["iataCode"] = "TESTING"
    print(sheet_data)
    new =flight_data.FlightData()
    new.get_data()