from tkinter import *


def start():
    update(0, 1)


def update(second, round):
    new_second = second
    if round == 5:
        print("Finished")
        exit()
    if second % 1500 == 0:
        round += 1
        pause(0)
        new_second = 0
    new_second += 1
    if second % 60 == 0:
        canvas.itemconfig(my_text, text=f"{second / 60}:00")
    elif second % 60 != 0:
        min = int((second - second % 60) / 60)
        canvas.itemconfig(my_text, text=f"{int(min)}:{second % 60}")
    window.after(1000, update, new_second, round)


def pause(second):
    if second == 300:
        print("Passes Test")
        pass
    else:
        second += 1
        if second % 60 == 0:
            canvas.itemconfig(my_text, text=f"{second / 60}:00")
        elif second % 60 != 0:
            min = int((second - second % 60) / 60)
            canvas.itemconfig(my_text, text=f"{int(min)}:{second % 60}")
        window.after(1000, pause, second)

def end():
    exit()

if __name__ == "__main__":
    # ---------------------------- CONSTANTS ------------------------------- #
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT_NAME = "Courier"
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20

    # ---------------------------- TIMER RESET ------------------------------- #

    # ---------------------------- TIMER MECHANISM ------------------------------- #

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    #Label
    text = Label(text="Timer", fg="green", font=("Times New Roman", 26, "bold"), bg=YELLOW)
    text.pack()

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    my_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.pack()

    #Button1
    first = Button(text="Start", bg="white", command=start)
    first.pack(side="left")

    #Button2
    second = Button(text="Reset", bg="white", command=end)
    second.pack(side="right")

    window.mainloop()

