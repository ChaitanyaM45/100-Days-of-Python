# 🎯 Day 012 - Number Guessing Game

## 📌 Project Overview

This is the **Day 012** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Number Guessing Game** is an interactive command-line game where the computer randomly selects a number between **1 and 100**, and the player tries to guess it within a limited number of attempts.

The player can select between **Easy** and **Hard** difficulty levels, which determine how many guesses are available.

This project focuses on combining **functions, loops, conditionals, random number generation, and game logic**.

---

## 🎮 Difficulty Levels

The game provides two difficulty options:

* 🟢 **Easy Mode** → 10 attempts
* 🔴 **Hard Mode** → 5 attempts

The player must guess the randomly generated number before running out of attempts.

---

## 🚀 How It Works

1. The program displays the game logo.
2. The computer randomly generates a number between `1` and `100`.
3. The player selects a difficulty level:

   * `easy` → 10 lives
   * `hard` → 5 lives
4. The program displays the remaining lives.
5. The player enters a guess.
6. The program compares the guess with the secret number.
7. The player receives a hint:

   * **Too high!**
   * **Too low!**
8. An incorrect guess reduces the remaining lives by one.
9. The game continues until the player guesses correctly or runs out of guesses.

---

## 🕹️ Example

```text
Welcome to Number Guessing Game!
I am thinking of a number between 1 to 100!

Choose a difficulty. Type 'easy' or 'hard': hard

You have 5 lives left.
Make a guess: 70

Too high!
Guess again.

You have 4 lives left.
Make a guess: 40

Too low!
Guess again.

You have 3 lives left.
Make a guess: 55

You got it! The answer was 55.
```

---

## 💻 Code Concepts Used

* Python `random` module
* `random.randint()`
* Variables
* `while` loops
* Conditional statements
* User input
* Integer conversion
* Comparison operators
* Difficulty selection
* Game state management
* Importing custom modules

---

## 🎲 Random Number Generation

The secret number is randomly generated between `1` and `100`:

```python
num = random.randint(1, 100)
```

This means a different number can be selected every time the game starts.

---

## ❤️ Difficulty & Lives

The number of available guesses depends on the selected difficulty:

```python
if diff == 'easy':
    lives = 10
else:
    lives = 5
```

### Easy

```text
Lives: 10
```

### Hard

```text
Lives: 5
```

Each incorrect guess decreases the number of lives:

```python
lives -= 1
```

---

## 🔍 Guessing Logic

The player's guess is compared with the randomly generated number.

```python
if user_num == num:
    print(f"You got it! The answer was {num}.")
```

If the guess is incorrect, the game provides a hint:

```text
Too high!
```

or

```text
Too low!
```

This helps the player narrow down the possible number.

---

## 📂 Project Structure

```text
Day-012-Number-Guessing-Game/
│── main.py
│── art.py
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3

---

## 🎯 Learning Outcome

By completing this project, I learned how to:

* Generate random numbers within a specific range
* Create difficulty levels in a game
* Control the number of attempts using variables
* Use `while` loops for repeated guesses
* Compare numerical values
* Provide hints based on user input
* Track remaining attempts
* Implement win and lose conditions
* Combine multiple Python concepts into an interactive game

---

## 🔮 Future Improvements

Some improvements that can be added include:

* Validate the difficulty input
* Handle non-numeric guesses
* Add a **Play Again** option
* Add multiple difficulty levels
* Track the number of guesses used
* Add a scoring system
* Improve the win/lose flow

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
