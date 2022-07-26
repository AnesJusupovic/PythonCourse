import random

if __name__ == "__main__":
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    enter = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
    if enter == 0:
        print("You choose rock")
        print(rock)
    elif enter == 1:
        print("You choose paper")
        print(paper)
    elif enter == 2:
        print("You choose scissors")
        print(scissors)
    number = random.randint(0, 2)
    print("The computer choose: \n")
    if number == 0:
        print("rock")
        print(rock)
    elif number == 1:
        print("paper")
        print(paper)
    elif number == 2:
        print("scissors")
        print(scissors)
    if enter == 0 and number == 1:
        print("You lost");
    elif enter == 0 and number == 0:
        print("You have the same as the computer have, please try again!")
    elif enter == 0 and number == 2:
        print("You won")
    elif enter == 1 and number == 2:
        print("You lost");
    elif enter == 1 and number == 1:
        print("You have the same as the computer have, please try again!")
    elif enter == 1 and number == 0:
        print("You won")
    elif enter == 2 and number == 0:
        print("You lost");
    elif enter == 2 and number == 2:
        print("You have the same as the computer have, please try again!")
    elif enter == 2 and number == 1:
        print("You won")
