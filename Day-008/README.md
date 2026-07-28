# 🔐 Day 8 - Caesar Cipher

## 📌 Project Overview

This is the **Day 8** project from the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.

The **Caesar Cipher** is a text encryption and decryption program. It shifts each letter in a message by a user-defined number of positions in the alphabet.

The program allows users to **encode** a message into encrypted text or **decode** an encrypted message back into its original form.

---

## 🚀 How It Works

1. The program displays the Caesar Cipher logo.
2. The user chooses whether to:

   * `encode` a message
   * `decode` a message
3. The user enters the message.
4. The user enters a shift number.
5. The program shifts each letter accordingly.
6. Spaces, numbers, and special characters remain unchanged.
7. The user can choose to run the program again or exit.

### Example - Encoding

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode

Type your message:
hello world

Type the shift number:
5

Here is the encoded result: mjqqt btwqi
```

### Example - Decoding

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
decode

Type your message:
mjqqt btwqi

Type the shift number:
5

Here is the decoded result: hello world
```

---

## 💻 Code Concepts Used

* Python Functions
* Function parameters and arguments
* `for` loops
* `while` loops
* Conditional statements
* Lists
* String manipulation
* List indexing
* Modulo operator (`%`)
* Boolean variables
* User input
* Importing custom modules

---

## 🔑 Caesar Cipher Logic

For **encoding**, the program moves each letter forward in the alphabet.

```text
a → b → c → d
```

For example, with a shift of `3`:

```text
a → d
b → e
c → f
```

For **decoding**, the program moves each letter backward by the specified shift amount.

The modulo operator `%` ensures that the shifting wraps around the alphabet correctly.

```text
z + 1 → a
```

---

## 📂 Project Structure

```text
Day-08-Caesar-Cipher/
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

* Create functions with multiple parameters
* Pass arguments using keyword arguments
* Encrypt and decrypt text
* Work with alphabet indexing
* Use the modulo operator for circular shifting
* Preserve spaces and special characters
* Use `while` loops to repeat a program
* Import and use custom Python modules
* Combine multiple Python concepts into one complete program

---

## 📚 Course

**100 Days of Code: The Complete Python Pro Bootcamp**
by Dr. Angela Yu (Udemy)

---

## 👨‍💻 Author

**Chaitanya Mahale**

GitHub: https://github.com/ChaitanyaM45
