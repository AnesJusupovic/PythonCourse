from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    make = True
    machine = CoffeeMaker()
    menu = Menu()
    while make:
        should = input("Do you want to make a Coffee[Y|N]: ")
        if should == "Y":
            type = input("What would you like? (espresso/latte/cappuccino/): ")
            if type == "espresso":
                if machine.is_resource_sufficient(menu.find_drink("esspresso")):
                    machine.make_coffee(menu.find_drink("espresso"))
                else:
                    print("Not enough ressources")
            elif type == "latte":
                if machine.is_resource_sufficient(menu.find_drink("latte")):
                    machine.make_coffee(menu.find_drink("latte"))
                else:
                    print("Not enough ressources!")
            elif type == "cappuccino":
                if machine.is_resource_sufficient(menu.find_drink("cappuccino")):
                    machine.make_coffee(menu.find_drink("cappuccino"))
                else:
                    print("Not enough ressources")
            elif type == "report":
                machine.report()
            else:
                print("Wrong input! ")
        elif should == "N":
            make = False
            print("Goodbye!")
        else:
            print("Wrong input!")