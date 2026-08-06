# ☕ Day 016 - Coffee Machine (Object-Oriented Programming)

## 📌 Project Overview

This is the **Day 016** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Coffee Machine (OOP Version)** is a command-line coffee vending machine built using **Object-Oriented Programming (OOP)** principles. Unlike the procedural version from Day 15, this implementation separates responsibilities into multiple classes, making the code cleaner, modular, reusable, and easier to maintain.

The application allows users to order different types of coffee, checks resource availability, processes payments, prepares the selected drink, and generates reports.

---

## 🚀 How It Works

1. The program displays the available coffee options.
2. The user selects one of the following drinks:
   - Espresso
   - Latte
   - Cappuccino
3. The machine checks whether enough ingredients are available.
4. If resources are sufficient, the user inserts coins.
5. The payment is verified.
6. If the payment is successful:
   - Resources are deducted.
   - The selected coffee is prepared.
7. Additional commands:
   - `report` → Displays available resources and current profit.
   - `off` → Turns off the coffee machine.

---

## ☕ Coffee Menu

| Drink | Water | Milk | Coffee | Cost |
|-------|-------:|------:|--------:|-----:|
| Espresso | 50 ml | 0 ml | 18 g | $1.50 |
| Latte | 200 ml | 150 ml | 24 g | $2.50 |
| Cappuccino | 250 ml | 100 ml | 24 g | $3.00 |

---

## 🕹️ Example

```text
What would you like? (latte/espresso/cappuccino): latte

Please insert coins.

How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0

Here is $0.00 in change.
Here is your latte ☕ Enjoy!
```

Generating a report:

```text
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.50
```

---

## 🏛️ Object-Oriented Design

The project is divided into multiple classes, each with a single responsibility.

### ☕ Menu

Responsible for:

- Displaying available drinks
- Finding drinks from the menu

Example:

```python
menu = Menu()
options = menu.get_items()
drink = menu.find_drink(choice)
```

---

### 🥛 CoffeeMaker

Responsible for:

- Managing machine resources
- Checking ingredient availability
- Preparing coffee
- Displaying resource reports

Example:

```python
coffee_maker.is_resource_sufficient(drink)
coffee_maker.make_coffee(drink)
```

---

### 💰 MoneyMachine

Responsible for:

- Accepting coins
- Processing payments
- Tracking profit
- Printing money reports

Example:

```python
money_machine.make_payment(drink.cost)
money_machine.report()
```

---

### 🍵 MenuItem

Represents a single coffee item and stores information such as:

- Name
- Water required
- Milk required
- Coffee required
- Cost

---

## 💻 Code Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects
- Attributes
- Methods
- Object Composition
- Importing Custom Modules
- Functions
- Conditional Statements
- `while` loops
- User Input
- Program Flow Control

---

## 📂 Project Structure

```text
Day-016-Coffee-Machine-OOP/
│── main.py
│── menu.py
│── coffee_maker.py
│── money_machine.py
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

## 🎯 Learning Outcome

By completing this project, I learned how to:

- Apply Object-Oriented Programming principles
- Create and use classes and objects
- Organize code into multiple modules
- Import custom Python modules
- Use object methods and attributes
- Separate program responsibilities into different classes
- Build modular and maintainable applications
- Simulate a real-world coffee vending machine using OOP

---

## 🔮 Future Improvements

Some enhancements that can be added include:

- Add more coffee varieties
- Allow users to refill ingredients
- Store transaction history in a file
- Add a graphical user interface (GUI)
- Save resources and profit between sessions
- Improve input validation and error handling

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**  
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45