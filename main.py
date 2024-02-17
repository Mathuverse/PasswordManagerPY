# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Password generator
def generate():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    password_entry.delete(0,END)
    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
def save_password():
    #ERROR BOX
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="ERROR",message="Please make sure no fields are left empty")
    else:
        answer = messagebox.askokcancel(title=website_entry.get(), message=f"Email: {e_u_entry.get()} \n Password: {password_entry.get()} \n Is it ok to save?")

        if answer:
            with open("data.txt","a") as pass_log:
                pass_log.write(f"{website_entry.get()} | {e_u_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0,END)
                e_u_entry.delete(0,END)
                password_entry.delete(0,END)
                e_u_entry.insert(0, "")


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

#Window
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

#Canvas
canvas = Canvas(width=200,height=200)
canvas.grid(row=0,column=1)
logo = PhotoImage(file="lock.png")
logo = logo.subsample(3)
canvas.create_image(100,100,image=logo)


#Labels
website_label = Label(text="Website:",font=("Arial",15,"bold"))
website_label.grid(row=1,column=0)
e_u_label = Label(text="Email/Username:",font=("Arial",15,"bold"))
e_u_label.grid(row=2,column=0)
password_label = Label(text="Password:",font=("Arial",15,"bold"))
password_label.grid(row=3,column=0)


#Entry
website_entry = Entry(width=36)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
e_u_entry = Entry(width=36)
e_u_entry.grid(row=2,column=1,columnspan=2)
e_u_entry.insert(0, "")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#Buttons
generate_pass = Button(text="Generate Password",width=11,command=generate)
generate_pass.grid(row=3,column=2)
add = Button(text="Add",width=34,command=save_password)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()