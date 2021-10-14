import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


def search_websites():
    try:
        with open("passwords.json", "r") as passwords_file:
            data = json.load(passwords_file)
            website = website_input.get().lower()
            email = data[website]["email/username"]
            password = data[website]["password"]
    except KeyError:
        messagebox.showwarning(title="Oops", message="No entry found for specified website")
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="No websites saved to file")
    else:
        messagebox.showinfo(title=website.title(), message=f"Email/Username: {email}\nPassword: {password}")


def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.delete(0, "end")
    password_input.insert(0, password)


def add_password():
    if not website_input.get() or not username_input.get() or not password_input.get():
        messagebox.showwarning(title="Oops", message="Make sure no field is empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered: \n"
                                                                          f"Email/Username: {username_input.get()} \n"
                                                                          f"Password: {password_input.get()} \n"
                                                                          f"Is it ok to save?")
        if is_ok:
            new_data = {website_input.get().lower(): {"email/username" : username_input.get(), "password" : password_input.get()}}
            try:
                with open("passwords.json", "r") as password_file:
                    data = json.load(password_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("passwords.json", "w") as password_file:
                    json.dump(new_data, password_file)
            else:
                with open("passwords.json", "w") as password_file:
                    json.dump(data, password_file, indent=4)
            finally:
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
website_input = Entry(width=33)
website_input.focus()
website_input.grid(column=1, row=1)
search_button = Button(text="Search", width=14, command=search_websites)
search_button.grid(column=2, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_input = Entry(width=52)
username_input.grid(column=1, row=2, columnspan=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=33)
password_input.grid(column=1, row=3)
generate_password = Button(text="Generate Password", command=generate_random_password)
generate_password.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
