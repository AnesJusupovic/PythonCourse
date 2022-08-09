from turtle import Screen
from player import Player
from car import Car
import random
import time

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.title("Crossing Bird")

    player = Player()
    screen.listen()
    screen.onkey(player.move_right, "d")
    screen.onkey(player.move_left, "a")
    screen.onkey(player.move_top, "w")
    screen.onkey(player.move_bottom, "s")

    columns = []
    screen.tracer(0)
    y_val = 200
    for i in range(0, 15):
        new_car = Car(y=y_val, x=400)
        y_val -= 30
        columns.append(new_car)

    columns_one = []
    y_val = 200
    for i in range(0, 15):
        new_car = Car(y=y_val, x=1200)
        y_val -= 30
        columns_one.append(new_car)

    columns_second = []
    y_val = 200
    for i in range(0, 15):
        new_car = Car(y=y_val, x=2000)
        y_val -= 30
        columns_second.append(new_car)

    game_is_on = True
    times = 0
    while game_is_on:
        screen.update()

        #check if won
        if player.ycor() > 290:
            print("Congratulation you won!")
            game_is_on = False
            exit()

        if times % 15 == 0:
            y_val = 200
            for i in range(0, 15):
                new_car = Car(y=y_val, x=2200)
                y_val -= 30
                columns_second.append(new_car)
        elif times % 10 == 0:
            y_val = 200
            for i in range(0, 15):
                new_car = Car(y=y_val, x=1200)
                y_val -= 30
                columns_one.append(new_car)
        elif times % 5 == 0:
            y_val = 200
            for i in range(0, 15):
                new_car = Car(y=y_val, x=400)
                y_val -= 30
                columns.append(new_car)
        time.sleep(0.2)
        #move cars
        for car_now in columns:
            car_now.move_forward()

        time.sleep(0.3)
        for car_now in columns_one:
            car_now.move_forward()

        time.sleep(0.3)
        for car_now in columns_second:
            car_now.move_forward()

        times += 1
        #check if collison with car



    screen.exitonclick()