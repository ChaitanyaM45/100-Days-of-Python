# 🌍 Day 033 - APIs, ISS Overhead Notifier & Kanye Quotes

## 📌 Project Overview

Day 33 focuses on working with **APIs, HTTP requests, JSON data, and Python automation**.

This day contains three projects:

1. 🛰️ **ISS Overhead Notifier** — Checks whether the International Space Station (ISS) is near a configured location and whether it is nighttime. If both conditions are met, it sends an email notification.
2. 💬 **Kanye Quotes App** — A Tkinter GUI application that fetches random Kanye West quotes from an API and displays them on the screen.
3. 🌅 **API Basics Practice** — Practices making API requests, checking response status codes, extracting JSON data, and passing parameters to an API.

---

# 🛰️ Project 1: ISS Overhead Notifier

## 📌 Project Overview

The ISS Overhead Notifier checks whether the International Space Station is close to a configured geographical location.

The program also checks whether it is nighttime at that location. When both conditions are satisfied, it sends an email notification informing the recipient that the ISS is overhead.

The program continuously checks these conditions every 60 seconds.

## 🎯 Features

* Fetches the current ISS location using an API
* Extracts ISS latitude and longitude
* Checks whether the ISS is within a configured range
* Retrieves sunrise and sunset information
* Determines whether it is nighttime
* Sends an email using Gmail SMTP
* Repeats the checks every 60 seconds

## 🌐 Fetching ISS Location

The program uses the Open Notify API to retrieve the current ISS position.

```python
response = requests.get(
    url="http://api.open-notify.org/iss-now.json"
)

response.raise_for_status()
data = response.json()
```

The ISS coordinates are extracted from the response:

```python
iss_latitude = float(
    data["iss_position"]["latitude"]
)

iss_longitude = float(
    data["iss_position"]["longitude"]
)
```

The API response provides the ISS's current latitude and longitude.

## 📍 Checking Whether the ISS Is Overhead

The program defines a target location using latitude and longitude:

```python
MY_LAT = 21.6796
MY_LONG = 92.0266
```

The `is_iss_overhead()` function checks whether the ISS coordinates fall within 5 degrees of the configured latitude and longitude.

```python
if (
    MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
    and
    MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
):
    return True
```

If both coordinate checks pass, the function returns `True`.

**Note:** This is a rectangular latitude/longitude range check, not an exact distance calculation.

## 🌅 Checking Whether It Is Nighttime

The program uses the Sunrise-Sunset API to obtain sunrise and sunset information.

```python
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
```

The parameters are passed to the API using `requests.get()`.

The program extracts the sunrise and sunset hours and compares them with the current local hour:

```python
time_now = datetime.now().hour

if time_now >= sunset or time_now <= sunrise:
    return True
```

If the current hour is after sunset or before sunrise, the function returns `True`.

## 📧 Sending the ISS Notification

The program continuously checks whether the ISS is overhead and whether it is nighttime.

```python
while True:
    time.sleep(60)

    if is_iss_overhead() and is_night():
        # Send email notification
```

When both functions return `True`, the program connects to Gmail's SMTP server.

```python
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(
        user=email,
        password=password
    )
```

The email informs the recipient:

```text
Subject: Look Up👍

The ISS is above you in the sky.
```

## 🔄 ISS Notifier Workflow

```text
Start Program
      ↓
Wait 60 Seconds
      ↓
Fetch ISS Location
      ↓
Check Whether ISS Is Within
Configured Latitude/Longitude Range
      ↓
Check Sunrise and Sunset
      ↓
Is It Nighttime?
      ↓
Both Conditions True?
   ↙          ↘
  No           Yes
  ↓             ↓
Repeat       Send Email
                ↓
             Repeat
```

---

# 💬 Project 2: Kanye Quotes App

## 📌 Project Overview

The Kanye Quotes App is a graphical application built using **Tkinter**.

It fetches a random quote from the Kanye REST API and displays the quote inside a graphical interface.

The user can click the Kanye button to retrieve and display another quote.

## 🎯 Features

* Tkinter graphical user interface
* Fetches quotes from an external API
* Displays quotes on a Canvas
* Button-based interaction
* Updates the displayed quote dynamically
* Uses an image-based interface

## 🌐 Fetching a Quote

The application sends a GET request to the Kanye REST API:

```python
def get_quote():
    responce = requests.get(
        url="https://api.kanye.rest"
    )

    quote = responce.json()["quote"]
```

The response is converted into JSON, and the quote is extracted using the `"quote"` key.

## 🖥️ Updating the GUI

The quote is displayed using a Tkinter Canvas text item:

```python
canvas.itemconfig(
    quote_text,
    text=quote
)
```

Whenever the button is clicked, the `get_quote()` function fetches a new quote and updates the text on the screen.

## 🖼️ User Interface

The application uses:

* `Tk()` to create the main window
* `Canvas` to display the background and quote
* `PhotoImage` to load images
* `Button` to trigger the API request
* `mainloop()` to run the GUI

The background image and Kanye button image are loaded from the project folder.

## 🔄 Kanye Quotes Workflow

```text
Start Application
      ↓
Display Tkinter Window
      ↓
User Clicks Kanye Button
      ↓
Send GET Request to API
      ↓
Receive JSON Response
      ↓
Extract Quote
      ↓
Update Canvas Text
      ↓
Display New Quote
```

---

# 🌅 Project 3: API Basics Practice

## 📌 Project Overview

This project practices the fundamentals of working with APIs using Python's `requests` library.

It demonstrates how to:

* Send GET requests
* Check HTTP status codes
* Handle unsuccessful requests
* Convert responses into JSON
* Extract nested values
* Pass parameters to an API

## 🌐 Making an API Request

The program sends a GET request to the Open Notify API:

```python
response = requests.get(
    url="http://api.open-notify.org/iss-now.json"
)
```

The response status code is printed:

```python
print(response.status_code)
```

A successful HTTP response commonly uses status code `200`.

## ❌ Testing an Invalid URL

The code also makes a request to an invalid endpoint:

```python
response1 = requests.get(
    url="http://api.open-notify.org/is-now.json"
)
```

The program prints the returned status code to demonstrate how an unsuccessful request can be identified.

The code then calls:

```python
response1.raise_for_status()
```

This raises an exception when the response indicates an HTTP error.

## 📦 Working With JSON

The response is converted into a Python dictionary:

```python
data = response.json()
```

The ISS position is extracted:

```python
latitude = data["iss_position"]["latitude"]

longitude = data["iss_position"]["longitude"]
```

The coordinates are then stored in a tuple:

```python
iss_position = (latitude, longitude)
```

This demonstrates how to access nested JSON values.

## 🌞 Passing Parameters to an API

The program defines parameters for the Sunrise-Sunset API:

```python
MY_LAT = 18.522892
MY_LONG = 73.859622

DATE = "2026-09-17"

parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "date": DATE,
}
```

The parameters are passed with the request:

```python
response2 = requests.get(
    url="https://api.sunrise-sunset.org/v2",
    params=parameter
)
```

The code then attempts to print the sunrise and sunset values from the response.

---

# 🧠 Code Concepts Used

## 🌐 API & HTTP Requests

* `requests.get()`
* GET requests
* API endpoints
* Query parameters
* HTTP response status codes
* `raise_for_status()`

## 📦 JSON Handling

* `response.json()`
* Dictionaries
* Nested dictionary access
* Extracting API response values

## 🛰️ ISS Location

* Latitude and longitude
* Coordinate range comparisons
* Conditional logic
* Boolean return values

## 📅 Datetime

* `datetime.now()`
* `.hour`
* Comparing current time with sunrise and sunset hours

## 📧 Email Automation

* `smtplib`
* Gmail SMTP
* `starttls()`
* `login()`
* `sendmail()`

## 🖥️ Tkinter

* `Tk()`
* `Canvas`
* `Button`
* `PhotoImage`
* `.itemconfig()`
* `mainloop()`

## ⏱️ Automation

* `while` loops
* `time.sleep()`
* Repeated API requests
* Conditional notifications

## 🐍 Python Fundamentals

* Functions
* Variables
* Dictionaries
* Tuples
* Imports
* Type conversion
* `if` statements
* `and` and `or` operators

---

# 📂 Project Structure

```text
Day-033/
│
├── ISS Overhead/
│   ├── config.py
│   └── main.py
│
├── Kayne Quotes/
│   ├── background.png
│   ├── kanye.png
│   └── main.py
│
├── API_Basics.py
└── README.md
```

## 📄 File Description

| File / Folder                 | Purpose                                                           |
| ----------------------------- | ----------------------------------------------------------------- |
| `ISS Overhead/main.py`        | Checks ISS position and nighttime conditions, then sends an email |
| `ISS Overhead/config.py`      | Configuration file for the ISS project                            |
| `Kayne Quotes/main.py`        | Tkinter application that fetches and displays quotes              |
| `Kayne Quotes/background.png` | Background image for the quote application                        |
| `Kayne Quotes/kanye.png`      | Button image used in the quote application                        |
| `API_Basics.py`               | Practices HTTP requests, JSON, status codes, and API parameters   |
| `README.md`                   | Project documentation                                             |

---

# 🛠️ Technologies Used

* **Python**
* **Requests**
* **Tkinter**
* **Datetime**
* **smtplib**
* **Time**
* **JSON**
* **Open Notify API**
* **Sunrise-Sunset API**
* **Kanye REST API**

---

# 🎯 Learning Outcome

Through Day 33, I learned how to interact with external APIs and use the returned data in Python applications.

Key concepts practiced:

* Making HTTP GET requests
* Understanding API endpoints
* Checking HTTP response status codes
* Using `raise_for_status()` for HTTP errors
* Converting API responses into JSON
* Extracting nested JSON data
* Passing query parameters to APIs
* Working with latitude and longitude
* Comparing current time with sunrise and sunset
* Sending automated email notifications
* Building a Tkinter application that uses an API
* Updating Canvas text dynamically
* Repeating checks using loops and delays

---

# 🚀 Future Improvements

## 🛰️ ISS Overhead Notifier

* Calculate the actual distance between the ISS and the target location
* Improve timezone handling for sunrise and sunset
* Add error handling for failed API requests
* Avoid sending repeated notifications during the same overhead pass
* Move email credentials into environment variables
* Use a scheduler or background service for regular execution

## 💬 Kanye Quotes App

* Add API error handling
* Display a loading message while fetching a quote
* Improve the layout for long quotes
* Add a copy-to-clipboard feature
* Add a favorites list
* Improve the application styling

## 🌐 API Basics

* Practice more public APIs
* Handle network errors
* Explore different HTTP status codes
* Work with additional JSON response structures
* Validate API response fields before accessing them

---

# 🔐 Security & Reliability Notes

* Do not hard-code email passwords or SMTP credentials in source code.
* Store credentials in environment variables or another secure configuration method.
* If an actual email app password has been exposed in code or committed to GitHub, revoke and replace it before publishing the repository.
* API requests can fail because of network problems, invalid endpoints, or changes to API responses. Add appropriate exception handling for a more reliable application.
* Confirm the Sunrise-Sunset API's current response structure and timezone behavior when running the ISS project.

---

# ✅ Project Status

**Completed ✔️**

### 🛰️ ISS Overhead Notifier

* [x] Fetch ISS location
* [x] Extract latitude and longitude
* [x] Check configured coordinate range
* [x] Request sunrise and sunset information
* [x] Check nighttime condition
* [x] Connect to Gmail SMTP
* [x] Send email notification
* [x] Repeat checks every 60 seconds

### 💬 Kanye Quotes App

* [x] Create Tkinter window
* [x] Load background and button images
* [x] Fetch quote from API
* [x] Extract quote from JSON
* [x] Update Canvas text
* [x] Add button interaction

### 🌐 API Basics

* [x] Send GET requests
* [x] Print status codes
* [x] Practice invalid endpoint handling
* [x] Use `raise_for_status()`
* [x] Convert response to JSON
* [x] Extract nested JSON values
* [x] Pass parameters to an API

---

# 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
