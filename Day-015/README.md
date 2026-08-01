# ☕ Day 015 - Coffee Machine

## 📌 Project Overview

This is the **Day 015** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Coffee Machine** is a command-line simulation of a real coffee vending machine. Users can choose from different coffee options, insert coins, and receive their drink if sufficient resources and payment are available.

The machine also keeps track of its available resources and earned money, making this project a great exercise in combining functions, dictionaries, loops, and program logic.

---

## 🚀 How It Works

1. The user selects a drink:
   - `espresso`
   - `latte`
   - `cappuccino`
2. The machine checks whether enough ingredients are available.
3. If resources are sufficient, the user is prompted to insert coins.
4. The machine calculates the total amount inserted.
5. If enough money is provided:
   - Change is returned (if any).
   - The required ingredients are deducted from the available resources.
   - The selected coffee is served.
6. The user can also:
   - Type `report` to view the remaining resources and money earned.
   - Type `off` to turn off the machine.

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
What would you like? (espresso/latte/cappuccino): latte

Please Insert Coins:

how many quarters?: 10
how many dimes?: 0
how many nickel?: 0
how many pennies?: 0

Here is $0.0 dollars in change.
Here is your latte coffee ☕
```

Viewing the report:

```text
What would you like? (espresso/latte/cappuccino): report

Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

---

## ⚙️ Features

- Multiple coffee options
- Resource availability check
- Coin-based payment system
- Change calculation
- Resource deduction after each purchase
- Machine report
- Machine shutdown option

---

## 💻 Code Concepts Used

- Python Dictionaries
- Nested Dictionaries
- Functions
- Function parameters
- Return values
- Global variables
- `while` loops
- Conditional statements
- Arithmetic operations
- User input
- Resource management
- Program state management

---

## 🧠 Program Logic

### Resource Check

Before preparing a drink, the machine verifies that enough ingredients are available.

```python
if is_resource_sufficient(drink["ingredients"]):
```

If an ingredient is insufficient, the machine informs the user.

---

### Coin Processing

The machine accepts four types of coins:

- Quarter ($0.25)
- Dime ($0.10)
- Nickel ($0.05)
- Penny ($0.01)

The total amount inserted is calculated before processing the transaction.

---

### Transaction Processing

If the inserted amount is greater than or equal to the drink price:

- Payment is accepted.
- Change is returned.
- The coffee is prepared.

Otherwise:

```text
Sorry that's not enough money. Money refunded.
```

---

### Making Coffee

Once payment is successful:

- Required ingredients are deducted from the machine resources.
- The selected coffee is served.

---

## 📂 Project Structure

```text
Day-015-Coffee-Machine/
│── main.py
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3

---

## 🎯 Learning Outcome

By completing this project, I learned how to:

- Work with nested dictionaries
- Build modular programs using multiple functions
- Manage resources dynamically
- Simulate a real-world vending machine
- Process monetary transactions
- Calculate and return change
- Update program state after each transaction
- Use loops to keep a program running continuously
- Organize code into reusable functions
- Combine multiple Python concepts into a practical application

---

## 🔮 Future Improvements

Some improvements that can be added include:

- Add input validation for invalid drink names
- Allow users to refill machine resources
- Track total number of drinks sold
- Improve money tracking using a profit variable
- Add additional beverages
- Create a graphical user interface (GUI)
- Store sales data in a file or database

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**  
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45