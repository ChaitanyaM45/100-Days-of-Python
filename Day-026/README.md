# 📡 Day 026 - NATO Phonetic Alphabet

## 📌 Project Overview

Day 26 focuses on **Pandas, CSV data, dictionaries, and list comprehensions** by building a simple **NATO Phonetic Alphabet Converter**.

The program reads the NATO phonetic alphabet from a CSV file and converts each letter of a user-entered word into its corresponding NATO phonetic code.

For example:

```text
Input:  HELLO

Output: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

---

## 🧠 How It Works

The program follows these steps:

1. Load the NATO phonetic alphabet CSV file using Pandas.
2. Create a dictionary where:

   * The letter is the **key**.
   * The NATO code is the **value**.
3. Ask the user to enter a word.
4. Convert the input to uppercase.
5. Use a list comprehension to convert every letter into its NATO code.
6. Print the resulting list.

---

## 📄 NATO Phonetic Alphabet

The CSV file contains two columns:

```text
letter,code
A,Alfa
B,Bravo
C,Charlie
D,Delta
E,Echo
...
Z,Zulu
```

The complete alphabet used by the program includes:

| Letter | Code     |
| ------ | -------- |
| A      | Alfa     |
| B      | Bravo    |
| C      | Charlie  |
| D      | Delta    |
| E      | Echo     |
| F      | Foxtrot  |
| G      | Golf     |
| H      | Hotel    |
| I      | India    |
| J      | Juliet   |
| K      | Kilo     |
| L      | Lima     |
| M      | Mike     |
| N      | November |
| O      | Oscar    |
| P      | Papa     |
| Q      | Quebec   |
| R      | Romeo    |
| S      | Sierra   |
| T      | Tango    |
| U      | Uniform  |
| V      | Victor   |
| W      | Whiskey  |
| X      | X-ray    |
| Y      | Yankee   |
| Z      | Zulu     |

---

## 🐼 Reading the CSV With Pandas

The NATO alphabet is stored in `nato_phonetic_alphabet.csv`.

It is loaded using:

```python
import pandas as pd

df = pd.read_csv("./Day-026/nato_phonetic_alphabet.csv")
```

This creates a Pandas DataFrame containing the letters and their corresponding NATO codes.

---

## 📖 Creating a Dictionary With Dictionary Comprehension

The DataFrame is converted into a dictionary using:

```python
new_dict = {
    row.letter: row.code
    for (index, row) in df.iterrows()
}
```

This produces a dictionary similar to:

```python
{
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    ...
}
```

This makes it easy to look up the NATO code for any letter.

---

## ⌨️ Taking User Input

The program asks the user to enter a word:

```python
name = input("Enter Word: ").upper()
```

The `.upper()` method ensures that lowercase input can also be converted into uppercase letters.

For example:

```text
hello → HELLO
python → PYTHON
```

---

## 🔄 List Comprehension

The most important part of the program is the list comprehension:

```python
output_list = [new_dict[letter] for letter in name]
```

It loops through every letter in the input word and retrieves its corresponding NATO code from the dictionary.

For example:

```text
PYTHON
```

becomes:

```text
Papa
Yankee
Tango
Hotel
Oscar
November
```

---

## 🖥️ Example

### Input

```text
Enter Word: HELLO
```

### Output

```python
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

Another example:

### Input

```text
Enter Word: PYTHON
```

### Output

```python
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```

---

# 🧠 Code Concepts Used

## Pandas

* Importing Pandas
* `pd.read_csv()`
* DataFrames
* `iterrows()`

## Dictionaries

* Creating dictionaries
* Key-value pairs
* Dictionary lookup
* Dictionary comprehension

## List Comprehension

Used to efficiently convert each input letter:

```python
output_list = [new_dict[letter] for letter in name]
```

## String Methods

* `input()`
* `.upper()`

## Loops

The list comprehension internally iterates through every character in the entered word.

---

# 📂 Project Structure

```text
Day-026/
│
├── main.py
├── nato_phonetic_alphabet.csv
└── README.md
```

### File Description

| File                         | Purpose                                       |
| ---------------------------- | --------------------------------------------- |
| `main.py`                    | Contains the NATO phonetic alphabet converter |
| `nato_phonetic_alphabet.csv` | Stores the letter-to-code mapping             |
| `README.md`                  | Project documentation                         |

---

# 🛠️ Technologies Used

* **Python**
* **Pandas**
* **CSV**
* **Dictionaries**
* **List Comprehension**

---

# 🎯 Learning Outcome

Through this project, I learned how to combine **Pandas and Python data structures** to process information stored in a CSV file.

Key concepts practiced:

* Reading CSV files using Pandas
* Iterating through DataFrame rows
* Creating dictionaries from tabular data
* Dictionary comprehension
* List comprehension
* Dictionary key-value lookup
* String manipulation
* Converting user input into processed output

---

# 🚀 Future Improvements

Possible improvements include:

* Handle numbers and special characters gracefully
* Display the NATO codes as a formatted sentence instead of a Python list
* Add error handling for characters not present in the dictionary
* Allow the user to convert multiple words without restarting the program
* Add an option to decode NATO phonetic words back into letters

---

# ✅ Project Status

**Completed ✔️**

* [x] Read NATO alphabet from CSV
* [x] Create dictionary using DataFrame rows
* [x] Accept user input
* [x] Convert input to uppercase
* [x] Use list comprehension
* [x] Generate NATO phonetic codes
* [x] Display converted output

---

# 📚 Course

Part of **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
