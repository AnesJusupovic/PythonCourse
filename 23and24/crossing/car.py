from turtle import Turtle
import random


class Car(Turtle):

    def __init__(self, y, x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.x = x
        self.y = y
        self.goto(self.x, self.y)
        self.color("black")

    def move_forward(self):
        self.x -= random.randrange(0, 50, 4)
        self.goto(self.x, self.y)
