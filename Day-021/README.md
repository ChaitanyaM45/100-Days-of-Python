# 🐍 Day 021 - Snake Game - Part 2

## 📌 Project Overview

This is **Part 2 of the Day 021** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

In Part 2, I expanded the Snake Game from Day 20 by adding the core gameplay features that make it a complete playable game.

The game now includes:

* 🍎 Food
* 🐍 Snake growth
* 🏆 Score tracking
* 🧱 Wall collision detection
* 💥 Self-collision detection
* 🎮 Game Over functionality

The project continues to use **Object-Oriented Programming (OOP)** and separates different game components into individual Python modules.

---

## 🚀 How It Works

1. The game starts with a three-segment snake.
2. The snake continuously moves forward.
3. The player controls the snake using the arrow keys.
4. Food appears at a random position on the screen.
5. When the snake eats the food:

   * The food moves to a new random position.
   * The snake grows by one segment.
   * The score increases by `1`.
6. If the snake hits the wall, the game ends.
7. If the snake collides with its own body, the game ends.
8. The final screen displays **Game Over**.

---

## 🎮 Controls

| Key      | Action     |
| -------- | ---------- |
| ⬆️ Up    | Move Up    |
| ⬇️ Down  | Move Down  |
| ⬅️ Left  | Move Left  |
| ➡️ Right | Move Right |

---

## 🍎 Food System

The `Food` class inherits from Python's Turtle class:

```python
class Food(Turtle):
```

The food is represented as a small white circle and is placed randomly on the screen.

```python
random_x = random.randint(-280, 280)
random_y = random.randint(-280, 280)
self.goto(random_x, random_y)
```

When the snake gets close enough to the food, the food is refreshed at a new location.

---

## 🐍 Snake Growth

When the snake eats food, the `extend()` method is called:

```python
if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
```

The new segment is added at the position of the snake's last segment:

```python
def extend(self):
    self.add_segment(self.segment[-1].position())
```

This allows the snake to grow throughout the game.

---

## 🏆 Scoreboard

The `Scoreboard` class is responsible for displaying and updating the player's score.

The initial score is:

```text
Score : 0
```

Whenever the snake eats food:

```python
def increase_score(self):
    self.score += 1
```

The scoreboard is then cleared and rewritten with the updated score.

---

## 🧱 Wall Collision

The game checks whether the snake's head has crossed the game boundaries:

```python
if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
   snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False
    scoreboard.game_over()
```

If the snake hits the wall, the game ends.

---

## 💥 Self-Collision

The game also checks whether the snake's head collides with any part of its own body.

```python
for segment in snake.segment:
    if segment == snake.head:
        continue

    if snake.head.distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over()
```

If the head gets too close to another segment, the game ends.

---

## 🏗️ Project Structure

The project is divided into separate modules:

```text
Day-021-Snake-Game-Part-2/
│── main.py
│── snake.py
│── food.py
│── scoreboard.py
└── README.md
```

### `main.py`

Controls the main game loop and handles:

* Snake movement
* Food collision
* Wall collision
* Self-collision
* Game state

### `snake.py`

Contains the `Snake` class responsible for:

* Creating the snake
* Moving the snake
* Changing direction
* Growing the snake

### `food.py`

Contains the `Food` class responsible for:

* Creating the food
* Positioning the food randomly

### `scoreboard.py`

Contains the `Scoreboard` class responsible for:

* Displaying the score
* Increasing the score
* Displaying Game Over

---

## 💻 Code Concepts Used

* Object-Oriented Programming
* Inheritance
* Classes and Objects
* Custom Python Modules
* Importing classes
* Turtle Graphics
* Lists
* Loops
* Conditional statements
* Random number generation
* Collision detection
* Coordinates and distances
* Game state management
* Methods and attributes

---

## 🛠️ Technologies Used

* Python 3
* Turtle Graphics
* Object-Oriented Programming

---

## 🎯 Learning Outcome

By completing Part 2 of the Snake Game, I learned how to:

* Build a complete playable game using Python
* Use inheritance with the Turtle class
* Organize a project into multiple Python modules
* Detect collisions using coordinates and distances
* Dynamically add objects to a list
* Make the snake grow during gameplay
* Create and update a scoreboard
* Detect wall and self-collisions
* Manage game states
* Apply OOP concepts to a larger project

---

## 🚧 Game Progress

### Completed

* [x] Create the snake
* [x] Control the snake using keyboard input
* [x] Add food
* [x] Detect food collision
* [x] Grow the snake
* [x] Add score tracking
* [x] Detect wall collision
* [x] Detect self-collision
* [x] Add Game Over screen
* [x] Separate game components into modules

---

## 🔮 Future Improvements

Some improvements that can be added include:

* Add a **High Score** system
* Add a **Play Again** option
* Prevent food from spawning inside the snake
* Add increasing difficulty as the score increases
* Add sound effects
* Add different themes
* Add a start screen
* Save high scores between game sessions

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
