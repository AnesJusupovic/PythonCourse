from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = -280
        self.shape("turtle")
        self.penup()
        self.speed(10)
        self.right(270)
        self.update()

    def update(self):
        self.goto(self.x, self.y)

    def move_right(self):
        self.x += 10
        self.update()

    def move_left(self):
        self.x -= 10
        self.update()

    def move_top(self):
        self.y += 10
        self.update()

    def move_bottom(self):
        self.y -= 10
        self.update()

