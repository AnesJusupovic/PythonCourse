import tkinter
import turtle

def button_clicked():
    my_label["text"] = input.get()

if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("My First GUI Program")
    window.minsize(width=500, height=300)
    window.config(padx=20, pady=20)

    # Label

    my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
    my_label.pack()

    my_label["text"] = "New Text"
    my_label.config(text="New Text")
    my_label.grid(column=0, row=0)

    #Button
    button = tkinter.Button(text="Click Me", command=button_clicked)
    button.grid(column=1, row=1)

    #Button1
    button = tkinter.Button(text="New Button")
    button.grid(column=2, row=0)

    #Entry
    input = tkinter.Entry(width=10)
    input.grid(column=3, row=2)

    window.mainloop()