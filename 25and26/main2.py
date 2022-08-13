import pandas

if __name__ == "__main__":

    data = pandas.read_csv("2018_Central_Park_Squirrel_Count.csv")
    gray = len(data[data["Primary Fur Color"] == "Gray"])
    cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black = len(data[data["Primary Fur Color"] == "Black"])
    data_dict = {
        "Fur Color": ["grey", "red", "black"],
        "Count": [gray, cinnamon, black]
    }

    data = pandas.DataFrame(data_dict)
    data.to_csv("squirrel_count.csv")