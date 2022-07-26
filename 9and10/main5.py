import os

if __name__ == "__main__":
    logo = '''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    '''
    print(logo)
    bid_number = int(input("How many biders are there? "))
    clear = lambda : os.system('cls')
    person = {}
    high = 0
    keyword = ""
    for i in range(0, bid_number):
        name = input("What is your name")
        bid = input("How many do you want to bid?")
        person[name] = bid
    for keys in person:
        if int(person[keys]) > high:
            high = int(person[keys])
            keyword = keys
    print(f"{keys} won the auction with {high}")
