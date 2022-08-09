from turtle import Turtle, Screen


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.height = 20
        self.width = 20
        self.x_move = 10
        self.y_move = 19
        self.shape("circle")
        self.circle(radius=self.height/2)
        self.goto(x=0, y=0)
        self.color("white")
        self.penup()
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed * 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed * 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()