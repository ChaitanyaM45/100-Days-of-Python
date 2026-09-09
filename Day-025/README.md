# 🐼 Day 025 - Pandas & U.S. States Game

## 📌 Project Overview

Day 25 focuses on learning **Pandas** for working with tabular data and applying it to a practical **U.S. States Game**.

This day contains two main parts:

1. 🐼 **Pandas Tutorial** — Reading, analyzing, filtering, creating, and exporting CSV data.
2. 🇺🇸 **U.S. States Game** — A Turtle-based interactive game that uses Pandas to read state data and display correctly guessed states on a U.S. map.

---

# 🐼 Pandas Tutorial

The `Pandas Tutorial` folder contains examples of working with CSV files using Pandas.

### 📂 Data Files

```text
Pandas Tutorial/
├── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
├── pandas_tutorial.py
├── squirrel_count.csv
├── student.csv
└── weather_data.csv
```

---

## 📊 Reading CSV Data

Pandas can load a CSV file into a DataFrame using:

```python
import pandas as pd

df = pd.read_csv("weather_data.csv")
```

A **DataFrame** provides a convenient way to work with rows and columns of data.

---

## 🌦️ Weather Data Analysis

The tutorial includes working with `weather_data.csv`.

Examples practiced include:

### Finding the average temperature

```python
df["temp"].mean()
```

### Finding the maximum temperature

```python
df["temp"].max()
```

### Filtering a specific day

```python
df[df["day"] == "Monday"]
```

### Finding the row with the maximum temperature

```python
df[df["temp"] == max]
```

### Accessing a specific column

```python
monday.condition
```

---

## 🌡️ Celsius to Fahrenheit Conversion

The tutorial also demonstrates converting Monday's temperature from Celsius to Fahrenheit:

```python
monday_temp_in_F = (monday.temp[0] * 9 / 5) + 32
```

---

## 📝 Creating a DataFrame From Scratch

A DataFrame can also be created using a Python dictionary:

```python
data_dict = {
    "student": ["rohit", "pranav", "chaitanya"],
    "score": [95, 98, 80]
}

data_frame = pd.DataFrame(data_dict)
```

The DataFrame can then be exported to CSV:

```python
data_frame.to_csv("student.csv")
```

---

# 🐿️ Squirrel Census Analysis

The project also analyzes the **2018 Central Park Squirrel Census** dataset.

The data is filtered according to the squirrel's `Primary Fur Color`.

### Gray Squirrels

```python
grey_squirell = df[df["Primary Fur Color"] == "Gray"]
```

### Cinnamon Squirrels

```python
cinnamon_squirell = df[df["Primary Fur Color"] == "Cinnamon"]
```

### Black Squirrels

```python
black_squirell = df[df["Primary Fur Color"] == "Black"]
```

The number of squirrels in each category is calculated using `len()`.

A new DataFrame is then created:

```python
new_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [
        len(grey_squirell),
        len(cinnamon_squirell),
        len(black_squirell)
    ]
}
```

Finally, the results are exported to:

```text
squirrel_count.csv
```

---

# 🇺🇸 U.S. States Game

## 🎮 Project Overview

The **U.S. States Game** is an interactive Turtle game where the player tries to guess all **50 U.S. states**.

The game combines:

* `turtle` for the graphical interface
* `pandas` for reading state data
* A CSV file containing state names and coordinates

The state coordinates from the CSV file are used to place the correctly guessed state name on the map.

---

## 🗺️ How It Works

1. A blank map of the United States is displayed.
2. The player enters a state name.
3. Pandas checks whether the entered state exists in the dataset.
4. If the answer is correct:

   * The state's `x` and `y` coordinates are retrieved.
   * A Turtle object is positioned at those coordinates.
   * The state name is written on the map.
5. The score increases.
6. The game continues until all 50 states are guessed or the player chooses to stop.

---

## 📊 Reading State Data

The game loads the CSV file using Pandas:

```python
df = pd.read_csv("./Day-025/us-states-game/50_states.csv")
```

The state names are converted into a Python list:

```python
all_state = df.state.to_list()
```

This list is then used to check whether the player's answer is a valid state.

---

## ✍️ Displaying a Correct Answer

When the player enters a valid state, the corresponding row is selected:

```python
state = df[df["state"] == answer_state]
```

The coordinates are then extracted:

```python
X = state.x.iloc[0]
Y = state.y.iloc[0]
```

A Turtle object moves to those coordinates and writes the state name:

```python
t.goto(X, Y)
t.write(
    state.state.iloc[0],
    align="left",
    font=("Arial", 10, "bold")
)
```

---

## 🔢 Score Tracking

The game keeps track of the number of correctly guessed states:

```python
guessed_state = 0
```

After a correct guess:

```python
guessed_state += 1
```

The input prompt displays the current progress:

```python
title=f"{guessed_state}/50 State Correct"
```

---

## 🚫 Preventing Duplicate Guesses

The program maintains a list of already guessed states:

```python
guessed_states = []
```

A state is accepted only when it:

* Exists in `all_state`
* Has not already been guessed

```python
if (answer_state in all_state) and (answer_state not in guessed_states):
```

---

## ⏸️ Continue Option

Every 5 correct guesses, the program asks whether the player wants to continue:

```python
if (guessed_state != 0) and (guessed_state % 5) == 0:
    choice = screen.textinput(
        "Do you want to Continue??",
        prompt="Type Y/N:"
    )
```

This also demonstrates the use of the **modulo operator `%`** to perform an action after every five correct answers.

---

# 📂 Project Structure

```text
Day-025/
│
├── Pandas Tutorial/
│   ├── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
│   ├── pandas_tutorial.py
│   ├── squirrel_count.csv
│   ├── student.csv
│   └── weather_data.csv
│
├── us-states-game/
│   ├── 50_states.csv
│   ├── blank_states_img.gif
│   └── main.py
│
└── README.md
```

---

# 🧠 Code Concepts Used

## Pandas

* Importing Pandas
* `pd.read_csv()`
* DataFrames
* Series
* Filtering DataFrames
* Selecting rows
* Selecting columns
* `.mean()`
* `.max()`
* `.to_list()`
* `.iloc[]`
* `pd.DataFrame()`
* `.to_csv()`

## File & CSV Data

* Reading CSV files
* Working with structured tabular data
* Creating CSV files
* Exporting processed data

## Python

* Lists
* Dictionaries
* Loops
* Conditional statements
* String methods
* `len()`
* Modulo operator `%`

## Turtle Graphics

* Creating a Turtle screen
* Loading a GIF image as a Turtle shape
* Creating Turtle objects
* Positioning objects with coordinates
* Writing text on the screen
* Taking user input with `textinput()`

---

# 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Turtle Graphics**
* **CSV**
* **DataFrames**

---

# 🎯 Learning Outcome

Through Day 25, I learned how to use **Pandas to work with structured data and CSV files**.

Key concepts practiced:

* Reading CSV datasets with Pandas
* Exploring and filtering DataFrames
* Performing calculations on columns
* Creating new DataFrames
* Exporting DataFrames to CSV
* Working with real-world datasets
* Combining Pandas with Turtle graphics
* Using coordinate data to create an interactive map-based game

---

# 🚀 Future Improvements

Possible improvements for the U.S. States Game:

* Add a separate `game_over` screen when all 50 states are guessed
* Save incorrectly guessed/missing states to a CSV file
* Add a final score summary
* Accept more variations of state names
* Add a timer
* Add difficulty levels
* Improve the continue/exit flow

---

# ✅ Project Status

**Completed ✔️**

### 🐼 Pandas Tutorial

* [x] Read CSV files
* [x] Work with DataFrames
* [x] Filter data
* [x] Calculate statistics
* [x] Create DataFrames
* [x] Export data to CSV
* [x] Analyze squirrel census data

### 🇺🇸 U.S. States Game

* [x] Display U.S. map
* [x] Read state data using Pandas
* [x] Accept user guesses
* [x] Check valid states
* [x] Prevent duplicate guesses
* [x] Place state names using coordinates
* [x] Track correct guesses
* [x] Continue/stop functionality

---

# 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
