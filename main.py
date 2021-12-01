from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_passwords():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbol
    random.shuffle(password_list)
    password = "".join(password_list)
    generated_password.insert(0, password)
    pyperclip.copy(password)


def save():
    website_nam = website_name.get()
    your_username = email_username.get()
    your_password = generated_password.get()
    if len(website_nam) == 0 or len(your_password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you  have not left any field empty.")

    is_ok = messagebox.askokcancel(title=website_nam, message=f"These are the details entered:\nEmail: {your_username}\n"
                                                              f"Password:{your_password}\nIs it ok to save?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website_nam}| {your_username} | {your_password}\n")
            website_name.delete(0, END)
            generated_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
website = Label(text="website:")
website.grid(row=1, column=0)
website_name = Entry(width=35)
website_name.grid(row=1, column=1, columnspan=2)
website_name.focus()
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
email_username = Entry(width=35)
email_username.grid(row=2, column=1, columnspan=2)
email_username.insert(0, "kneupane800@gmail.com")
password = Label(text="Password:")
password.grid(row=3, column=0)

generated_password = Entry(width=21)
generated_password.grid(row=3, column=1)
generate_password = Button(text="Generate Password", command=generate_passwords)
generate_password.grid(row=3, column=2)
add = Button(text="add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)
canvas.grid(row=0, column=1)

window.mainloop()
