# 🏛️ Day 016 - Object-Oriented Programming (OOP)

## 📌 Overview

Day 016 of the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu focused on learning the fundamentals of **Object-Oriented Programming (OOP)** in Python.

Instead of building a standalone project, this day introduced the core concepts of OOP, including **classes, objects, attributes, methods, and Python packages**. These concepts are essential for writing organized, reusable, and scalable code.

---

## 📖 Topics Covered

- Why Object-Oriented Programming (OOP) is needed
- Understanding Classes and Objects
- Creating Objects
- Object Attributes
- Object Methods
- Accessing Attributes and Methods
- Modifying Object Attributes
- Calling Methods
- Installing Python Packages using PyPI
- Importing and using external libraries

---

## 🧠 What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **objects**.

An object is an instance of a class and contains:

- **Attributes** → Data or properties
- **Methods** → Functions that define the object's behavior

For example:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")
```

Creating an object:

```python
my_dog = Dog("Buddy")
my_dog.bark()
```

---

## 📚 Classes vs Objects

### Class

A **class** is a blueprint used to create objects.

```python
class Car:
    pass
```

### Object

An **object** is an instance of a class.

```python
my_car = Car()
```

---

## 🏷️ Attributes

Attributes store information about an object.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Accessing an attribute:

```python
print(student.name)
```

Modifying an attribute:

```python
student.name = "Chaitanya"
```

---

## ⚙️ Methods

Methods define what an object can do.

```python
class Student:
    def greet(self):
        print("Hello!")
```

Calling a method:

```python
student.greet()
```

---

## 📦 Python Packages (PyPI)

I also learned how to install external Python packages using **PyPI (Python Package Index)**.

Example:

```bash
pip install prettytable
```

Importing the package:

```python
from prettytable import PrettyTable
```

Using external packages allows developers to build applications more efficiently without writing everything from scratch.

---

## 💻 Practice

The exercises for this day focused on:

- Creating classes
- Creating objects
- Accessing attributes
- Calling methods
- Modifying object attributes
- Installing and importing Python packages

I did **not complete the Coffee Machine OOP project** on this day, as it is covered later in the course.

---

## 📂 Project Structure

```text
Day-016-Object-Oriented-Programming/
└── README.md
```

Optional:

```text
Day-016-Object-Oriented-Programming/
│── README.md
└── practice.py
```

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- PyPI
- pip

---

## 🎯 Learning Outcome

By completing Day 016, I learned how to:

- Understand why Object-Oriented Programming is useful
- Create classes and objects
- Work with attributes and methods
- Access and modify object attributes
- Call object methods
- Organize code using OOP principles
- Install external Python packages using PyPI
- Import and use third-party libraries

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**  
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45