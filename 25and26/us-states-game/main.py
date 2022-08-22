import turtle
import pandas


def get_mouse_click_coor(x, y):
    print(x, y)


if __name__ == "__main__":

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    game_is_on = True
    correct_guesses = 0
    data = pandas.read_csv("50_states.csv")
    correct = []
    turtle.goto(0, 0)
    while game_is_on:
        answer_state = screen.textinput(title=f"{correct_guesses}/50", prompt="What's another state's name")
        if correct_guesses == 50:
            new_data = pandas.DataFrame(correct)
            new_data.to_csv("states_to_learn.csv")
            print("Game Over!")
            game_is_on = False
        else:
            if answer_state == "exit":
                new_data = pandas.DataFrame(correct)
                new_data.to_csv("states_to_learn.csv")
                exit()
            elif data["state"].to_list().index(answer_state) > -1:
                x = int(data[data["state"] == answer_state]["x"].to_list()[0])
                y = int(data[data["state"] == answer_state]["y"].to_list()[0])
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(x, y)
                t.write(answer_state, font=("Verdana", 8, "normal"))
                correct_guesses += 1
                correct.append(answer_state)
            else:
                print("There is no State like this, please try again!")

    #turtle.onscreenclick(get_mouse_click_coor)
    #turtle.mainloop()

    #screen.exitonclick()