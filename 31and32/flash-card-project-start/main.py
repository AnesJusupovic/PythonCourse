import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
number = 0

def reject():
    global number
    number = random.randint(0, 100)
    text = data_dict["French"][number]
    canvas.itemconfig(bottom_line, text=f"{text}")

def accept():
    english_text = data_dict["English"][number]
    canvas.itemconfig(top_line, text="English")
    canvas.itemconfig(bottom_line, text=f"{english_text}")
    canvas.itemconfig(canvas_image, image=card_back)
    window.after(3000, back)

def back():
    french_text = data_dict["French"][number]
    english_text = data_dict["English"][number]
    canvas.itemconfig(top_line, text="French")
    canvas.itemconfig(bottom_line, text=f"{french_text}")
    canvas.itemconfig(canvas_image, image=card_front)
    dict_data = {"French": french_text, "English": english_text}
    data_new = pandas.DataFrame(dict_data, index=[0])
    data_new.to_csv("right_words.csv")
    data.drop(number)

if __name__ == "__main__":
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict()
    window = tkinter.Tk()
    window.title("Flashly")
    window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

    # Card
    canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_front = tkinter.PhotoImage(file="images/card_front.png")
    card_back = tkinter.PhotoImage(file="images/card_back.png")
    canvas_image = canvas.create_image(400, 263, image=card_front)
    top_line = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    bottom_line = canvas.create_text(400, 263, text="partie", font=("Ariel", 60, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)


    #Buttons
    wrong = tkinter.PhotoImage(file="images/wrong.png")
    cancel = tkinter.Button(image=wrong, command=reject)
    cancel.configure(background=BACKGROUND_COLOR, bd=0)
    cancel.grid(column=0, row=1)

    right = tkinter.PhotoImage(file="images/right.png")
    apply = tkinter.Button(image=right, command=accept)
    apply.configure(background=BACKGROUND_COLOR, bd=0)
    apply.grid(column=1, row=1)




    window.mainloop()
