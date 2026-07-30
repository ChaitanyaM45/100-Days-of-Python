# 🃏 Day 011 - Blackjack Game

## 📌 Project Overview

This is the **Day 011** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Blackjack Game** is a command-line implementation of the classic card game Blackjack. The player competes against the computer and tries to get a hand value as close to **21** as possible without going over.

The game includes card dealing, score calculation, Blackjack detection, Ace handling, and winner comparison.

This project brings together many Python concepts learned throughout the previous days.

---

## 🎯 Game Objective

The goal of Blackjack is to have a hand with a total value closer to **21** than the computer without exceeding 21.

### Card Values

* Number cards → Their face value
* Jack, Queen, King → `10`
* Ace → `11` or `1`
* Blackjack → `21` using exactly two cards

---

## 🚀 How It Works

1. The player and computer are each dealt two random cards.
2. The player's cards and current score are displayed.
3. Only the computer's first card is shown initially.
4. The player can choose:

   * `y` → Get another card (**Hit**)
   * `n` → Stop taking cards (**Stand**)
5. An Ace initially counts as `11`.
6. If the score exceeds 21, an Ace can be converted from `11` to `1`.
7. A score of 21 with exactly two cards is treated as **Blackjack**.
8. The computer draws additional cards according to the game logic.
9. The final scores are compared.
10. The winner is displayed.

---

## 🕹️ Example

```text id="l7udsa"
Your Cards: [10, 7], Your Score: 17
Computer's First Cards: 10

Type 'y' to get another card or type 'n' to pass: n

Your Final Hands: [10, 7]
Your Final Score: 17

Computer Final Hands: [10, 6, 8]
Computer Final Score: 24

Computer Went Over, You Win :)
```

---

## 💻 Code Concepts Used

* Python Functions
* Function parameters
* Return values
* Lists
* `for` loops
* `while` loops
* Conditional statements
* Boolean variables
* Random module
* `random.choice()`
* List manipulation
* `sum()`
* User input
* Game state management
* Importing custom modules

---

## 🃏 Card Dealing

The `deal_cards()` function randomly selects a card from the available card values.

```python id="cbk7iw"
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
```

The value `10` appears four times to represent:

```text id="oh5j4s"
10 → Number 10
10 → Jack
10 → Queen
10 → King
```

---

## 🧮 Score Calculation

The `calculate_score()` function calculates the total value of a hand.

```python id="njp1so"
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
```

A return value of `0` represents a **Blackjack**.

The function also handles an Ace by changing its value from `11` to `1` when the player's score would otherwise exceed 21.

---

## ⚖️ Winner Comparison

The `compare()` function determines the final result by comparing the player's score with the computer's score.

It checks for:

* Draw
* Player Blackjack
* Computer Blackjack
* Player going over 21
* Computer going over 21
* Higher player score
* Higher computer score

---

## 📂 Project Structure

```text id="d67h7q"
Day-011-Blackjack/
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

* Break a larger program into multiple functions
* Work with lists and dynamically add cards
* Generate random values using the `random` module
* Calculate and update game scores
* Handle special game rules such as Blackjack
* Handle an Ace as either `1` or `11`
* Control game flow using Boolean variables
* Use nested loops and conditional statements
* Compare multiple game conditions
* Build a more complex command-line game

---

## 🔮 Future Improvements

Some improvements that can be added include:

* Add a **Play Again** option
* Add betting and virtual chips
* Add difficulty levels
* Improve input validation
* Display playing card ASCII art
* Keep track of wins and losses
* Improve the computer dealer logic

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
