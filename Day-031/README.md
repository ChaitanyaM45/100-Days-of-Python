# 🃏 Day 031 - Flash Card App

## 📌 Project Overview

Day 31 focuses on building a **Flash Card Language Learning Application** using Python, Tkinter, Pandas, and the Random module.

The application helps users learn **German vocabulary** by displaying a German word first and automatically flipping the card after **3 seconds** to reveal its English meaning.

The user can mark a word as **known** using the right button. Known words are removed from the learning dataset and the updated list is saved to a CSV file.

---

# 🎯 Project Features

* 🃏 Interactive flash cards
* 🇩🇪 Displays German words
* 🇬🇧 Automatically reveals English translations
* ⏱️ 3-second automatic card flip
* 🔀 Random vocabulary selection
* ❌ Wrong button to move to another card
* ✅ Right button to mark a word as known
* 💾 Saves remaining words to `words_to_learn.csv`
* 📊 Uses Pandas for CSV data management
* 🖥️ Tkinter graphical interface

---

# 📚 How It Works

When the application starts, it tries to load the user's existing learning progress:

```python
try:
    df = pd.read_csv(r"./Day-031/data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv(r"./Day-031/data/german_words.csv")
```

If `words_to_learn.csv` does not exist, the original `german_words.csv` file is used.

The DataFrame is then converted into a list of dictionaries:

```python
new_dict = df.to_dict(orient="records")
```

Each dictionary represents one flash card containing:

```text
German → German word
English → English translation
```

---

# 🃏 Flash Card System

The `next_card()` function selects a random card:

```python
current_card = random.choice(new_dict)
```

The German side of the card is then displayed:

```python
canvas.itemconfig(
    card_title,
    text="German",
    fill="black"
)

canvas.itemconfig(
    card_word,
    text=current_card["German"],
    fill="black"
)
```

The front card image is also displayed:

```python
canvas.itemconfig(
    card_bg,
    image=card_front_img
)
```

---

# ⏱️ Automatic Card Flip

After displaying the German word, the program schedules the card to flip after **3 seconds**:

```python
flip_timer = window.after(
    3000,
    func=flip_card
)
```

The `flip_card()` function changes the card to its English side:

```python
canvas.itemconfig(
    card_title,
    text="English",
    fill="white"
)

canvas.itemconfig(
    card_word,
    text=current_card["English"],
    fill="white"
)

canvas.itemconfig(
    card_bg,
    image=card_back_img
)
```

The user therefore gets a short amount of time to remember the German word before seeing its translation.

---

# 🔀 Random Card Selection

Cards are selected randomly using:

```python
current_card = random.choice(new_dict)
```

This means the vocabulary does not necessarily appear in the same order every time.

---

# ❌ Wrong Button

The **Wrong** button is connected to:

```python
command=next_card
```

When the user does not know the word, clicking the button simply moves to another randomly selected flash card.

```python
wrong_button = Button(
    image=wrong_img,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=next_card
)
```

The current word remains in the learning dataset.

---

# ✅ Right Button

The **Right** button calls:

```python
command=is_known
```

This indicates that the user knows the word.

The current card is removed from the vocabulary list:

```python
new_dict.remove(current_card)
```

---

# 💾 Saving Learning Progress

After removing a known word, the remaining cards are converted back into a Pandas DataFrame:

```python
data = pd.DataFrame(new_dict)
```

The remaining vocabulary is then saved to:

```text
./Day-031/data/words_to_learn.csv
```

using:

```python
data.to_csv(
    "./Day-031/data/words_to_learn.csv",
    index=False
)
```

This allows the application to keep track of the words that still need to be learned.

---

# 🔄 Learning Progress Flow

```text
Start Application
       ↓
Load words_to_learn.csv
       ↓
If File Not Found
       ↓
Load german_words.csv
       ↓
Convert DataFrame → List of Dictionaries
       ↓
Select Random German Word
       ↓
Display German Card
       ↓
Wait 3 Seconds
       ↓
Flip Card
       ↓
Display English Translation
       ↓
      User
     ↙     ↘
  ❌ Wrong  ✅ Right
     ↓        ↓
Next Card   Remove Word
              ↓
         Save Remaining Words
              ↓
           Next Card
```

---

# 🖥️ Graphical User Interface

The application is created using **Tkinter**.

The main window uses:

```python
BACKGROUND_COLOR = "#B1DDC6"
```

The window is configured with:

```python
window = Tk()

window.title("Flashy")
window.config(
    padx=50,
    pady=50,
    bg=BACKGROUND_COLOR
)
```

---

# 🖼️ Card Images

Two images are used for the flash card:

### Front

```python
card_front_img = PhotoImage(
    file="./Day-031/images/card_front.png"
)
```

### Back

```python
card_back_img = PhotoImage(
    file="./Day-031/images/card_back.png"
)
```

The front displays the German word, while the back displays the English translation.

---

# 🔘 Buttons

The application has two image-based buttons.

### ❌ Wrong

```text
Wrong → Next Random Card
```

### ✅ Right

```text
Right → Remove Card → Save Progress → Next Card
```

The button images are loaded using `PhotoImage`.

---

# 🧠 Code Concepts Used

## Tkinter

* `Tk()`
* `Canvas`
* `Button`
* `PhotoImage`
* `mainloop()`
* `grid()`
* `.itemconfig()`
* `.after()`
* `.after_cancel()`

## Pandas

* `pd.read_csv()`
* DataFrames
* `.to_dict()`
* `orient="records"`
* `pd.DataFrame()`
* `.to_csv()`

## Random Module

```python
random.choice()
```

Used to randomly select a vocabulary card.

## File Handling

* Reading CSV files
* Handling `FileNotFoundError`
* Saving updated vocabulary data

## Python

* Functions
* Lists
* Dictionaries
* Global variables
* Conditional logic
* Exception handling
* List/data manipulation

---

# 📂 Project Structure

```text
Day-031/
│
├── data/
│   ├── german_words.csv
│   └── words_to_learn.csv
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── wrong.png
│   └── right.png
│
├── main.py
└── README.md
```

### File Description

| File / Folder        | Purpose                                                 |
| -------------------- | ------------------------------------------------------- |
| `main.py`            | Contains the Flash Card application                     |
| `german_words.csv`   | Original German-English vocabulary dataset              |
| `words_to_learn.csv` | Stores vocabulary that has not yet been marked as known |
| `card_front.png`     | Front side of the flash card                            |
| `card_back.png`      | Back side of the flash card                             |
| `wrong.png`          | Wrong-answer button image                               |
| `right.png`          | Correct-answer button image                             |
| `README.md`          | Project documentation                                   |

---

# 🛠️ Technologies Used

* **Python**
* **Tkinter**
* **Pandas**
* **Random Module**
* **CSV**
* **Exception Handling**

---

# 🎯 Learning Outcome

Through Day 31, I learned how to combine **Tkinter GUI programming with Pandas and file handling** to create an interactive learning application.

Key concepts practiced:

* Creating a GUI-based application
* Working with Tkinter Canvas
* Displaying images in Tkinter
* Creating interactive buttons
* Scheduling functions using `after()`
* Cancelling scheduled callbacks
* Reading vocabulary from CSV files
* Converting DataFrames into dictionaries
* Randomly selecting data
* Removing learned items from a dataset
* Saving updated data back to CSV
* Handling `FileNotFoundError`
* Maintaining learning progress between program runs

---

# 🚀 Future Improvements

Possible improvements include:

* Add a progress counter such as `25 / 100 words`
* Add more languages
* Add pronunciation/audio for vocabulary
* Prevent starting multiple countdown timers
* Display a completion message when all cards are learned
* Add a reset-learning-progress option
* Add categories such as verbs, nouns, adjectives, etc.
* Add a pause button for the flash-card timer

---

# ✅ Project Status

**Completed ✔️**

* [x] Create flash card GUI
* [x] Load vocabulary from CSV
* [x] Use Pandas for data management
* [x] Randomly select German words
* [x] Display German side
* [x] Automatically flip after 3 seconds
* [x] Display English translation
* [x] Add Wrong button
* [x] Add Right button
* [x] Remove known words
* [x] Save remaining words to CSV
* [x] Preserve learning progress

---

# 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
