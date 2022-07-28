import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

def substract(a, b):
    return a - b

def test(sum):
    type = input("What do you want to make(+/-/*//: ")
    first = int(input("First Input: "))
    second = int(input("Second Input: "))
    cont = input("Do you want to continue")
    value = 0
    if type == "+":
        value = sum + add(first, second)
    elif type == "-":
        value = sum + substract(first, second)
    elif type == "*":
        value = sum + multiply(first, second)
    elif type == "/":
        value = sum + divide(first, second)
    if cont == "Y":
        test(value)
    else:
        print(value)

if __name__ == "__main__":
    test(0)
    """"
    print(logo)
    cont = True
    while cont:
        clear = lambda: os.system('cls')
        should = input("Do you want to use the calculator? [Y/N]")
        if should == "Y":
            type = input("What do you want to make(+/-/*//: ")
            first = int(input("First Input: "))
            second = int(input("Second Input: "))
            if type == "+":
                print(add(first, second))
            elif type == "-":
                print(substract(first, second))
            elif type == "*":
                print(multiply(first, second))
            elif type == "/":
                print(divide(first, second))
        else:
            print("Finished! ")
            cont = False
    """