# ---------------constants----------------------------------
import json
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


# --------------------------------------------Password Generator--------------------------------
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list.extend(numbers_list)
    password_list.extend(symbols_list)
    shuffle(password_list)

    x = "".join(password_list)
    password_entry.insert(END, string=f"{x}")
    # to save to clipboard
    pyperclip.copy(text=f"{x}")


# --------------------------------Saving the password to a file------------------------------------
def save():
    website_info = str(website_entry.get())
    email_info = str(email_entry.get())
    password_info = str(password_entry.get())

    new_dict = {website_info: {
        "email": email_info,
        "password": password_info
    }}

    if len(website_info) and len(password_info) == 0:
        messagebox.showinfo(title="Error", message="You need to fill the required fields")



    else:
        try:
            with open("data.json", mode="r") as data_file:
                # ========READING OLD DATA======
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_dict, data_file, indent=4)

        else:
            # =========UPDATING DATA========
            data.update(new_dict)

            with open("data.json", mode="w") as data_file:
                # ========SAVING UPDATED DATA===========
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------------------Search Button-----------------------------------
def find_password():
    website_info = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", messsage="No data found")
    else:
        if data == website_info:
            email = data[website_info]["email"]
            password = data[website_info]["password"]
            messagebox.showinfo(title=f"{website_info}", message=f"email: {email}\npassword:{password}")
        else:
            messagebox.showerror(title="Error", message=f"no details for {website_info} exits")


# --------------------------------UI SETUP-------------------------------------------------------
# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# photo image
photo_image = PhotoImage(file='logo.png')

# canvas
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo_image)
canvas.grid(column=1, row=0)

# label
website = Label(text="Website:", font=("aries", 13, "normal"))
website.grid(column=0, row=1)

email = Label(text="Email/Username:", font=("aries", 13, "normal"))
email.grid(column=0, row=2)

password = Label(text="Password:", font=("aries", 13, "normal"))
password.grid(column=0, row=3)

# entry
website_entry = Entry(width=36)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=36)
email_entry.insert(END, string="ogunbanjotosin106@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
# button
generate_password = Button(text="Generate Password", command=gen_pass)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=31, command=save)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=13, command=find_password)
search.grid(column=3, row=1)
# window mainloop
window.mainloop()
