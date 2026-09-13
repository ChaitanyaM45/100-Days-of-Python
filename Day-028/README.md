# 🍅 Day 028 - Pomodoro Timer

## 📌 Project Overview

Day 28 focuses on building a **Pomodoro Timer** using Python's **Tkinter** library.

The Pomodoro technique divides study/work time into focused work sessions followed by short breaks and longer breaks after several sessions.

This project creates a graphical timer with a **tomato image**, countdown display, **START** and **RESET** buttons, and check marks to track completed sessions.

---

## 🎯 Project Features

* 🍅 Pomodoro-style countdown timer
* 🟢 25-minute work sessions
* 🌸 5-minute short breaks
* 🔴 20-minute long breaks
* ▶️ START button
* 🔄 RESET button
* ⏱️ Live countdown display
* ✔️ Completed-session check marks
* 🎨 Different colors for work and break periods
* 🔁 Automatic transition between work and break sessions

---

# ⏱️ Pomodoro Timer Mechanism

The timer uses the following durations:

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

The number of completed timer sessions is tracked using:

```python
reps = 0
```

Each time the **START** button is pressed, the repetition counter increases:

```python
reps += 1
```

---

## 🔄 Timer Sequence

The timer determines which session should run based on the value of `reps`.

```text
Work → Short Break → Work → Short Break
             ↓
       ... repeated ...
             ↓
       Long Break
```

More specifically:

```text
1 → Work
2 → Short Break
3 → Work
4 → Short Break
5 → Work
6 → Short Break
7 → Work
8 → Long Break
```

After the long break, the cycle starts again.

---

# 🟢 Work Session

For odd-numbered repetitions, the timer starts a **25-minute work session**:

```python
count_down(WORK_MIN * 60)
timer_txt.config(text="WORK", fg=GREEN)
```

The timer is displayed in minutes and seconds.

---

# 🌸 Short Break

For even repetitions that are not multiples of 8, the timer starts a **5-minute short break**:

```python
count_down(SHORT_BREAK_MIN * 60)
timer_txt.config(text="SHORT BRAKE", fg=PINK)
```

---

# 🔴 Long Break

After every 8th repetition, the timer starts a **20-minute long break**:

```python
count_down(LONG_BREAK_MIN * 60)
timer_txt.config(text="LONG BRAKE", fg=RED)
```

---

# ⏳ Countdown Mechanism

The countdown is handled by the `count_down()` function.

The remaining seconds are converted into minutes and seconds using:

```python
canvas.itemconfig(
    timer,
    text=f"{count//60:02d}:{count%60:02d}"
)
```

The expression:

```text
count // 60
```

calculates the minutes, while:

```text
count % 60
```

calculates the remaining seconds.

---

## 🔁 Tkinter `after()`

Instead of blocking the entire GUI with a traditional loop, the program uses Tkinter's `after()` method:

```python
timer_countdown = window.after(
    1000,
    count_down,
    count - 1
)
```

This calls `count_down()` again after **1000 milliseconds (1 second)**.

The returned timer ID is stored in:

```python
timer_countdown
```

This ID is later used to cancel the countdown when the user presses **RESET**.

---

# 🔄 Reset Function

The `timer_reset()` function resets the timer and session counter.

It cancels the currently scheduled countdown:

```python
window.after_cancel(timer_countdown)
```

Then resets:

```python
reps = 0
```

The timer display is changed back to:

```text
00:00
```

The heading is also changed back to `"Timer"` and the completed-session check marks are cleared.

---

# ✔️ Session Tracking

After a timer finishes, the program displays check marks to represent completed sessions.

The number of marks is generated using:

```python
for i in range(math.floor(reps / 2)):
    mark += "✔"
```

The result is displayed using the `tickmark` label.

For example:

```text
✔
✔✔
✔✔✔
```

This provides a visual indication of completed work/break cycles.

---

# 🎨 Graphical User Interface

The application is built using Tkinter.

The main window is configured with:

```python
window = Tk()

window.title("Pomodoro")
window.config(
    padx=100,
    pady=50,
    bg=YELLOW
)
```

The project uses a yellow background:

```python
YELLOW = "#f7f5dd"
```

---

# 🍅 Tomato Image

The timer uses a tomato image loaded with `PhotoImage`:

```python
tomato_img = PhotoImage(
    file="./Day-028/tomato.png"
)
```

The image is displayed on a Tkinter `Canvas`.

The timer text is then placed over the tomato:

```python
timer = canvas.create_text(
    100,
    130,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 30, "bold")
)
```

---

# 🖱️ Buttons

## ▶️ START

The START button calls:

```python
start_timer
```

```python
start = Button(
    text="START",
    highlightthickness=0,
    command=start_timer
)
```

## 🔄 RESET

The RESET button calls:

```python
timer_reset
```

```python
reset = Button(
    text="RESET",
    highlightthickness=0,
    command=timer_reset
)
```

---

# 🧠 Code Concepts Used

## Tkinter

* `Tk()`
* `Label`
* `Button`
* `Canvas`
* `PhotoImage`
* `mainloop()`
* `grid()`
* `.config()`
* `.itemconfig()`

## Timer Management

* `after()`
* `after_cancel()`
* Countdown functions
* Timer IDs

## Python

* Functions
* Global variables
* Conditional statements
* `if / elif / else`
* `for` loops
* `math.floor()`
* Integer division `//`
* Modulo `%`
* f-strings

## GUI Programming

* Event-driven programming
* Button callbacks
* Dynamic widget updates
* Canvas text and image placement

---

# 📂 Project Structure

```text
Day-028/
│
├── main.py
├── tomato.png
└── README.md
```

### File Description

| File         | Purpose                                 |
| ------------ | --------------------------------------- |
| `main.py`    | Contains the Pomodoro Timer application |
| `tomato.png` | Tomato image displayed behind the timer |
| `README.md`  | Project documentation                   |

---

# 🛠️ Technologies Used

* **Python**
* **Tkinter**
* **Math module**
* **GUI Programming**

---

# 🎯 Learning Outcome

Through Day 28, I learned how to build a **functional timer application with Tkinter**.

Key concepts practiced:

* Creating a GUI application
* Using Tkinter widgets
* Working with `Canvas`
* Displaying images in Tkinter
* Creating button callbacks
* Updating GUI elements dynamically
* Creating a countdown timer
* Using `after()` for scheduled callbacks
* Cancelling scheduled callbacks with `after_cancel()`
* Managing application state using variables
* Using mathematical operations for time conversion

---

# 🚀 Future Improvements

Possible improvements include:

* Add a pause/resume button
* Add customizable work and break durations
* Prevent multiple timers from starting simultaneously
* Add sound notifications when a session ends
* Add a session counter
* Improve the check-mark tracking
* Add a settings section for timer customization

---

# ✅ Project Status

**Completed ✔️**

* [x] Create Tkinter window
* [x] Add tomato image
* [x] Create countdown timer
* [x] Add work sessions
* [x] Add short breaks
* [x] Add long breaks
* [x] Add START button
* [x] Add RESET button
* [x] Track repetitions
* [x] Display completed-session check marks
* [x] Automatically move between sessions

---

# 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
