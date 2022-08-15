if __name__ == "__main__":
    weather = [23, 25, 31, 12, 19, 0, 4, -5]
    weather_f = {temp:(temp * 9/5) + 32 for temp in weather}
    print(weather_f)