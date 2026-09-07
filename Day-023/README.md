# 🚦 Day 023 - Turtle Crossing Game

## 📌 Project Overview

This project is a **Turtle Crossing Game** built using Python's `turtle` module.

The player controls a turtle and must **cross the road without getting hit by moving cars**. Each time the player successfully reaches the finish line, the game advances to the next level and the cars become faster.

The project brings together **Object-Oriented Programming, keyboard controls, collision detection, game levels, and animated movement**.

---

## 🎮 How It Works

1. The game opens a **600 × 600 Turtle graphics screen**.
2. The player starts at the bottom of the screen.
3. Use the **Up Arrow** key to move the player forward.
4. Cars are continuously created and move across the screen.
5. If the player collides with a car, the game ends.
6. When the player reaches the finish line:

   * The player returns to the starting position.
   * The game level increases.
   * Cars become faster.
7. The game continues until the player is hit by a car.

---

## 🕹️ Controls

| Key         | Action              |
| ----------- | ------------------- |
| ⬆️ Up Arrow | Move player forward |

---

## 🚗 Game Components

The project is divided into separate classes/modules:

### 👤 Player

The `Player` class manages:

* Player movement
* Starting position
* Moving upward
* Detecting whether the finish line has been reached
* Returning to the starting position

### 🚙 CarManager

The `CarManager` class manages:

* Creating cars
* Storing all cars in a list
* Moving cars across the screen
* Increasing car speed when the player reaches a new level

### 🏆 Scoreboard

The `Scoreboard` class manages:

* Displaying the current level
* Increasing the level
* Displaying the **Game Over** message

---

## 💥 Collision Detection

The game checks the distance between the player and every car:

```python
for car in car_manager.all_cars:
    if car.distance(player) < 20:
        game_is_on = False
        scoreboard.game_over()
```

If a car comes within a distance of `20` from the player, the game ends.

---

## 🏁 Level Progression

When the player successfully reaches the finish line:

```python
if player.is_at_finish_line():
    player.go_to_start()
    car_manager.level_up()
    scoreboard.increase_level()
```

The player is sent back to the starting position and the difficulty increases by making the cars faster.

---

## 🔄 Main Game Loop

The game continuously performs these actions:

```text
Start Game
    ↓
Create Cars
    ↓
Move Cars
    ↓
Check Player-Car Collision
    ↓
Check Finish Line
    ↓
Level Up if Successful
    ↓
Repeat
```

The game uses:

```python
time.sleep(0.1)
screen.update()
```

to control the animation speed and update the screen.

---

## 🧠 Code Concepts Used

* Object-Oriented Programming (OOP)
* Python classes and objects
* Inheritance through Turtle-based game objects
* Custom Python modules
* `turtle` graphics
* Keyboard event handling
* Game loops
* Collision detection using `distance()`
* Lists for managing multiple cars
* Conditional statements
* Functions and methods
* Screen animation with `tracer()` and `update()`
* Time delays using `time.sleep()`
* Level progression
* Game state management

---

## 📂 Project Structure

```text
Day-023-Turtle-Crossing/
│
├── main.py
├── player.py
├── car_manager.py
└── scoreboard.py
```

### File Description

| File             | Purpose                                         |
| ---------------- | ----------------------------------------------- |
| `main.py`        | Runs the main game loop and controls game logic |
| `player.py`      | Defines the player and its movement             |
| `car_manager.py` | Creates, stores, moves, and speeds up cars      |
| `scoreboard.py`  | Displays the level and game-over message        |

---

## 🛠️ Technologies Used

* **Python**
* **Turtle Graphics**
* **Object-Oriented Programming**
* **Time module**

---

## 🎯 Learning Outcome

Through this project, I practiced building a complete interactive game using Python and OOP.

Key concepts learned:

* Managing multiple objects using classes
* Handling keyboard input
* Detecting collisions
* Creating an animated game loop
* Managing game states
* Implementing increasing difficulty through levels
* Organizing a larger project into multiple Python modules

---

## 🚀 Future Improvements

Possible improvements include:

* Add horizontal movement for the player
* Add different car colors and sizes
* Increase the number of cars at higher levels
* Add sound effects
* Add a high-score system
* Add a start/restart button
* Add lives instead of ending the game after one collision

---

## ✅ Project Status

**Completed ✔️**

This project successfully implements:

* Player movement
* Moving cars
* Collision detection
* Finish-line detection
* Level progression
* Increasing car speed
* Game-over state

---

## 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
