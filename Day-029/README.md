# 🔐 Day 029 - Password Manager

## 📌 Project Overview

Day 29 focuses on building a **Password Manager GUI application** using Python's **Tkinter** library.

The application allows the user to:

* Enter a website
* Enter an email/username
* Generate a random password
* Save the website, email/username, and password to a text file
* Confirm the details before saving
* Automatically clear the input fields after successfully saving

The project combines **GUI programming, file handling, random password generation, lists, functions, and message boxes**.

---

# 🎯 Project Features

* 🔐 Password Manager GUI
* 🎲 Random password generator
* 🌐 Website input
* 📧 Email/Username input
* 🔑 Password input
* 💾 Save credentials to a file
* ⚠️ Empty-field validation
* ✅ Confirmation dialog before saving
* 🧹 Automatically clears fields after saving
* 🖥️ Tkinter-based graphical interface

---

# 🔑 Password Generator

The password generator creates a random password using:

* Uppercase letters
* Lowercase letters
* Numbers
* Symbols

The character sets are stored in separate lists:

```python id="1i9y9p"
letters = [...]
numbers = [...]
symbols = [...]
```

---

## 🎲 Random Password Generation

The number of characters from each category is randomized.

### Letters

```python id="8q0p2z"
password_letter = [
    choice(letters)
    for _ in range(randint(8, 10))
]
```

The program generates between **8 and 10 letters**.

### Numbers

```python id="s4v3m8"
password_number = [
    choice(numbers)
    for _ in range(randint(2, 4))
]
```

The program generates between **2 and 4 numbers**.

### Symbols

```python id="9wq8mj"
password_symbol = [
    choice(symbols)
    for _ in range(randint(2, 4))
]
```

The program generates between **2 and 4 symbols**.

---

## 🔀 Shuffling the Password

The generated characters are combined:

```python id="u9x0vp"
password_list = password_letter + password_number + password_symbol
```

Then the characters are randomly shuffled:

```python id="q7m3dz"
shuffle(password_list)
```

Finally, the list is converted into a string:

```python id="g7n3kx"
password = "".join(password_list)
```

This prevents the password from always following the same order of letters → numbers → symbols.

---

## 📝 Automatically Filling the Password Field

The generated password is inserted into the password entry box:

```python id="b2p7sa"
pass_ip.insert(0, password)
```

---

# 💾 Saving Password Data

The `save_data()` function retrieves the values entered by the user:

```python id="j4s2nc"
website = website_ip.get()
email = email_ip.get()
password = pass_ip.get()
```

---

## ⚠️ Input Validation

Before saving, the program checks whether any field is empty:

```python id="h8x4qa"
if len(website) == 0 or len(email) == 0 or len(password) == 0:
```

If a field is empty, a message box is displayed:

```python id="p5f7zd"
messagebox.showinfo(
    title="Oops",
    message="Please make sure you haven't left any field empty."
)
```

---

# ✅ Confirmation Before Saving

If all fields contain data, the program asks the user to confirm the information:

```python id="v5y2rx"
is_ok = messagebox.askokcancel(
    title=website,
    message=f"These are the details entered:"
            f"\nEmail/Username: {email}"
            f"\nPassword: {password}"
            f"\nIs it okay to save?"
)
```

The data is saved only when the user selects **OK**.

---

# 📄 File Handling

The password information is stored in:

```text id="f3v6pz"
password_data.txt
```

The file is opened in append mode:

```python id="z5m8kw"
with open(
    file="./Day-029/password_data.txt",
    mode="a"
) as data:
```

Using `"a"` ensures that new credentials are **added to the existing file** instead of overwriting previous entries.

Each saved entry follows this format:

```text id="e4m1ry"
website|email/username|password
```

For example:

```text id="q7j8hx"
example.com|user@example.com|MyPassword123!
```

---

# 🧹 Clearing the Input Fields

After successfully saving the credentials, all input fields are cleared:

```python id="x3q5nr"
website_ip.delete(0, END)
email_ip.delete(0, END)
pass_ip.delete(0, END)
```

This prepares the application for entering another password.

---

# 🖥️ Graphical User Interface

The application is built using **Tkinter**.

The main window is configured with:

```python id="r6n9kt"
window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)
```

---

## 🖼️ Logo

A logo image is displayed using a Tkinter `Canvas`:

```python id="c8m2vy"
canvas = Canvas(
    width=200,
    height=200,
    highlightthickness=0
)

logo_img = PhotoImage(file="./Day-029/logo.png")

canvas.create_image(
    100,
    100,
    image=logo_img
)
```

---

# 🧩 Tkinter Widgets Used

| Widget       | Purpose                                    |
| ------------ | ------------------------------------------ |
| `Tk()`       | Creates the main application window        |
| `Canvas`     | Displays the application logo              |
| `Label`      | Displays field names                       |
| `Entry`      | Accepts website, username, and password    |
| `Button`     | Generates passwords and saves data         |
| `messagebox` | Displays warnings and confirmation dialogs |

---

# 📐 GUI Layout

The interface is arranged using Tkinter's `grid()` geometry manager.

```text id="z9q1xk"
             [ 🔐 Logo ]

Website:       [________________________]

Email/Username:[________________________]

Password:      [____________] [Generate Password]

               [          Add           ]
```

---

# 🔄 Program Flow

```text id="j7d4pk"
Start Application
       ↓
Enter Website
       ↓
Enter Email/Username
       ↓
Generate Password
       ↓
Password Automatically Filled
       ↓
Click Add
       ↓
Check Empty Fields
       ↓
 ┌─────┴─────┐
 ↓           ↓
Empty       Filled
 ↓           ↓
Warning    Confirmation
             ↓
        Confirm Saving
             ↓
        Save to File
             ↓
        Clear Fields
```

---

# 🧠 Code Concepts Used

## Tkinter

* `Tk()`
* `Label`
* `Entry`
* `Button`
* `Canvas`
* `PhotoImage`
* `messagebox`
* `grid()`
* `mainloop()`

## Random Module

The project uses:

```python id="j5c8qp"
from random import randint, choice, shuffle
```

* `choice()` → Selects a random character
* `randint()` → Determines random character counts
* `shuffle()` → Randomizes the password character order

## File Handling

* `open()`
* Append mode `"a"`
* `write()`
* `with open()`

## String Handling

* `.join()`
* `.get()`
* `.delete()`
* `.insert()`
* f-strings

## Functions

The project separates its functionality into:

```python id="p6y4mt"
generate_pass()
save_data()
```

This keeps password generation and saving logic separate.

---

# 📂 Project Structure

```text id="q4v8sc"
Day-029/
│
├── main.py
├── logo.png
├── password_data.txt
└── README.md
```

### File Description

| File                | Purpose                                           |
| ------------------- | ------------------------------------------------- |
| `main.py`           | Contains the Password Manager application         |
| `logo.png`          | Logo displayed in the GUI                         |
| `password_data.txt` | Stores saved website, username, and password data |
| `README.md`         | Project documentation                             |

---

# 🛠️ Technologies Used

* **Python**
* **Tkinter**
* **Random Module**
* **File Handling**
* **GUI Programming**

---

# 🎯 Learning Outcome

Through Day 29, I learned how to combine multiple Python concepts to create a practical GUI application.

Key concepts practiced:

* Building GUI applications with Tkinter
* Creating and using Entry widgets
* Connecting buttons to functions
* Generating random passwords
* Using list comprehensions
* Shuffling lists
* Reading user input from GUI fields
* Validating user input
* Displaying message boxes
* Saving data to a text file
* Appending data without overwriting previous entries
* Clearing Tkinter Entry widgets

---

# 🚀 Future Improvements

Possible improvements include:

* Store passwords in a more secure/encrypted format
* Add a search feature for saved credentials
* Add a password visibility toggle
* Prevent duplicate website entries
* Add stronger password customization options
* Use JSON or a database instead of a plain text file
* Add a master password for accessing saved credentials

> **Security Note:** This project is designed for learning purposes. Storing passwords as plain text is not suitable for a real-world password manager.

---

# ✅ Project Status

**Completed ✔️**

* [x] Create Password Manager GUI
* [x] Add website input
* [x] Add email/username input
* [x] Add password input
* [x] Generate random passwords
* [x] Include letters, numbers, and symbols
* [x] Shuffle generated passwords
* [x] Validate empty fields
* [x] Confirm data before saving
* [x] Save credentials to a text file
* [x] Clear fields after saving

---

# 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
