from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# UI setup
window = Tk()
window.config(width=500, height=500, padx=50, pady=50, bg="white")
window.title("Password Generator")


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
               'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
               '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '!', '#', '$', '%', '&', '(', ')', '*', '+', '!', '#', '$',
               '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(5, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    ran_letter = [random.choice(letters) for _ in range(nr_letters)]
    ran_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    ran_number = [random.choice(numbers) for _ in range(nr_numbers)]
    final_password = ran_letter + ran_symbol + ran_number
    random.shuffle(final_password)
    password = ""
    for y in final_password:
        password += y
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# Saving the data into a file


def save():
    website_entered = website_entry.get().title()
    password_entered = password_entry.get()
    email_username_entered = email_username_entry.get()
    text = f"{website_entered} | {email_username_entered} | {password_entered}\n"
    if len(website_entered) and len(password_entered) > 0:
        correct = messagebox.askokcancel(title="Conformation!!", message=f"Are all the information correct?\nWebsite:{website_entered}\nEmail/Username:{email_username_entered}\nPassword:{password_entered}")
        if correct:
            with open("password manager.txt", "a") as file:
                file.write(text)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Successful", message="You entries were saved successfully")
    else:
        messagebox.showinfo(title="Alert", message="You have not entered all the fields")


# Image setup
canvas = Canvas()
lock = PhotoImage(file="lock.png")
canvas.config(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

# Label setup
website_label = Label()
website_label.config(text="Website:", font=("Arial", 10, "normal"), bg="white")
website_label.grid(row=1, column=0)

email_username_label = Label()
email_username_label.config(text="Email/Username:", font=("Arial", 10, "normal"), bg="white")
email_username_label.grid(row=2, column=0)

password_label = Label()
password_label.config(text="Password:", font=("Arial", 10, "normal"), bg="white")
password_label.grid(row=3, column=0)

# Entry setup
website_entry = Entry()
website_entry.config(width=35,  bg="white")
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# Email/Username entry
email_username_entry = Entry()
email_username_entry.config(width=35, bg="white", highlightthickness=0)
email_username_entry.insert(0, "sujendra2001@gmail.com")
email_username_entry.grid(row=2, column=1, columnspan=2)

# Password entry
password_entry = Entry()
password_entry.config(width=21, bg="white", highlightthickness=0)
password_entry.grid(row=3, column=1)

# Generate password button

generate_password_button = Button()
generate_password_button.config(text="Generate Password", font=("Arial", 7, "normal"), bg="white", width=13, highlightthickness=0, command=generate_password)
generate_password_button.grid(row=3, column=2)

# Add button
add_button = Button()
add_button.config(text="Add", font=("Arial", 10, "normal"), bg="white", width=27, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
