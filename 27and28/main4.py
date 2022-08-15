import tkinter
import turtle

if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("My First GUI Program")
    window.minsize(width=500, height=300)

    # Label

    my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
    my_label.pack()

    my_label["text"] = "New Text"
    my_label.config(text="New Text")

    #Button
    def button_clicked():
        my_label["text"] = input.get()

    button = tkinter.Button(text="Click Me", command=button_clicked)
    button.pack()


    #Entry

    input = tkinter.Entry(width=10)
    input.pack()

    window.mainloop()