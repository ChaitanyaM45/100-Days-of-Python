# 🧠 Day 034 - Quizzler: True or False Quiz App

## 📌 Project Overview

Day 34 focuses on building an interactive **True or False Quiz Application** using Python, Tkinter, object-oriented programming, and an external API.

The project, called **Quizzler**, fetches 10 questions from the Open Trivia Database API and displays them in a graphical user interface.

Users answer each question by clicking the True or False buttons. The application checks the answer, updates the score, and provides visual feedback.

---

## 🎯 Features

* Fetches 10 True/False questions from an online API
* Uses the Open Trivia Database API
* Displays questions in a Tkinter GUI
* Provides True and False buttons with images
* Checks answers and tracks the user's score
* Displays green feedback for correct answers
* Displays red feedback for incorrect answers
* Automatically moves to the next question after a short delay
* Displays a completion message when all questions have been answered

---

## 🌐 1. Fetching Quiz Questions

The `data.py` file sends a GET request to the Open Trivia Database API.

```python
import requests

parameter = {
    "amount": 10,
    "type": "boolean",
}

data = requests.get(
    url="https://opentdb.com/api.php",
    params=parameter
)

question_data = data.json()["results"]
```

### How It Works

* `amount: 10` requests 10 questions.
* `type: boolean` requests True/False questions.
* `requests.get()` sends the API request.
* `.json()` converts the response into a Python dictionary.
* `["results"]` extracts the list of questions.

The resulting question data is used to create the quiz question objects.

---

## 🧩 2. Question Model

The `question_model.py` file defines the `Question` class.

```python
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

### Concepts Used

* Classes and objects
* Constructors using `__init__()`
* Instance attributes
* Storing question text and correct answers

Each question is represented as an object containing its text and correct answer.

---

## 🧠 3. Quiz Brain

The `quiz_brain.py` file contains the `QuizBrain` class, which manages the quiz logic.

### Main Responsibilities

* Track the current question number
* Store the user's score
* Check whether questions remain
* Retrieve the next question
* Check whether an answer is correct
* Increase the score for correct answers

### Checking Remaining Questions

```python
def still_has_questions(self):
    return self.question_number < len(self.question_list)
```

This method returns `True` while there are questions remaining.

### Getting the Next Question

```python
def next_question(self):
    self.current_question = (
        self.question_list[self.question_number]
    )

    self.question_number += 1

    q_text = html.unescape(
        self.current_question.text
    )

    return f"Q.{self.question_number}: {q_text}"
```

The method retrieves the next question, updates the question number, and returns the question text.

The `html.unescape()` function converts HTML entities into readable characters.

### Checking the Answer

```python
def check_answer(self, user_answer):
    correct_answer = self.current_question.answer

    if user_answer.lower() == correct_answer.lower():
        self.score += 1
        return True
    else:
        return False
```

The user's answer is compared with the correct answer.

* If the answer is correct, the score increases.
* If the answer is incorrect, the score remains unchanged.
* The method returns `True` or `False` to the GUI.

---

## 🖥️ 4. Graphical User Interface

The `ui.py` file contains the `QuizInterface` class, which builds the application using Tkinter.

### Interface Components

| Component      | Purpose                        |
| -------------- | ------------------------------ |
| Tkinter Window | Main application window        |
| Score Label    | Displays the current score     |
| Canvas         | Displays quiz questions        |
| True Button    | Submits a True answer          |
| False Button   | Submits a False answer         |
| Images         | Provide visual button controls |

### Answer Buttons

The True and False buttons call their respective methods:

```python
self.correct_button = Button(
    image=correct,
    command=self.true_pressed
)

self.wrong_button = Button(
    image=wrong,
    command=self.false_pressed
)
```

When clicked, each button checks the selected answer and sends the result to the feedback method.

### Visual Feedback

```python
def give_feedback(self, is_right):
    if is_right:
        self.canvas.config(bg="green")
    else:
        self.canvas.config(bg="red")

    self.window.after(
        1000,
        self.get_next_question
    )
```

* Green background indicates a correct answer.
* Red background indicates an incorrect answer.
* After one second, the next question is displayed.

### End of Quiz

When no questions remain, the application displays:

```text
You have reached question limit.
```

---

## 🔄 Application Workflow

```text
Start Application
       ↓
Fetch 10 Questions from API
       ↓
Create Question Objects
       ↓
Initialize QuizBrain
       ↓
Display Tkinter Interface
       ↓
Display Next Question
       ↓
User Clicks True or False
       ↓
Check Answer
       ↓
Update Score if Correct
       ↓
Show Green or Red Feedback
       ↓
Wait 1 Second
       ↓
More Questions?
    ↙        ↘
   Yes        No
    ↓          ↓
Next       Show Completion
Question      Message
```

---

## 🧠 Code Concepts Used

### Python & OOP

* Classes and objects
* Constructors
* Instance attributes
* Methods
* Object interaction
* Type hints

### API & JSON

* `requests.get()`
* API parameters
* HTTP responses
* JSON parsing
* Extracting nested dictionary values

### Tkinter GUI

* `Tk()`
* `Label`
* `Canvas`
* `Button`
* `PhotoImage`
* `.grid()`
* `.config()`
* `.itemconfig()`
* `.after()`
* `mainloop()`

### Python Fundamentals

* Lists
* Dictionaries
* Conditional statements
* Functions and methods
* String comparison
* Boolean values
* HTML entity decoding
* Score tracking

---

## 📂 Project Structure

```text
Day-034/
│
├── images/
│   ├── false.png
│   └── true.png
│
├── data.py
├── main.py
├── question_model.py
├── quiz_brain.py
├── ui.py
└── README.md
```

### File Description

| File / Folder       | Purpose                                                   |
| ------------------- | --------------------------------------------------------- |
| `data.py`           | Fetches quiz questions from the Open Trivia Database API  |
| `main.py`           | Creates the question bank and initializes the quiz        |
| `question_model.py` | Defines the `Question` class                              |
| `quiz_brain.py`     | Handles question progression and answer checking          |
| `ui.py`             | Builds the Tkinter interface and handles user interaction |
| `images/true.png`   | Image for the True button                                 |
| `images/false.png`  | Image for the False button                                |
| `README.md`         | Project documentation                                     |

---

## 🛠️ Technologies Used

* Python
* Tkinter
* Requests
* Open Trivia Database API
* JSON
* Object-Oriented Programming

---

## ▶️ How to Run

1. Make sure Python is installed.

2. Install the Requests library:

   ```bash
   pip install requests
   ```

3. Ensure the project files and `images` folder are in the correct locations.

4. Run the application from the project root:

   ```bash
   python main.py
   ```

5. Answer the questions using the True and False buttons.

---

## 🎯 Learning Outcomes

Through Day 34, I learned how to:

* Fetch data from an external API
* Work with JSON responses
* Create Python classes and objects
* Separate application logic from the user interface
* Build a graphical quiz application using Tkinter
* Handle button clicks and user input
* Track a user's score
* Provide visual feedback
* Use Tkinter's `after()` method to schedule actions
* Decode HTML entities in API-provided text

---

## 🚀 Future Improvements

* Add a restart quiz button
* Display the final score and percentage
* Disable answer buttons after one answer is submitted
* Add loading and API error handling
* Allow users to select question categories and difficulty
* Improve the completion screen
* Add a progress indicator
* Randomize questions and answer order

---

## 🔐 Notes

* An internet connection is required to fetch questions from the API.
* The API may return HTML-encoded characters, which are handled using `html.unescape()`.
* Ensure that the image paths match the actual project structure.
* The current program displays a completion message but does not yet provide a dedicated restart feature.

---

## ✅ Project Status

**Completed ✔️**

* [x] Fetch quiz questions from API
* [x] Create Question class
* [x] Implement QuizBrain
* [x] Build Tkinter interface
* [x] Add True and False buttons
* [x] Check user answers
* [x] Track score
* [x] Display visual feedback
* [x] Move between questions
* [x] Display quiz completion message

---

## 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
