from turtle import Turtle


class Player(Turtle):
    def __init__(self, width, height, name):
        super(Player, self).__init__()
        self.width = width
        self.height = height
        self.name = name
        self.shape("square")

    def up(self):
        pass

    def down(self):
        pass


