from turtle import Turtle, Screen
import random

if __name__ == "__main__":
    timmy_turtle = Turtle()
    score = 3
    color = ["green", "red", "blue", "yellow", "black", "grey", "purple"]

    for i in range(0, 10):
        color_num = random.randint(0, 6)
        timmy_turtle.color(color[color_num])
        for b in range(0, score):
            timmy_turtle.forward(100)
            timmy_turtle.right(360/score)
        score += 1