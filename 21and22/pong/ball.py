from turtle import Turtle


def left_down(self, x, y):
    value = []
    if x < -280:
        print("You lost!")
        exit()
    else:
        new_x = x - 10
        new_y = y - 10
        self.goto(new_x, new_y)
        value.append(new_x)
        value.append(new_y)
        return value
    return value


def left_up(self, x, y):
    value = []
    if x < -280:
        print("You lost!")
        exit()
    else:
        new_x = x - 10
        new_y = y + 10
        self.goto(new_x, new_y)
        value.append(new_x)
        value.append(new_y)
    return value


def right_up(self, x, y):
    value = []
    if x < -280:
        print("You lost!")
        exit()
    else:
        new_x = x + 10
        new_y = y + 10
        self.goto(new_x, new_y)
        value.append(new_x)
        value.append(new_y)
    return value


def right_down(self, x, y):
    value = []
    if x < -280:
        print("You lost!")
        exit()
    else:
        new_x = x + 10
        new_y = y - 10
        self.goto(new_x, new_y)
        value.append(new_x)
        value.append(new_y)
    return value


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")

    def move(self, direction, y_scale, x, y):
        if direction == "left":
            if y_scale == "down":
                left_down(self=self, x=x, y=y)
            elif y_scale == "up":
                left_up(self=self, x=x, y=y)
            else:
                print("Error")
        elif direction == "right":
            if y_scale == "down":
                right_down(self=self, x=x, y=y)
            elif y_scale == "up":
                right_up(self=self, x=x, y=y)
            else:
                print("Error")
