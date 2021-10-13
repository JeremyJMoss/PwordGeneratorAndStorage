from tkinter import *
from tkinter import messagebox
from typing import TextIO


def add_password():
    if not website_input.get() or not username_input.get() or not password_input.get():
        messagebox.showwarning(title="Oops", message="Make sure no field is empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered: \n"
                                                                          f"Email/Username: {username_input.get()} \n"
                                                                          f"Password: {password_input.get()} \n"
                                                                          f"Is it ok to save?")

        if is_ok:
            with open("passwords.txt", "a") as password_file:
                password_file.write(f"{website_input.get()} | {username_input.get()} | {password_input.get()}\n")
            website_input.delete(0, "end")
            username_input.delete(0, "end")
            password_input.delete(0, "end")
            website_input.focus()


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=52)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_input = Entry(width=52)
username_input.grid(column=1, row=2, columnspan=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=33)
password_input.grid(column=1, row=3)
generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
