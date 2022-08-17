import tkinter
from tkinter import messagebox
import data
import pyperclip

def save():
    website = w_input.get()
    email = e_input.get()
    password = p_input.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email }"
                           f"\nPassword: {password}Is it ok to save?")

    if is_ok and len(website) > 0 and len(email) > 0 and len(password) > 0:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} |{password}\n")
            w_input.delete(0, len(w_input.get()))
            p_input.delete(0, len(p_input.get()))
    else:
        messagebox.showwarning(title=website, message="Please enter your data!")

def gen():
    new_password = data.gen_password()
    p_input.insert(0, new_password)
    pyperclip.copy(new_password)


if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = tkinter.Canvas(height=200, width=200)
    lock_img = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=lock_img)
    canvas.grid(row=0, column=1)


    #Label1
    website = tkinter.Label(text="Website:")
    website.grid(row=1, column=0)

    #Label2
    email = tkinter.Label(text="Email/Username:")
    email.grid(row=2, column=0)

    #Label3
    password = tkinter.Label(text="Password:")
    password.grid(row=3, column=0)

    #Entry
    w_input = tkinter.Entry(width=35)
    w_input.grid(row=1, column=1, columnspan=2)
    w_input.focus()

    #Entry1
    e_input = tkinter.Entry(width=35)
    e_input.grid(row=2, column=1, columnspan=2)
    e_input.insert(0, "angela@gmail.com")

    #Entry2
    p_input = tkinter.Entry(width=17)
    p_input.grid(row=3, column=1)

    # Button1
    p_button = tkinter.Button(text="Generate Password", command=gen)
    p_button.grid(row=3, column=2)

    # Button2
    add_button = tkinter.Button(width=36, text="Add", command=save)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #