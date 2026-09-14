from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter=[choice(letters) for _ in range(randint(8,10))]
    password_number=[choice(numbers) for _ in range(randint(2,4))]
    password_symbol=[choice(symbols) for _ in range(randint(2,4))]

    password_list=password_letter+password_number+password_symbol
    shuffle(password_list)

    password = "".join(password_list)

    pass_ip.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website=website_ip.get()
    email=email_ip.get()
    password=pass_ip.get()

    new_data={
        website.title():{
            "email/username":email,
            "password":password,
        }
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open(file="./Day-030/Day-029 Improved Version/password_data.json",mode="r") as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open(file="./Day-030/Day-029 Improved Version/password_data.json",mode="w") as data_file:
                json.dump(new_data,data_file,indent=4)
                
        except json.JSONDecodeError:
            with open(file="./Day-030/Day-029 Improved Version/password_data.json",mode="w") as data_file:
                json.dump(new_data,data_file,indent=4)

        else:
            #Updating Old data with New data
            data.update(new_data)
            with open(file="./Day-030/Day-029 Improved Version/password_data.json",mode="w") as data_file:
                json.dump(data,data_file,indent=4)

        finally:
            website_ip.delete(0,END)
            email_ip.delete(0,END)
            pass_ip.delete(0,END)

# ---------------------------- SEARCH DATA ------------------------------- #

def search_data():
    website=website_ip.get().title()
    try:
        with open(file="./Day-030/Day-029 Improved Version/password_data.json",mode="r") as data_file:
            data=json.load(data_file)
        email=data[website]["email/username"]
        password=data[website]["password"]

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found.")

    except KeyError:
        messagebox.showinfo(title="Error",message="No Such Data in Database.")

    else:
        messagebox.showinfo(title=website,message=f"Email/Username: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200,highlightthickness=0)
logo_img=PhotoImage(file="./Day-029/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_txt=Label(text="Website:")
website_txt.grid(column=0,row=1)

website_ip=Entry(width=25)
website_ip.grid(column=1,row=1)

search_button=Button(text="Search",width=15,command=search_data)
search_button.grid(column=2,row=1)

email_txt=Label(text="Email/Username:")
email_txt.grid(column=0,row=2)

email_ip=Entry(width=43)
email_ip.grid(column=1,row=2,columnspan=2)

pass_txt=Label(text="Password:")
pass_txt.grid(column=0,row=3)

pass_ip=Entry(width=22)
pass_ip.grid(column=1,row=3)

generate_pass_button=Button(text="Generate Password",command=generate_pass)
generate_pass_button.grid(column=2,row=3)

add_button=Button(text="Add",width=36,command=save_data)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()