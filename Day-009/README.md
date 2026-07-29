# 🔨 Day 009 - Secret Auction Program

## 📌 Project Overview

This is the **Day 009** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Secret Auction Program** is a command-line bidding application where multiple users can secretly enter their names and bid amounts.

Once all bidders have entered their bids, the program compares them and determines the person with the **highest bid**, announcing them as the winner.

This project mainly focuses on working with **Python dictionaries, functions, loops, and program logic**.

---

## 🚀 How It Works

1. The program displays the Secret Auction logo.
2. The first bidder enters their:

   * Name
   * Bid amount
3. The bid is stored in a Python dictionary.
4. The program asks whether there are any other bidders.
5. If there are more bidders, the screen is cleared using blank lines to keep previous bids hidden.
6. The process continues until there are no more bidders.
7. The program checks all submitted bids.
8. The bidder with the highest amount is announced as the winner.

### Example

```text
What is your name?: Chaitanya
What is your bid: $250

Are there any other bidders? Type 'yes' or 'no'.
yes

What is your name?: Rohit
What is your bid: $350

Are there any other bidders? Type 'yes' or 'no'.
no

The winner is Rohit with a bid of $350.0
```

---

## 💻 Code Concepts Used

* Python Dictionaries
* Functions
* Function parameters
* `for` loops
* `while` loops
* Conditional statements
* Boolean variables
* Dictionary key-value pairs
* User input
* Comparing numerical values
* Importing custom modules

---

## 🧠 Auction Logic

Each bidder's name and bid amount are stored in a dictionary.

For example:

```python
bid = {
    "Chaitanya": 250,
    "Rohit": 350,
    "Pranav": 300
}
```

The program loops through the dictionary and compares each bid with the current highest bid.

```python
if bid_amt > highest_bid:
    highest_bid = bid_amt
    winner = bids
```

Whenever a higher bid is found, the program updates both the **highest bid** and the **winner**.

---

## 📂 Project Structure

```text
Day-009-Secret-Auction/
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

* Create and use Python dictionaries
* Store data using key-value pairs
* Add new data dynamically to a dictionary
* Loop through dictionary entries
* Create functions that accept dictionaries as parameters
* Compare values to find the maximum
* Use `while` loops for repeated user input
* Combine functions, dictionaries, loops, and conditions
* Build a simple multi-user bidding application

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
