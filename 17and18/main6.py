from turtle import Turtle, Screen
import random

if __name__ == "__main__":
    timmy_turtle = Turtle()

    timmy_turtle.color
    timmy_turtle.speed(10)
    timmy_turtle.pensize(15)
    for i in range(0, 200):
        steps = random.randrange(0, 40, 10)
        turn_right = random.randrange(0, 360, 90)
        color_num = random.randint(0, 4)
        timmy_turtle.forward(steps)
        timmy_turtle.right(turn_right)
