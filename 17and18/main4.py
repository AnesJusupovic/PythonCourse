from turtle import Turtle, Screen

if __name__ == "__main__":
    timmy_turtle = Turtle()
    for i in range(0, 4):
        timmy_turtle.forward(60)
        timmy_turtle.penup()
        timmy_turtle.forward(20)
        timmy_turtle.pendown()