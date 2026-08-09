# 🎨 Day 018 - Hirst Spot Painting

## 📌 Project Overview

This is the **Day 018** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Hirst Spot Painting** project uses Python's **Turtle graphics** to create a colorful dot painting inspired by the artwork of Damien Hirst.

The program generates a grid of randomly colored dots using a predefined RGB color palette. It also uses the `colorgram` library to extract colors from an image.

This project focuses on Turtle graphics, RGB colors, loops, randomization, and Python libraries.

---

## 🎨 How It Works

1. A Turtle object is created.
2. The screen color mode is set to support RGB values.
3. A predefined list of RGB colors is used.
4. The Turtle moves to the starting position.
5. The program draws **100 colored dots**.
6. Each dot receives a randomly selected color.
7. After every 10 dots, the Turtle moves to the next row.
8. The result is a colorful 10 × 10 dot painting.

---

## 🖼️ Example

The program generates a painting similar to:

```text
●  ●  ●  ●  ●  ●  ●  ●  ●  ●

●  ●  ●  ●  ●  ●  ●  ●  ●  ●

●  ●  ●  ●  ●  ●  ●  ●  ●  ●

●  ●  ●  ●  ●  ●  ●  ●  ●  ●

        ...

        10 × 10 dots
```

Each dot is assigned a random color from the selected palette.

---

## 🌈 Color Extraction

The project also introduces the `colorgram` library, which can be used to extract colors from an image.

Example:

```python
colors = colorgram.extract("hirst.jpg", 25)
```

The RGB values can then be stored in a list and used by Turtle.

In my implementation, the extracted RGB colors were stored in a `colors` list and used to randomly select the color of each dot.

---

## 💻 Code Concepts Used

- Python Turtle graphics
- RGB colors
- `random.choice()`
- `for` loops
- Conditional statements
- Modulo operator (`%`)
- Lists
- Tuples
- Functions from Python libraries
- `penup()` and `pendown()`
- Turtle movement
- External Python packages

---

## 🐢 Turtle Functions Used

Some important Turtle functions used in this project include:

```python
tim.dot()
tim.forward()
tim.setheading()
tim.penup()
tim.pendown()
tim.hideturtle()
```

The program uses `tim.dot(30, random.choice(colors))` to draw a 30-pixel dot with a randomly selected color.

---

## 🔄 Creating the Grid

The program uses the modulo operator to move to a new row after every 10 dots:

```python
if i % 10 == 0:
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)
    tim.pendown()
```

This creates the **10 × 10 grid** of dots.

---

## 📂 Project Structure

```text
Day-018-Hirst-Spot-Painting/
│── main.py
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- Turtle Graphics
- Random module
- Colorgram

---

## 🎯 Learning Outcome

By completing this project, I learned how to:

- Use Python's Turtle graphics library
- Work with RGB color values
- Generate random colors
- Use loops to create graphical patterns
- Control Turtle movement
- Use the modulo operator to create rows
- Work with tuples and lists
- Extract colors from images using `colorgram`
- Use external Python libraries
- Create artwork programmatically

---

## 🔮 Future Improvements

Some improvements that can be added include:

- Allow the user to select the image used for color extraction
- Generate different painting sizes
- Change the dot size and spacing
- Add more color palettes
- Randomize the position of dots
- Create different geometric patterns
- Add a GUI to customize the painting

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**  
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45