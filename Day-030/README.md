# 🛡️ Day 030 - Exception Handling & Error Management

## 📌 Project Overview

Day 30 focuses on **Error Handling and Exceptions in Python**.

This day contains three related sections:

1. 📡 **Improved Day 26 - NATO Phonetic Alphabet**
   Added error handling using `try`, `except`, and `else` to handle invalid characters.

2. 🔐 **Improved Day 29 - Password Manager**
   Upgraded the Password Manager to use **JSON** for storing data and added exception handling for missing or invalid data files.

3. ⚠️ **Exception Handling Practice**
   Practiced `try`, `except`, `else`, `finally`, and manually raising exceptions with `raise`.

---

# 📡 Day 026 Improved Version - NATO Phonetic Alphabet

The Day 26 NATO Phonetic Alphabet project was improved by adding **exception handling**.

The program reads the NATO alphabet from:

```text
nato_phonetic_alphabet.csv
```

and creates a dictionary containing each letter and its corresponding phonetic code.

```python
phonetic_dict = {
    row.letter: row.code
    for (index, row) in data.iterrows()
}
```

---

## ⚠️ Handling Invalid Characters

The program uses `try` and `except` when converting the user's word:

```python
try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
```

If the user enters a character that does not exist as a key in the dictionary, a `KeyError` occurs.

Instead of allowing the program to crash, the error is caught and a helpful message is displayed.

---

## 🔄 Recursive Retry

After an invalid input, the function calls itself again:

```python
generate_phonetic()
```

This allows the user to enter another word.

The program uses `else` when no exception occurs:

```python
else:
    print(output_list)
```

---

# 🔐 Day 029 Improved Version - Password Manager

The Password Manager from Day 29 was improved by replacing the plain text storage approach with **JSON-based data storage**.

The project now contains:

```text
password_data.json
```

instead of relying only on:

```text
password_data.txt
```

---

## 📄 JSON Data Structure

Saved credentials are organized using website names as dictionary keys:

```python
new_data = {
    website.title(): {
        "email/username": email,
        "password": password,
    }
}
```

This makes it possible to search for credentials using the website name.

---

# 💾 Saving Data With JSON

The program first attempts to read existing data:

```python
try:
    with open(
        file="./Day-030/Day-029 Improved Version/password_data.json",
        mode="r"
    ) as data_file:
        data = json.load(data_file)
```

If the file does not exist, `FileNotFoundError` is handled:

```python
except FileNotFoundError:
    with open(
        file="./Day-030/Day-029 Improved Version/password_data.json",
        mode="w"
    ) as data_file:
        json.dump(new_data, data_file, indent=4)
```

If the JSON file cannot be decoded, `JSONDecodeError` is handled:

```python
except json.JSONDecodeError:
    ...
```

This allows the program to create valid JSON data instead of crashing.

---

## 🔄 Updating Existing Data

If the JSON file already contains valid data, the new website information is added using:

```python
data.update(new_data)
```

The updated dictionary is then written back to the JSON file:

```python
json.dump(data, data_file, indent=4)
```

---

# 🔍 Search Function

The improved Password Manager also introduces a search feature.

The user enters a website and clicks **Search**.

The program loads the JSON data:

```python
with open(
    file="./Day-030/Day-029 Improved Version/password_data.json",
    mode="r"
) as data_file:
    data = json.load(data_file)
```

The saved username and password are then retrieved:

```python
email = data[website]["email/username"]
password = data[website]["password"]
```

---

## ⚠️ Search Error Handling

The search function handles two possible errors.

### File Not Found

```python
except FileNotFoundError:
    messagebox.showinfo(
        title="Error",
        message="No Data File Found."
    )
```

### Website Not Found

```python
except KeyError:
    messagebox.showinfo(
        title="Error",
        message="No Such Data in Database."
    )
```

This prevents the program from crashing when the requested website does not exist.

---

# 🧪 Exception Handling Practice

Day 30 also includes a separate example demonstrating the basic structure of Python exception handling.

The commented practice code demonstrates:

```python
try:
    ...
except FileNotFoundError:
    ...
except KeyError as error_msg:
    ...
else:
    ...
finally:
    ...
```

---

## 🔹 `try`

The `try` block contains code that might produce an exception.

```python
try:
    file = open(file="./Day-030/data.txt")
```

---

## 🔹 `except`

The `except` block handles a specific error.

For example:

```python
except FileNotFoundError:
```

can handle a situation where the requested file does not exist.

Another example:

```python
except KeyError as error_msg:
```

handles an attempt to access a dictionary key that does not exist.

---

## 🔹 `else`

The `else` block runs when no exception occurs:

```python
else:
    content = file.read()
    print(content)
```

---

## 🔹 `finally`

The `finally` block runs regardless of whether an exception occurred:

```python
finally:
    file.close()
    print("File was Closed.")
```

This can be useful for performing cleanup operations.

---

# ⚠️ Raising an Exception Manually

The final Day 30 program demonstrates how to intentionally raise an exception when an invalid value is detected.

The program takes height and weight:

```python
height = float(input("Enter Your Height: "))
weight = float(input("Enter Your Weight: "))
```

It then checks whether the entered height is greater than 3 meters:

```python
if height > 3:
    raise ValueError(
        "The human height cannot be greater than 3 meters"
    )
```

Instead of allowing an invalid value to continue through the calculation, a `ValueError` is manually raised.

---

# 🧮 BMI Calculation

After validating the height, BMI is calculated using:

```python
bmi = weight / height ** 2
```

The calculated BMI is then printed:

```python
print(bmi)
```

The project demonstrates how validation and exceptions can be used before performing a calculation.

---

# 🧠 Code Concepts Used

## ⚠️ Exception Handling

* `try`
* `except`
* `else`
* `finally`
* `raise`
* `FileNotFoundError`
* `KeyError`
* `JSONDecodeError`
* `ValueError`

## 📄 File Handling

* Opening files
* Reading files
* Writing files
* File modes
* Handling missing files
* Closing files

## 🗃️ JSON

* `json.load()`
* `json.dump()`
* JSON dictionaries
* Updating JSON data
* Handling invalid JSON

## 🔐 Password Manager

* GUI with Tkinter
* Password generation
* JSON-based storage
* Searching saved credentials
* Message boxes
* Input validation

## 📡 NATO Phonetic Alphabet

* Pandas
* CSV files
* Dictionary comprehension
* List comprehension
* `KeyError` handling
* Recursive function calls

## 🧮 Python

* Functions
* Dictionaries
* Lists
* Conditional statements
* User input
* Type conversion
* `raise ValueError`

---

# 📂 Project Structure

```text
Day-030/
│
├── Day-026 Improved Version/
│   ├── main.py
│   └── nato_phonetic_alphabet.csv
│
├── Day-029 Improved Version/
│   ├── logo.png
│   ├── main.py
│   ├── password_data.json
│   └── password_data.txt
│
├── data.txt
├── main.py
└── README.md
```

---

# 📄 File Description

| File / Folder                | Purpose                                     |
| ---------------------------- | ------------------------------------------- |
| `Day-026 Improved Version/`  | Improved NATO Phonetic Alphabet project     |
| `Day-029 Improved Version/`  | Improved Password Manager using JSON        |
| `data.txt`                   | File used for exception-handling practice   |
| `main.py`                    | Day 30 exception and BMI practice           |
| `nato_phonetic_alphabet.csv` | NATO alphabet data                          |
| `password_data.json`         | Stores Password Manager data in JSON format |
| `password_data.txt`          | Earlier Password Manager data file          |
| `logo.png`                   | Password Manager logo                       |
| `README.md`                  | Project documentation                       |

---

# 🔄 Exception Handling Flow

```text
                Try Code
                    ↓
             Exception Occurs?
               ↙         ↘
             Yes          No
              ↓            ↓
           except        else
              ↓            ↓
          Handle Error   Continue
               ↘         ↙
                 finally
                    ↓
              Cleanup Code
```

---

# 🛠️ Technologies Used

* **Python**
* **Tkinter**
* **Pandas**
* **JSON**
* **CSV**
* **File Handling**
* **Exception Handling**

---

# 🎯 Learning Outcome

Through Day 30, I learned how to make Python programs more **robust and reliable** by handling unexpected situations.

Key concepts practiced:

* Understanding Python exceptions
* Handling specific exceptions with `except`
* Using `else` when no exception occurs
* Using `finally` for cleanup
* Raising exceptions manually with `raise`
* Handling missing files
* Handling missing dictionary keys
* Handling invalid JSON
* Storing structured data using JSON
* Searching JSON data
* Improving previous projects with error handling

---

# 🚀 Future Improvements

Possible improvements include:

* Add more input validation to the Password Manager
* Handle invalid numeric input using `ValueError`
* Replace recursive retry logic with a loop in the NATO project
* Add JSON data backup functionality
* Improve password storage security
* Add better error messages for invalid inputs
* Add exception handling around all user-input operations

> **Security Note:** The Password Manager is a learning project. Passwords are currently stored in JSON as plain text and should not be considered secure for real-world password management.

---

# ✅ Project Status

**Completed ✔️**

### 📡 Improved NATO Phonetic Alphabet

* [x] Read NATO alphabet using Pandas
* [x] Create phonetic dictionary
* [x] Accept user input
* [x] Handle invalid characters
* [x] Use `try/except/else`
* [x] Retry after invalid input

### 🔐 Improved Password Manager

* [x] Generate passwords
* [x] Save credentials using JSON
* [x] Load existing JSON data
* [x] Update existing data
* [x] Handle missing JSON files
* [x] Handle invalid JSON
* [x] Search saved credentials
* [x] Handle missing website entries

### ⚠️ Exception Handling Practice

* [x] Practice `try`
* [x] Practice `except`
* [x] Practice `else`
* [x] Practice `finally`
* [x] Practice `raise`
* [x] Raise `ValueError` for invalid height
* [x] Calculate BMI

---

# 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
