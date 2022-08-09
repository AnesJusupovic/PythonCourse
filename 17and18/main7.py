from turtle import Turtle, Screen
import random

if __name__ == "__main__":
    timmy_turtle = Turtle()
    timmy_turtle.speed(50)
    for i in range(0, 72):
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        timmy_turtle.circle(150)
        timmy_turtle.right(5)