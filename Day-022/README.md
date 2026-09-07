# 🏓 Day 022 - Pong Game

## 📌 Project Overview

This is the **Day 022** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Pong Game** is a two-player arcade game built using Python's `turtle` module.

The game features two paddles, a moving ball, collision detection, and a scoreboard. Players control their paddles and try to prevent the ball from passing their side of the screen.

This project combines **Object-Oriented Programming (OOP), Turtle graphics, keyboard controls, collision detection, and game logic** to create a complete playable game.

---

## 🎮 How It Works

1. The game window is created with a size of `800 × 600`.
2. Two paddles are positioned on opposite sides of the screen.
3. A ball starts moving across the screen.
4. Players control the paddles using the keyboard.
5. The ball:
   - Bounces off the top and bottom walls.
   - Bounces off the paddles.
   - Speeds up after hitting a paddle.
6. If the ball passes a paddle, the opposing player gets a point.
7. The ball resets to the center after a point is scored.
8. The scoreboard keeps track of both players' scores.

---

## 🎮 Controls

| Player | Key | Action |
|--------|-----|--------|
| 🏓 Left Paddle | `↑` | Move Up |
| 🏓 Left Paddle | `↓` | Move Down |
| 🏓 Right Paddle | `8` | Move Up |
| 🏓 Right Paddle | `2` | Move Down |

---

## 🏓 Game Components

The project is divided into separate classes:

### Paddle

The `Paddle` class handles:

- Creating the paddles
- Positioning the paddles
- Moving the paddles upward
- Moving the paddles downward

Two paddle objects are created:

```python
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
```

---

### ⚪ Ball

The `Ball` class handles:

- Ball movement
- Horizontal bouncing
- Vertical bouncing
- Ball reset
- Movement speed

The ball changes direction when it collides with a wall or paddle.

---

### 🏆 Scoreboard

The `Scoreboard` class handles:

- Displaying player scores
- Increasing the left player's score
- Increasing the right player's score

When the ball passes a paddle, the appropriate score is updated.

---

## 💥 Collision Detection

### Wall Collision

The game checks whether the ball reaches the top or bottom boundaries:

```python
if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()
```

The ball then changes its vertical direction.

---

### Paddle Collision

The game checks both the ball's position and its distance from the paddles:

```python
if (r_paddle.distance(ball) < 50 and ball.xcor() > 320) or \
   (l_paddle.distance(ball) < 50 and ball.xcor() < -320):
    ball.bounce_x()
```

When the ball hits a paddle, it bounces horizontally.

The ball also becomes faster:

```python
ball.move_speed *= 0.9
```

---

## 🏆 Scoring

If the ball passes the right paddle:

```python
if ball.xcor() > 380:
    ball.resetpos()
    scoreboard.l_point()
```

The left player receives a point.

If the ball passes the left paddle:

```python
if ball.xcor() < -380:
    ball.resetpos()
    scoreboard.r_point()
```

The right player receives a point.

---

## ⚡ Game Speed

The game uses:

```python
screen.tracer(0)
```

and manually updates the screen using:

```python
screen.update()
```

The `time.sleep()` function is also used to control the movement speed of the ball.

---

## 💻 Code Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects
- Inheritance
- Custom Python Modules
- Turtle Graphics
- Keyboard Event Handling
- `Screen()`
- `Turtle()`
- `distance()`
- `xcor()` and `ycor()`
- Collision Detection
- Loops
- Conditional Statements
- Game State Management
- Score Tracking
- Object Movement
- Screen Animation

---

## 📂 Project Structure

```text
Day-022-Pong-Game/
│── main.py
│── paddle.py
│── ball.py
│── scoreboard.py
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- Turtle Graphics
- Object-Oriented Programming

---

## 🎯 Learning Outcome

By completing this project, I learned how to:

- Build a complete two-player arcade game
- Work with multiple classes and objects
- Organize a project into separate Python modules
- Handle keyboard events
- Implement collision detection
- Control object movement
- Detect when the ball passes a boundary
- Implement a scoring system
- Create bouncing mechanics
- Control game animation using `tracer()` and `update()`
- Increase the ball's movement speed during gameplay

---

## 🚧 Game Progress

### Completed

- [x] Create the game screen
- [x] Create the left paddle
- [x] Create the right paddle
- [x] Add keyboard controls
- [x] Create the ball
- [x] Implement ball movement
- [x] Detect wall collisions
- [x] Detect paddle collisions
- [x] Add ball speed increase
- [x] Detect missed paddles
- [x] Add score tracking
- [x] Reset the ball after a point

---

## 🔮 Future Improvements

Some improvements that can be added include:

- Add a winning score limit
- Display a **Game Over** message
- Add a restart option
- Add sound effects
- Add a start/countdown screen
- Improve paddle movement boundaries
- Add difficulty levels
- Add a pause/resume feature
- Add customizable player names

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**  
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45