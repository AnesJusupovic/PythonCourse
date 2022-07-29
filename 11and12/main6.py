import random

logo = """
___________                        _________                      __  .__    .__                 
\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
  |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
          \/     |__|        \/          \/             \/     \/          \/        \//_____/   """
def guess(guesses):
    number = random.randint(0, 100)
    won = False
    while not won:
        guess_number = int(input("What is your guess number? "))
        if guesses == 0:
            print("You lost!")
            won = True
        else:
            if guess_number < number:
                guesses -= 1
                print("Too Low")
            elif guess_number > number:
                guesses -= 1
                print("Too high")
            elif guess_number == number:
                won = True
                print("You won")

if __name__ == "__main__":
    print(logo)
    print("Welcome to the Number Guessing Game!")
    play = True
    while play:
        val = input("Do you want to play[Y|N] ")
        if val == "Y":
            level = input("Which Level do you want to play[Easy|High] ")
            if level == "Easy":
                guess(10)
            elif level == "High":
                guess(5)
            else:
                print("Wrong input, please try again")
        elif val == "N":
            print("Goodbye!")
            play = False
        else:
            print("Wrong input!")
