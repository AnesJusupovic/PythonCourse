import tkinter

def calculate():
    result["text"] = int(input.get())*1.609

if __name__ == "__main__":

    window = tkinter.Tk()
    window.title("Mile to Km Converter")
    window.config(padx=20, pady=20)

    #Entry
    input = tkinter.Entry()
    input.grid(column=1, row=0)

    #Label
    show = tkinter.Label(text="is equal to")
    show.grid(column=0, row= 1)

    #Label
    result = tkinter.Label(text="0")
    result.grid(column=1, row=1)

    #Button
    clickOn = tkinter.Button(text="Calculate", command=calculate)
    clickOn.grid(column=1, row=2)

    #Label
    miles = tkinter.Label(text="Miles")
    miles.grid(column=2, row=0)

    # Label
    km = tkinter.Label(text="Km")
    km.grid(column=2, row=1)

    window.mainloop()