# 🐍 Day 020 - Snake Game - Part 1

## 📌 Project Overview

This is **Part 1 of the Day 020** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

In this part, I started building a classic **Snake Game** using Python's `turtle` module.

The main focus of Part 1 is creating the snake, controlling its movement, and allowing the player to change its direction using the keyboard.

The project also introduces a more structured approach by separating the snake logic into its own Python module.

---

## 🎮 How It Works

1. A `600 × 600` Turtle screen is created with a black background.
2. A `Snake` object is created.
3. The snake starts with **three segments**.
4. The snake continuously moves forward.
5. The player can control the snake using the arrow keys.
6. The snake's body follows the head as it moves.
7. The program prevents the snake from immediately reversing direction.

---

## 🐍 Starting Snake

The snake starts with three segments positioned at:

```python
STARTING_POSITION = [
    (0, 0),
    (-20, 0),
    (-40, 0)
]
```

Each segment is represented by a white square Turtle.

The segments are stored inside a list:

```python
self.segment = []
```

---

## 🎮 Controls

| Key      | Action     |
| -------- | ---------- |
| ⬆️ Up    | Move Up    |
| ⬇️ Down  | Move Down  |
| ⬅️ Left  | Move Left  |
| ➡️ Right | Move Right |

The keyboard controls are connected to the Snake object's methods:

```python
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
```

---

## 🧠 Snake Class

The snake is implemented as a custom Python class:

```python
class Snake:
```

The class is responsible for:

* Creating the snake
* Storing its segments
* Controlling movement
* Changing direction
* Preventing direct reverse movement

The head of the snake is stored separately:

```python
self.head = self.segment[0]
```

---

## 🔄 Snake Movement

The snake's body follows the segment in front of it.

The segments are moved **backwards from the tail toward the head**:

```python
for seg_num in range(len(self.segment) - 1, 0, -1):
    new_x = self.segment[seg_num - 1].xcor()
    new_y = self.segment[seg_num - 1].ycor()
    self.segment[seg_num].goto(new_x, new_y)
```

After the body segments are repositioned, the head moves forward:

```python
self.head.forward(MOVE_DISTANCE)
```

The movement distance is set to:

```python
MOVE_DISTANCE = 20
```

---

## 🧭 Direction Control

The snake uses headings to control its direction:

```python
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
```

The program also prevents the snake from turning directly into itself.

For example:

```python
def up(self):
    if self.head.heading() != DOWN:
        self.head.setheading(UP)
```

This prevents the snake from immediately moving from **Down → Up**.

---

## 💻 Code Concepts Used

* Object-Oriented Programming
* Classes and Objects
* Class methods
* Constructors (`__init__`)
* Instance attributes
* Python modules
* Importing custom classes
* Lists
* `for` loops
* `while` loops
* Keyboard event handling
* Turtle Graphics
* Coordinates
* Object movement
* Direction and heading

---

## 📂 Project Structure

```text
Day-020-Snake-Game-Part-1/
│── main.py
│── snake.py
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3
* Turtle Graphics
* Object-Oriented Programming

---

## 🎯 Learning Outcome

By completing Part 1 of the Snake Game, I learned how to:

* Create a custom `Snake` class
* Organize code into separate Python files
* Create and manage multiple Turtle objects
* Store objects inside a list
* Control multiple objects as a single game component
* Implement continuous movement
* Handle keyboard events
* Work with Turtle headings and coordinates
* Prevent invalid reverse-direction movement
* Apply Object-Oriented Programming to a game

---

## 🚧 Current Progress

This is **Part 1** of the Snake Game.

### Completed

* [x] Create the game screen
* [x] Create the Snake class
* [x] Create the initial three snake segments
* [x] Implement snake movement
* [x] Implement keyboard controls
* [x] Prevent direct reverse movement
* [x] Separate snake logic into `snake.py`

### Coming in Later Parts

The complete Snake Game will be expanded with additional functionality such as food, scoring, collision detection, and game-over logic.

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
