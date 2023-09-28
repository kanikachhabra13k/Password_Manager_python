from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have'nt left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}"
                           f"\nPassword: {password} \n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)

                with open("data.json","w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0,END)
                pass_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30,pady=30)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(column=1,row=1)

web_label = Label(text="Website:")
web_label.grid(column=0,row=2)

web_entry = Entry( width=35)
web_entry.grid(column=1,row=2,columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=3)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=3,columnspan=2)
email_entry.insert(0,"kanikachhabra13k@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0,row=4)

pass_entry = Entry(width=21)
pass_entry.grid(column=1,row=4)

gen_button = Button(text="Generate Password",command=gen_password)
gen_button.grid(column=2,row=4)

add_button = Button(text="Add",width=36,command=save_password)
add_button.grid(row=5,column=1,columnspan=2)

window.mainloop()
