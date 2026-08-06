# 🧠 Day 017 - Quiz Game (Object-Oriented Programming)

## 📌 Project Overview

This is the **Day 017** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Quiz Game** is a command-line True/False quiz application built using **Object-Oriented Programming (OOP)** principles.

The program loads a collection of questions, presents them one by one to the user, checks each answer, keeps track of the score, and displays the final result after all questions have been answered.

This project demonstrates how to organize a Python application into multiple classes and modules.

---

## 🚀 How It Works

1. Quiz questions are loaded from a separate data file.
2. Each question is converted into a `Question` object.
3. All question objects are stored in a question bank.
4. The `QuizBrain` class controls the quiz.
5. Questions are displayed one by one.
6. The user's answer is checked.
7. The score is updated after every question.
8. When all questions have been answered, the final score is displayed.

---

## 🕹️ Example

```text
Q1. A slug's blood is green. (True/False):
True

You Got it Right!
The correct answer was True.
Your Score: 1/1

Q2. The loudest animal is the African Elephant. (True/False):
False

You Got it Right!
The correct answer was False.
Your Score: 2/2

...

You have completed the quiz.
Your Final Score: 12/12
```

---

## 🏛️ Object-Oriented Design

The application is divided into multiple classes, each with a specific responsibility.

### 📄 Question Class

The `Question` class represents a single quiz question.

Each object stores:

- Question text
- Correct answer

Example:

```python
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
```

---

### 🧠 QuizBrain Class

The `QuizBrain` class manages the quiz by:

- Displaying questions
- Checking answers
- Updating the score
- Tracking question progress
- Determining when the quiz ends

---

### 📚 Question Data

The quiz questions are stored separately inside `data.py`.

Each question is represented as a dictionary:

```python
{
    "text": "A slug's blood is green.",
    "answer": "True"
}
```

Separating the data from the program logic makes the application easier to maintain and extend.

---

## 💻 Code Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Attributes
- Methods
- Importing custom modules
- Lists
- Dictionaries
- `while` loops
- Conditional statements
- User input
- Score tracking
- Program flow control

---

## 📂 Project Structure

```text
Day-017-Quiz-Game/
│── main.py
│── question_model.py
│── quiz_brain.py
│── data.py
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

## 🎯 Learning Outcome

By completing this project, I learned how to:

- Create classes and objects
- Design programs using Object-Oriented Programming
- Organize code into multiple Python modules
- Store and access object attributes
- Create methods inside classes
- Build objects from external data
- Track user progress and score
- Separate data, business logic, and application flow
- Build a modular command-line quiz application

---

## 🔮 Future Improvements

Some improvements that can be added include:

- Load questions from an online API
- Shuffle questions randomly
- Add multiple difficulty levels
- Support multiple-choice questions
- Display colored output
- Add a timer for each question
- Save high scores in a file
- Build a graphical user interface (GUI)

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**  
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45