# 🎯 Day 7 - Hangman Game

## 📌 Project Overview

This is the **Day 7** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Hangman Game** is a classic word-guessing game where the player attempts to guess a randomly selected word one letter at a time. The player has a limited number of lives, and each incorrect guess reduces the remaining lives. The game ends when the player either guesses the entire word or runs out of lives.

This project helps strengthen Python fundamentals by combining loops, conditionals, lists, strings, and randomization to build a complete interactive game.

---

## 🚀 How It Works

1. The program randomly selects a word from a predefined word list.
2. The player guesses one letter at a time.
3. If the guessed letter exists in the word, all matching positions are revealed.
4. If the guess is incorrect, one life is deducted.
5. The game continues until:
   - The player guesses the complete word (**Win**), or
   - The player runs out of lives (**Lose**).

### Example

```text
['_', '_', '_', '_', '_', '_']

Guess the letter: a

['_', 'a', '_', '_', '_', '_']

Guess the letter: z

Wrong Guess
Lives Left: 5

...

['v', 'e', 'd', 'a', 'n', 't']

You Win
```

---

## 💻 Code Concepts Used

- Python Lists
- `while` loops
- `for` loops
- Conditional statements (`if` / `else`)
- String indexing
- `random.choice()`
- Variables
- User input
- Game logic

---

## 📂 Project Structure

```
Day-07-Hangman/
│── main.py
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3

---

## 🎯 Learning Outcome

By completing this project, I learned how to:
- Build a complete command-line game
- Use loops to control game flow
- Update lists dynamically
- Work with strings and indexing
- Generate random words using the `random` module
- Implement win and lose conditions

---

## 🚀 Future Improvements

Some enhancements that can be added to this game include:

- Displaying Hangman ASCII art for each remaining life
- Preventing duplicate guesses
- Using a larger dictionary of words
- Showing guessed letters separately
- Adding difficulty levels
- Allowing the player to play multiple rounds

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45