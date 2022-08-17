def login(name, password):
    with open("log_data.txt", mode="r") as file:
        lines = file.readlines()
        check = lines[0].split(",")
        if check[0] == name and check[1] == password:
            print("Success")
        else:
            print("Failed to login!")


def register(name, password):
    with open("log_data.txt", mode="w") as file:
        file.writelines(f"{name},{password}")
    print("Success!")

if __name__ == "__main__":
    print("Welcome to Blackchat!")
    option = input("Login or Register ( login, reg): \n")
    should_run = True
    while should_run:
        if option == "login":
            name = input("Whats your name: ")
            password = input("Whats your password: ")
            login(name, password)
            should_run = False
        elif option == "register":
            name = input("Whats your name: ")
            password = input("Whats your password: ")
            register(name, password)
            should_run = False
        else:
            print("Wrong input please try again!")
            option = input("Login or Register ( login, reg): \n")



