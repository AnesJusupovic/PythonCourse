

if __name__ == "__main__":
    file = ""
    try:
        file = open("a_file.txt")
        a_dictionary = {"key": "value"}
        print(a_dictionary["sdfsdf"])
    except FileNotFoundError:
        file = open("a_file.txt", "w")
        print("There was a error")
    except KeyError as error_message:
        print(f"The key {error_message} does not exist.")
    else:
        content = file.read()
        print(content)
    finally:
        file.close()
        print("File was closed.")

    height = float(input("Height: "))
    weight = int(input("Weight: "))

    if height > 3:
        raise ValueError("Human Height should not be over 3 meters")
    else:
        bmi = weight / height ** 2
        print(bmi)
