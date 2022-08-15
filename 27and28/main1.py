import tkinter
import turtle

if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("My First GUI Program")
    window.minsize(width= 500, height=300)

    #Label

    my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
    my_label.pack(side="left")

    tim = turtle.Turtle()
    tim.write("Some text", font=("Times New Roman", 80, "bold"))




    window.mainloop()
