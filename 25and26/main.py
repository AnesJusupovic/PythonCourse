import pandas

if __name__ == "__main__":
    data = pandas.read_csv("weather_data.csv")
    print(type(data["temp"]))

    data_dict = data.to_dict()
    print(data_dict)

    temp_list = data["temp"].to_list()
    print(temp_list)
    print(sum(temp_list)/len(temp_list))

    print(data["temp"].mean())
    print(data["temp"].max())
    print(max(temp_list))

    print(data["condition"])
    print(data.condition)

    #Get Data in Row
    print(data[data.day == "Monday"])
    print(data[data.temp == 24])

    monday = data[data.day == "Monday"]
    monday_temp = int(monday.temp)
    monday_f = monday_temp * 9/5 + 32
    print(monday_f)
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data = pandas.DataFrame(data_dict)
    data.to_csv("new_data.csv")
    print(data)