MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def ask():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.01
    dimes = int(input("How many dimes?: ")) * 0.05
    nickles = int(input("How many nickles?: ")) * 0.10
    pennies = int(input("How many pennies?: ")) * 0.25
    money = quarters + dimes + nickles + pennies
    print(f"Money is {money}")
    return money

if __name__ == "__main__":
    run = True
    water = 300
    milk = 200
    coffee = 100
    money = 0
    while run:
        type = input("What would you like? (espresso/latte/cappuccino): ")
        if type == "espresso":
            money += ask()
            if MENU["espresso"]["cost"] <= money:
                if MENU["espresso"]["ingredients"]["water"] <= water:
                    if MENU["espresso"]["ingredients"]["milk"] <= milk:
                        if MENU["espresso"]["ingredients"]["coffee"] <= coffee:
                            water -= MENU["espresso"]["ingredients"]["water"]
                            milk -= MENU["espresso"]["ingredients"]["milk"]
                            coffee -= MENU["espresso"]["ingredients"]["coffee"]
                            money -= MENU["espresso"]["cost"]
                            print("Here is your espresso :D")
                            print(f"Water: {water}, Milk: {milk}, Coffee: {coffee}, Money: {money}")
                        else:
                            print("To less coffee!")
                    else:
                        print("To less milk!")
                else:
                    print("To less water!")
            else:
                run = False
                print("To less money!")
        elif type == "latte":
            money += ask()
            if MENU["latte"]["cost"] <= money:
                if MENU["latte"]["ingredients"]["water"] <= water:
                    if MENU["latte"]["ingredients"]["milk"] <= milk:
                        if MENU["latte"]["ingredients"]["coffee"] <= coffee:
                            water -= MENU["latte"]["ingredients"]["water"]
                            milk -= MENU["latte"]["ingredients"]["milk"]
                            coffee -= MENU["latte"]["ingredients"]["coffee"]
                            money -= MENU["latte"]["cost"]
                            print("Here is your latte :D")
                            print(f"Water: {water}, Milk: {milk}, Coffee: {coffee}, Money: {money}")
                        else:
                            print("To less coffee!")
                    else:
                        print("To less milk!")
                else:
                    print("To less water!")
            else:
                run = False
                print("To less money!")
        elif type == "cappuccino":
            money += ask()
            if MENU["cappuccino"]["cost"] <= money:
                if MENU["cappuccino"]["ingredients"]["water"] <= water:
                    if MENU["cappuccino"]["ingredients"]["milk"] <= milk:
                        if MENU["cappuccino"]["ingredients"]["coffee"] <= coffee:
                            water -= MENU["cappuccino"]["ingredients"]["water"]
                            milk -= MENU["cappuccino"]["ingredients"]["milk"]
                            coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
                            money -= MENU["cappuccino"]["cost"]
                            print("Here is your cappuccino :D")
                            print(f"Water: {water}, Milk: {milk}, Coffee: {coffee}, Money: {money}")
                        else:
                            print("To less coffee!")
                    else:
                        print("To less milk!")
                else:
                    print("To less water!")
            else:
                run = False
                print("To less money!")
        elif type == "Nothing":
            run = False
            print("Goodbye!")
        else:
            print("Wrong input!")