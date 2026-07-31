# 📈 Day 014 - Higher Lower Game

## 📌 Project Overview

This is the **Day 014** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Higher Lower Game** is an interactive command-line game where the player compares two famous people, brands, or organizations and guesses which one has more social media followers.

The game continues as long as the player makes the correct choice. Each correct answer increases the score, while an incorrect answer ends the game and displays the final score.

This project combines many Python concepts learned throughout the previous days into one complete game.

---

## 🚀 How It Works

1. The program randomly selects two entries from the game data.
2. The player is shown:
   - Name
   - Description
   - Country
3. The player chooses who they think has more followers:
   - `A`
   - `B`
4. The program compares the follower counts.
5. If the answer is correct:
   - The score increases by `1`
   - Option B becomes the new Option A
   - A new Option B is randomly selected
6. The game continues until the player gives a wrong answer.
7. The final score is displayed.

---

## 🎮 Example

```text
Compare A: Cristiano Ronaldo, a Footballer, from Portugal

 _    __    
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)

Against B: Selena Gomez, a Musician and actress, from United States

Who has more followers? Type 'A' or 'B': a

You're right! Current score: 1.
```

If the player chooses incorrectly:

```text
Sorry, that's wrong. Final score: 1
```

---

## 🧠 Game Logic

The program compares the follower counts of both options:

```python
if a["follower_count"] > b["follower_count"]:
    correct = "a"
else:
    correct = "b"
```

The player's answer is then compared with the correct answer.

```python
if action == correct:
    points += 1
else:
    should_continue = False
```

---

## 🔄 Continuing the Game

After a correct answer, **Option B becomes the new Option A**:

```python
a = b
b = random.choice(data)
```

A new Option B is then randomly selected.

The program also ensures that A and B are not the same:

```python
while a == b:
    b = random.choice(data)
```

This keeps every comparison between two different entries.

---

## 💻 Code Concepts Used

- Python Dictionaries
- Lists
- `while` loops
- Conditional statements
- Boolean variables
- `random.choice()`
- Dictionary key-value access
- String formatting using f-Strings
- User input
- Score tracking
- Game state management
- Importing custom modules
- Working with external game data

---

## 📂 Project Structure

```text
Day-014-Higher-Lower-Game/
│── main.py
│── art.py
│── game_data.py
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3

---

## 🎯 Learning Outcome

By completing this project, I learned how to:

- Work with lists containing dictionaries
- Access values from dictionaries using keys
- Randomly select data using `random.choice()`
- Compare numerical values
- Track the player's score
- Control game flow using `while` loops
- Prevent duplicate random selections
- Move data between game rounds
- Work with external Python modules
- Separate game data, ASCII art, and program logic
- Combine multiple Python concepts into a complete interactive game

---

## 🔮 Future Improvements

Some improvements that can be added include:

- Validate user input
- Add a **Play Again** option
- Display the player's high score
- Add difficulty levels
- Add more entries to the game data
- Add a limited number of lives
- Improve the command-line interface

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**  
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45