# 🐢 Day 019(B) - Turtle Race

## 📌 Project Overview

This is the **Day 019(B)** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Turtle Race** is an interactive racing game built using Python's `turtle` module. Six turtles with different colors compete against each other, and the player places a bet on which turtle they think will win.

Each turtle moves forward by a random distance, creating a different race outcome every time the program runs.

---

## 🚀 How It Works

1. A Turtle graphics window is created.
2. The player is asked to enter the color of the turtle they think will win.
3. Six turtles are created with different colors:

   * 🔴 Red
   * 🟢 Green
   * 🟡 Yellow
   * 🔵 Blue
   * 🟣 Purple
   * 🟠 Orange
4. Each turtle starts at a different vertical position.
5. During the race, every turtle moves a random distance between `0` and `10`.
6. The race continues until one turtle crosses the finish line.
7. The winning turtle's color is determined.
8. The program tells the player whether their prediction was correct.

---

## 🏁 Example

```text
Make your bet
Which Turtle will win the race? Enter Color: red

You Won! red turtle won the race!
```

If the player's prediction is incorrect:

```text
Make your bet
Which Turtle will win the race? Enter Color: blue

You Lose! yellow turtle won the race!
```

---

## 🐢 Turtles Used

The race contains six turtles:

```python
color = [
    "red",
    "green",
    "yellow",
    "blue",
    "purple",
    "orange"
]
```

Each turtle is positioned on a different horizontal lane using predefined Y coordinates.

---

## 🎲 Random Movement

Every turtle moves a random distance on each turn:

```python
rand_dist = random.randint(0, 10)
turtle.forward(rand_dist)
```

Because the distance is randomly generated, the winner is different each time the game is played.

---

## 🏆 Determining the Winner

The program checks each turtle's X-coordinate:

```python
if turtle.xcor() > 230:
    is_race_on = False
```

When a turtle crosses the finish line, its color is stored as the winning color.

The player's bet is then compared with the winning turtle:

```python
if winning_color == user_bet:
    print(f"You Won! {winning_color} turtle won the race!")
else:
    print(f"You Lose! {winning_color} turtle won the race!")
```

---

## 💻 Code Concepts Used

* Python Turtle Graphics
* `random` module
* `random.randint()`
* Lists
* `for` loops
* `while` loops
* Conditional statements
* User input with `screen.textinput()`
* Turtle positioning
* Turtle movement
* `xcor()`
* `pencolor()`
* Boolean variables
* Object creation

---

## 📂 Project Structure

```text
Day-019B-Turtle-Race/
│── main.py
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3
* Turtle Graphics
* Random Module

---

## 🎯 Learning Outcome

By completing this project, I learned how to:

* Create multiple Turtle objects
* Store objects inside a list
* Use loops to control multiple objects
* Randomize movement using the `random` module
* Position objects on different lanes
* Detect when a Turtle reaches a specific position
* Accept user input through a Turtle screen
* Build an interactive racing game
* Combine Turtle graphics, loops, lists, and randomness

---

## 🔮 Future Improvements

Some improvements that can be added include:

* Add a visible finish line
* Add a countdown before the race starts
* Display the race winner on the screen
* Add a replay option
* Add a betting score system
* Allow the player to place virtual bets
* Add more turtles and customizable colors
* Improve the graphical appearance of the race

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
