# ✉️ Day 024 - Mail Merge & File Handling

## 📌 Project Overview

Day 24 focuses on **File Handling in Python** and applying it to a practical **Mail Merge project**.

The main project reads a list of names from a text file and a starting letter template from another text file. It then replaces the `[name]` placeholder with each person's name and creates a separate personalized letter for every recipient.

This day also includes an **improved version of the Day 21 Snake Game**, where a **High Score system** was added using file handling.

---

# ✉️ Mail Merge Project

## 📂 How It Works

The program uses three main steps:

1. Read all names from `invited_names.txt`.
2. Read the letter template from `starting_letter.txt`.
3. For every name:

   * Remove extra whitespace using `.strip()`.
   * Replace `[name]` with the actual name.
   * Create a new personalized letter.
   * Save it inside the `Output/ReadyToSend` folder.

The placeholder is defined as:

```python
PLACEHOLDER = "[name]"
```

The replacement is performed using:

```python
new_letter = letter_content.replace(PLACEHOLDER, name)
```

---

## 📝 Input Files

### `invited_names.txt`

Contains the names of all recipients.

Example:

```text
Aang
Appa
Katara
Momo
Sokka
Toph
Uncle Iroh
Zuko
```

### `starting_letter.txt`

Contains the common letter template with the `[name]` placeholder.

The program replaces this placeholder with each name.

---

## 📤 Output

For every name, the program creates a separate text file:

```text
letter_for_Aang.txt
letter_for_Appa.txt
letter_for_Katara.txt
letter_for_Momo.txt
letter_for_Sokka.txt
letter_for_Toph.txt
letter_for_Uncle Iroh.txt
letter_for_Zuko.txt
```

Each generated file contains a personalized version of the starting letter.

---

## 🔄 Mail Merge Flow

```text
invited_names.txt
       ↓
Read Names
       ↓
starting_letter.txt
       ↓
Read Letter Template
       ↓
Replace [name]
       ↓
Create Personalized Letter
       ↓
Save to Output/ReadyToSend
```

---

# 🐍 Day 021 Improved - Snake Game

As part of Day 24's file-handling practice, I also modified my previous **Day 21 Snake Game** to add a persistent **High Score** system.

The improved version stores the high score in:

```text
data.txt
```

Initially, the file contains:

```text
0
```

---

## 🏆 High Score System

When the game starts, the program reads the previous high score from `data.txt`:

```python
with open("data.txt") as data:
    self.high_score = int(data.read())
```

When the player loses or resets the game, the program checks whether the current score is greater than the stored high score.

If it is, the new high score is written back to `data.txt`:

```python
if self.score > self.high_score:
    self.high_score = self.score

    with open("data.txt", mode="w") as data:
        data.write(str(self.high_score))
```

This means the high score can be **saved between different game runs**.

---

## 🐍 Improved Snake Features

The improved version includes:

* Snake movement
* Food generation
* Snake growth
* Score tracking
* Wall collision detection
* Self-collision detection
* Game reset
* High score storage
* High score display
* Persistent data using a text file

The `Scoreboard` now displays:

```text
Score : 5    High Score : 12
```

---

# 🧠 Code Concepts Used

## File Handling

* `open()`
* Reading files with `"r"` / default mode
* Writing files with `"w"`
* `read()`
* `write()`
* `with open(...)`
* File paths

## String Handling

* `.strip()`
* `.replace()`
* f-strings
* String concatenation/interpolation

## Loops

The program loops through every name:

```python
for name in names:
    ...
```

This allows one template to generate multiple personalized letters.

## Working With Lists

The names are loaded into a list:

```python
names = name_file.readlines()
```

Each name is then processed individually.

## Object-Oriented Programming

The improved Snake Game continues to use classes such as:

* `Snake`
* `Food`
* `Scoreboard`

## Persistent Data

The Snake Game demonstrates how information can be stored in a file so that the high score is available the next time the program runs.

---

# 📂 Project Structure

```text
Day-024/
│
├── Day-021(Improved)/
│   ├── data.txt
│   ├── food.py
│   ├── main.py
│   ├── scoreboard.py
│   ├── snake.py
│   └── README.md
│
├── Input/
│   ├── Letters/
│   │   └── Starting_letter.txt
│   │
│   └── Names/
│       └── invited_names.txt
│
├── Output/
│   └── ReadyToSend/
│       ├── letter_for_Aang.txt
│       ├── letter_for_Appa.txt
│       ├── letter_for_Katara.txt
│       ├── letter_for_Momo.txt
│       ├── letter_for_Sokka.txt
│       ├── letter_for_Toph.txt
│       ├── letter_for_Uncle Iroh.txt
│       └── letter_for_Zuko.txt
│
└── main.py
```

---

# 📄 File Description

| File / Folder         | Purpose                                   |
| --------------------- | ----------------------------------------- |
| `main.py`             | Runs the Mail Merge program               |
| `Input/Names/`        | Contains the list of recipient names      |
| `Input/Letters/`      | Contains the starting letter template     |
| `Output/ReadyToSend/` | Stores the generated personalized letters |
| `Day-021(Improved)/`  | Improved version of the Day 21 Snake Game |
| `data.txt`            | Stores the Snake Game high score          |
| `food.py`             | Handles Snake Game food                   |
| `snake.py`            | Handles the snake                         |
| `scoreboard.py`       | Handles score and high score              |
| `README.md`           | Documentation for the improved Snake Game |

---

# 🛠️ Technologies Used

* **Python**
* **File Handling**
* **String Manipulation**
* **Turtle Graphics**
* **Object-Oriented Programming**

---

# 🎯 Learning Outcome

Through this project, I learned how to work with **external text files in Python** and use file data inside a program.

Key concepts learned:

* Opening and closing files
* Reading text files
* Writing to text files
* Processing multiple lines from a file
* Replacing text dynamically
* Generating multiple output files
* Using file handling for persistent data
* Storing and retrieving a high score
* Combining file handling with Object-Oriented Programming

---

# 🚀 Future Improvements

Possible improvements for the Mail Merge project:

* Generate letters in additional formats such as `.docx` or `.pdf`
* Add error handling for missing input files
* Create the output folder automatically if it doesn't exist
* Use relative paths instead of absolute Windows paths
* Add more customizable placeholders such as `[date]`, `[address]`, etc.

---

# ✅ Project Status

**Completed ✔️**

### Mail Merge

* [x] Read names from a file
* [x] Read letter template
* [x] Replace `[name]`
* [x] Generate personalized letters
* [x] Save letters to the output folder

### Improved Snake Game

* [x] Save high score
* [x] Read high score on startup
* [x] Update high score when beaten
* [x] Reset current score
* [x] Display current score and high score

---

# 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
