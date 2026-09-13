# 🖥️ Day 027 - Miles to Kilometers Converter

## 📌 Project Overview

Day 27 focuses on building a **Graphical User Interface (GUI)** using Python's built-in **Tkinter** library.

The main project is a simple **Miles to Kilometers Converter**. The user enters a distance in miles, clicks the **Calculate** button, and the application displays the equivalent distance in kilometers.

This day also includes practice with basic Tkinter components such as **Labels, Buttons, and Entry widgets**, along with positioning elements using the `grid()` layout manager.

---

## 🎯 Project Features

* 🖥️ Graphical user interface using Tkinter
* ⌨️ Input field for entering miles
* 🔘 Calculate button
* 🔄 Miles-to-kilometers conversion
* 📊 Dynamic result displayed in the GUI
* 📐 GUI layout using `grid()`
* 📦 Window padding and sizing

---

# 🔢 Miles to Kilometers Converter

## 🧮 Conversion Formula

The program converts miles to kilometers using:

```text
Kilometers = Miles × 1.6
```

The calculation is performed when the user clicks the **Calculate** button.

```python
def calculate():
    txt2.config(text=f"{float(miles.get()) * 1.6}")
```

---

## 🖥️ GUI Layout

The application contains:

```text
┌───────────────────────────────┐
│                               │
│        [ Miles ] Miles        │
│                               │
│        is equal to 0 Km       │
│                               │
│          [ Calculate ]        │
│                               │
└───────────────────────────────┘
```

The result initially displays `0` and is updated after the calculation.

---

# 🧩 Tkinter Components Used

## 🪟 Tkinter Window

The main application window is created using:

```python
window = Tk()
```

The title and minimum size are configured with:

```python
window.title("Miles to KM Converter")
window.minsize(width=400, height=400)
```

Padding is added around the window:

```python
window.config(padx=20, pady=20)
```

---

## ⌨️ Entry Widget

The `Entry` widget allows the user to enter the number of miles:

```python
miles = Entry(width=7)
miles.grid(column=1, row=0)
```

The entered value can be retrieved using:

```python
miles.get()
```

Since the value returned by `get()` is a string, it is converted into a floating-point number:

```python
float(miles.get())
```

---

## 🏷️ Label Widgets

Several labels are used to create the interface:

```python
txt = Label(text="Miles")
txt1 = Label(text="is equal to")
txt2 = Label(text="0")
txt3 = Label(text="Km")
```

The result label is updated dynamically using:

```python
txt2.config(text=...)
```

---

## 🔘 Button Widget

The Calculate button is connected to the `calculate()` function:

```python
button = Button(text="Calculate", command=calculate)
```

When the button is clicked, the function executes and updates the result.

---

# 📐 Grid Layout

Tkinter's `grid()` geometry manager is used to arrange the widgets into rows and columns.

For example:

```python
miles.grid(column=1, row=0)
txt.grid(column=2, row=0)
txt1.grid(column=0, row=1)
txt2.grid(column=1, row=1)
txt3.grid(column=2, row=1)
button.grid(column=1, row=2)
```

This allows the interface to be organized in a simple table-like structure.

---

# 🔄 Program Flow

```text
Start Program
      ↓
Create Tkinter Window
      ↓
Create Labels, Entry & Button
      ↓
User Enters Miles
      ↓
User Clicks Calculate
      ↓
Get Entry Value
      ↓
Convert String → Float
      ↓
Miles × 1.6
      ↓
Update Result Label
      ↓
Display Kilometers
```

---

# 🧪 Example

### Input

```text
Miles: 10
```

### Calculation

```text
10 × 1.6 = 16.0
```

### Output

```text
10 Miles is equal to 16.0 Km
```

---

# 🧠 Additional Tkinter Practice

Before building the converter, I practiced creating a basic GUI with:

* Labels
* Buttons
* Entry widgets
* Button click functions
* Updating label text with `.config()`
* `grid()` positioning
* Multiple buttons using the same function

Example:

```python
def button_clicked():
    my_label.config(text=f"{entry.get()}")
```

This helped build the foundation for the Miles to Kilometers Converter.

---

# 🧠 Code Concepts Used

## Tkinter

* `Tk()`
* `Label`
* `Button`
* `Entry`
* `mainloop()`

## GUI Layout

* `grid()`
* Rows and columns
* Window padding
* Window sizing

## Functions

* Defining functions
* Using functions as button commands
* Updating GUI elements from functions

## Data Conversion

* Getting text from an Entry widget
* Converting string input using `float()`
* Performing arithmetic calculations

## Dynamic GUI Updates

The result label is modified using:

```python
txt2.config(text=...)
```

---

# 📂 Project Structure

```text
Day-027/
│
├── main.py
└── README.md
```

### File Description

| File        | Purpose                                            |
| ----------- | -------------------------------------------------- |
| `main.py`   | Contains the Tkinter Miles to Kilometers Converter |
| `README.md` | Project documentation                              |

---

# 🛠️ Technologies Used

* **Python**
* **Tkinter**
* **GUI Programming**

---

# 🎯 Learning Outcome

Through Day 27, I learned the fundamentals of creating **Graphical User Interfaces in Python using Tkinter**.

Key concepts practiced:

* Creating a GUI window
* Adding widgets
* Taking user input
* Handling button clicks
* Connecting buttons to functions
* Updating widgets dynamically
* Using the `grid()` layout manager
* Converting user input into numeric values
* Building a simple interactive application

---

# 🚀 Future Improvements

Possible improvements include:

* Handle empty or invalid input
* Round the result to two decimal places
* Add conversions for kilometers to miles
* Improve the GUI design
* Add more unit conversion options
* Add keyboard support for triggering the calculation

---

# ✅ Project Status

**Completed ✔️**

* [x] Create Tkinter window
* [x] Add Miles input field
* [x] Add labels
* [x] Add Calculate button
* [x] Read user input
* [x] Convert miles to kilometers
* [x] Update result dynamically
* [x] Practice Tkinter GUI components

---

# 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
