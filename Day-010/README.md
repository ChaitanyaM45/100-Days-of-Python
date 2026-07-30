# 🧮 Day 010 - Calculator

## 📌 Project Overview

This is the **Day 010** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Calculator** is a command-line Python application that performs basic mathematical operations based on the user's input.

The program allows users to enter two numbers, select an arithmetic operation, and displays the calculated result. The calculator can also be used repeatedly until the user chooses to exit.

This project focuses on **functions with outputs, dictionaries, loops, and calling functions dynamically**.

---

## 🚀 How It Works

1. The program displays the calculator logo.
2. The user enters the first number.
3. The available mathematical operations are displayed:

   * `+` Addition
   * `-` Subtraction
   * `*` Multiplication
   * `/` Division
4. The user selects an operation.
5. The user enters the second number.
6. The appropriate function is called using the selected operation.
7. The calculated result is displayed.
8. The user can choose whether to perform another calculation or exit.

### Example

```text
Enter the first number: 25

+
-
*
/

Enter the operation: *
Enter the second number: 4

25.0 * 4.0 = 100.0

Do you want to continue? (y/n): n
```

---

## 💻 Code Concepts Used

* Python Functions
* Functions with return values
* Function parameters
* Dictionaries
* Storing functions inside dictionaries
* `for` loops
* `while` loops
* Conditional statements
* Boolean variables
* User input
* Floating-point numbers
* Importing custom modules

---

## ⚙️ Calculator Functions

Separate functions are created for each mathematical operation.

```python
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2
```

These functions are then stored inside a dictionary:

```python
operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
```

This allows the program to dynamically select and execute the correct function based on the user's chosen operator.

For example:

```python
answer = operation[op_symbol](n1, n2)
```

---

## 📂 Project Structure

```text
Day-010-Calculator/
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

* Create functions that return values
* Use multiple functions for different operations
* Store functions inside Python dictionaries
* Call functions dynamically using dictionary keys
* Work with `float` values
* Use loops to run a program repeatedly
* Take mathematical input from users
* Combine functions, dictionaries, loops, and conditions
* Build a functional command-line calculator

---

## 🔮 Future Improvements

Some improvements that can be added to the calculator include:

* Continue calculations using the previous result
* Handle division by zero
* Handle invalid operator input
* Add additional operations such as `%`, power, and square root
* Add input validation for non-numeric values

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
