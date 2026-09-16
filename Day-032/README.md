# 🎂 Day 032 - Birthday Wisher & Email Automation

## 📌 Project Overview

Day 32 focuses on **SMTP, Datetime, Pandas, Randomization, and Email Automation** in Python.

This day contains two practical projects:

1. 🎂 **Birthday Wisher** — Automatically sends a personalized birthday email when a person's birthday matches the current date.
2. 💌 **SMTP & Datetime Library Practice** — Sends a randomly selected motivational quote through email on a specific weekday.

These projects demonstrate how Python can interact with **email servers, dates, CSV files, text files, and automated conditions**.

---

# 🎂 Birthday Wisher

## 📌 Project Overview

The Birthday Wisher program checks a CSV file containing people's birthdays and automatically sends a **personalized Happy Birthday email** if someone's birthday matches today's date.

A random letter template is selected from three available templates, and the person's name is inserted into the letter.

---

## 📂 Birthday Data

The program reads birthday information from:

```text
birthdays.csv
```

The data is loaded using Pandas:

```python
df = pd.read_csv(
    "./Day-032/Birthday Wisher/birthdays.csv"
)
```

The birthday data is then converted into a dictionary:

```python
birthday_dict = {
    (data["month"], data["day"]): data
    for (index, data) in df.iterrows()
}
```

The dictionary uses:

```text
(month, day)
```

as the key.

---

# 📅 Getting Today's Date

The `datetime` module is used to get the current date:

```python
now = dt.datetime.now()
```

The current month and day are extracted:

```python
today_tuple = (now.month, now.day)
```

The program then checks whether today's date exists in the birthday dictionary:

```python
if today_tuple in birthday_dict:
```

If a birthday matches, the email process begins.

---

# ✉️ Random Birthday Letter

The project contains three letter templates:

```text
letter_1.txt
letter_2.txt
letter_3.txt
```

A random template is selected:

```python
file_path = f"./Day-032/Birthday Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
```

This means the birthday email can have a different message each time.

---

# 👤 Personalizing the Letter

The selected letter is read:

```python
with open(file_path) as letter:
    content = letter.read()
```

The person's information is retrieved from the birthday dictionary:

```python
birthday_person = birthday_dict[today_tuple]
```

The placeholder:

```text
[NAME]
```

is replaced with the person's actual name:

```python
content = content.replace(
    "[NAME]",
    birthday_person["name"]
)
```

This creates a personalized birthday message.

---

# 📧 Sending Email With SMTP

The project uses Python's `smtplib` module to connect to Gmail's SMTP server:

```python
with smtplib.SMTP("smtp.gmail.com") as connection:
```

The connection is secured using TLS:

```python
connection.starttls()
```

The program then logs into the email account and sends the message.

The email subject is:

```text
Happy Birthday :)
```

The personalized letter is included in the email body.

---

# 🔄 Birthday Wisher Flow

```text
Start Program
      ↓
Get Current Date
      ↓
Read birthdays.csv
      ↓
Create Birthday Dictionary
      ↓
Check Today's Month & Day
      ↓
Birthday Found?
    ↙       ↘
  No         Yes
  ↓           ↓
End       Select Random Letter
              ↓
        Read Letter Template
              ↓
          Replace [NAME]
              ↓
          Connect to SMTP
              ↓
          Send Birthday Email
              ↓
             End
```

---

# 💌 SMTP & Datetime Library Practice

The second part of Day 32 is a practice project using **SMTP, Datetime, Random, and file handling**.

The program sends a motivational quote by email when the current weekday matches the condition in the program.

---

## 📅 Checking the Weekday

The current date and time are obtained using:

```python
now = dt.datetime.now()
```

The weekday is then retrieved:

```python
weekday = now.weekday()
```

Python represents weekdays as:

```text
Monday    → 0
Tuesday   → 1
Wednesday → 2
Thursday  → 3
Friday    → 4
Saturday  → 5
Sunday    → 6
```

The program checks:

```python
if weekday == 2:
```

So, according to the current implementation, the email is sent when the weekday value is `2`.

---

# 💬 Reading Motivational Quotes

The quotes are stored in:

```text
quotes.txt
```

The file is opened and all quotes are read:

```python
with open(
    "./Day-032/SMTP and Datetime Lib Practice/quotes.txt"
) as quote_file:
    all_quotes = quote_file.readlines()
```

A random quote is selected:

```python
quote = random.choice(all_quotes)
```

---

# 📧 Sending the Quote

The selected quote is sent using Gmail's SMTP server:

```python
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(
        user=my_email,
        password=password
    )
```

The email is then sent using:

```python
connection.sendmail(
    from_addr=my_email,
    to_addrs="...",
    msg=f"Subject:Monday Motivation\n\n{quote}"
)
```

---

# 🔄 Motivation Email Flow

```text
Start Program
      ↓
Get Current Date
      ↓
Find Weekday
      ↓
Check Weekday Condition
      ↓
Condition Matched?
    ↙       ↘
  No         Yes
  ↓           ↓
 End      Read quotes.txt
              ↓
        Select Random Quote
              ↓
          Connect to SMTP
              ↓
          Send Email
              ↓
             End
```

---

# 🧪 SMTP Practice

Before creating the complete automation projects, I practiced sending a basic email using SMTP.

The basic process is:

```python
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(
        user=my_email,
        password=password
    )
    connection.sendmail(
        from_addr=my_email,
        to_addrs="...",
        msg="Subject: Test Mail\n\nHELLO :)"
    )
```

This helped demonstrate the basic steps required to send an email from Python.

---

# 🕒 Datetime Practice

The project also includes basic `datetime` operations:

```python
now = dt.datetime.now()

print(now)
print(now.year)
print(now.weekday())
```

This demonstrates how to access:

* Current date and time
* Current year
* Current weekday

---

# 🧠 Code Concepts Used

## 📅 Datetime

* `datetime`
* `datetime.now()`
* `.year`
* `.month`
* `.day`
* `.weekday()`

## 📧 SMTP

* `smtplib`
* `SMTP()`
* `starttls()`
* `login()`
* `sendmail()`

## 🐼 Pandas

* `pd.read_csv()`
* DataFrames
* `iterrows()`
* Creating dictionaries from DataFrame rows

## 🎲 Random

* `random.randint()`
* `random.choice()`

## 📄 File Handling

* `open()`
* `read()`
* `readlines()`
* `with open()`

## 🔤 String Manipulation

* `.replace()`
* f-strings
* Email subject/body formatting

## 🔀 Conditional Logic

* `if`
* Checking dates
* Checking weekdays
* Triggering automated actions

---

# 📂 Project Structure

```text
Day-032/
│
├── Birthday Wisher/
│   ├── birthdays.csv
│   ├── main.py
│   │
│   └── letter_templates/
│       ├── letter_1.txt
│       ├── letter_2.txt
│       └── letter_3.txt
│
├── SMTP and Datetime Lib Practice/
│   ├── main.py
│   └── quotes.txt
│
└── README.md
```

---

# 📄 File Description

| File / Folder                            | Purpose                                         |
| ---------------------------------------- | ----------------------------------------------- |
| `Birthday Wisher/main.py`                | Checks birthdays and sends personalized emails  |
| `birthdays.csv`                          | Stores birthday information                     |
| `letter_templates/`                      | Contains different birthday letter templates    |
| `letter_1.txt`                           | Birthday message template 1                     |
| `letter_2.txt`                           | Birthday message template 2                     |
| `letter_3.txt`                           | Birthday message template 3                     |
| `SMTP and Datetime Lib Practice/main.py` | SMTP, datetime, and motivational quote practice |
| `quotes.txt`                             | Contains motivational quotes                    |
| `README.md`                              | Project documentation                           |

---

# 🛠️ Technologies Used

* **Python**
* **Pandas**
* **SMTP / smtplib**
* **Datetime**
* **Random**
* **CSV**
* **File Handling**

---

# 🎯 Learning Outcome

Through Day 32, I learned how Python can interact with **email services and date/time information** to automate tasks.

Key concepts practiced:

* Sending emails using SMTP
* Establishing secure SMTP connections using TLS
* Authenticating with an email account
* Reading CSV files using Pandas
* Creating dictionaries from DataFrame data
* Working with dates and weekdays
* Selecting random values
* Reading text files
* Replacing placeholders in templates
* Automating actions based on dates
* Combining multiple Python modules in one project

---

# 🚀 Future Improvements

Possible improvements for the Birthday Wisher:

* Run the program automatically every day
* Add more birthday letter templates
* Support birthdays with full dates
* Add HTML-formatted birthday emails
* Add email logging
* Handle SMTP connection errors
* Move email credentials to environment variables

Possible improvements for the motivational email project:

* Send quotes on a chosen day
* Allow multiple recipients
* Add HTML formatting
* Select quotes based on categories
* Schedule the script to run automatically

---

# 🔐 Security Note

Email passwords or SMTP credentials should **never be hard-coded or committed to GitHub**.

For a real project, credentials should be stored using environment variables or another secure secrets-management method.

If an actual email app password has already been exposed in code or committed to a repository, it should be **revoked/rotated** before publishing the repository.

---

# ✅ Project Status

**Completed ✔️**

### 🎂 Birthday Wisher

* [x] Read birthday data from CSV
* [x] Get current date
* [x] Create birthday dictionary
* [x] Check today's birthday
* [x] Select random letter template
* [x] Replace `[NAME]`
* [x] Connect to Gmail SMTP
* [x] Send personalized birthday email

### 💌 SMTP & Datetime Practice

* [x] Practice SMTP connection
* [x] Use TLS
* [x] Authenticate with SMTP
* [x] Send an email
* [x] Work with datetime
* [x] Determine weekday
* [x] Read quotes from a text file
* [x] Select a random quote
* [x] Send automated motivational email

---

# 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
