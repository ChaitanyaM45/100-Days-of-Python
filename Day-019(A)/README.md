# 🎮 Day 019(A) - Turtle Sketcher

## 📌 Project Overview

This is the **Day 019(A)** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

In this project, I created an interactive **Turtle Keyboard Control** program using Python's `turtle` module.

The user can control the Turtle using the keyboard arrow keys. The program allows the Turtle to move forward and backward, rotate left and right, and clear the drawing.

This project focuses on **event listeners, keyboard controls, functions, and Turtle graphics**.

---

## 🚀 How It Works

The program uses keyboard keys to control the Turtle:

| Key      | Action            |
| -------- | ----------------- |
| ⬆️ Up    | Move Forward      |
| ⬇️ Down  | Move Backward     |
| ⬅️ Left  | Turn Left         |
| ➡️ Right | Turn Right        |
| `C`      | Clear the Drawing |

The Turtle responds immediately when the corresponding key is pressed.

---

## 🎮 Controls

### ⬆️ Move Forward

Press the **Up Arrow** key to move the Turtle forward by 10 pixels.

```python
def move_forward():
    tim.forward(10)
```

### ⬇️ Move Backward

Press the **Down Arrow** key to move backward.

```python
def move_backward():
    tim.backward(10)
```

### ⬅️ Turn Left

Press the **Left Arrow** key to rotate the Turtle 10 degrees to the left.

```python
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
```

### ➡️ Turn Right

Press the **Right Arrow** key to rotate the Turtle 10 degrees to the right.

```python
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
```

### 🧹 Clear

Press **C** to return the Turtle to its starting position and clear the drawing.

```python
def clear():
    tim.home()
    tim.clear()
```

---

## 💻 Code Concepts Used

* Python Turtle Graphics
* Functions
* Event Listeners
* Keyboard Input
* `screen.listen()`
* `screen.onkey()`
* Turtle movement
* Turtle heading
* `setheading()`
* `home()`
* `clear()`

---

## 🧠 Key Concept - Event Listeners

The program listens for keyboard events using:

```python
screen.listen()
```

Keyboard keys are then connected to specific functions:

```python
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
```

This allows the program to respond to user actions instead of simply executing from top to bottom.

---

## 📂 Project Structure

```text
Day-019A-Turtle-Keyboard-Control/
│── main.py
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3
* Turtle Graphics

---

## 🎯 Learning Outcome

By completing this project, I learned how to:

* Create interactive Turtle graphics
* Handle keyboard events in Python
* Connect keyboard keys to functions
* Use event listeners
* Control Turtle movement
* Change the Turtle's heading
* Clear and reset the Turtle screen
* Build interactive programs using user input

---

## 🔮 Future Improvements

Some improvements that can be added include:

* Add different movement speeds
* Add a reset button
* Add color-changing controls
* Add pen up/down controls
* Add an eraser mode
* Add a save drawing feature
* Add more keyboard shortcuts

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
