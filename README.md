# Learn-Python

# 🐍 Python Fundamentals Repository

This repository contains a collection of Python scripts designed to teach core programming concepts. The files range from basic syntax to Object-Oriented Programming (OOP) and file handling.

## 📂 Repository Contents

### 1. Basics & Syntax
* **`hello.py`**
    * **Core Concepts:** Basic printing, single and multi-line comments, and variable assignment.
    * **Data Types:** Covers Strings (`str`), Integers (`int`), Floats (`float`), and Booleans (`bool`).
    * **Modules:** Demonstrates importing standard libraries like `math` (for `pi` and `sqrt`) and `random`.

### 2. Control Flow & Logic
* **`loops_and_conditions.py`**
    * **Conditionals:** Usage of `if`, `elif`, and `else` statements for decision making.
    * **Loops:**
        * `for` loops iterating over lists and ranges.
        * `while` loops with counters.
    * **Flow Control:** Implementation of `continue` to skip iterations and `else` blocks within loops.

### 3. Data Structures
* **`lists.py`**
    * **Lists:** Creating lists and using methods like `.append()`, `.insert()`, `.remove()`, `.pop()`, `.reverse()`, and `.sort()`.
    * **Dictionaries:** Creating key-value pairs, accessing data safely with `.get()`, updating values, and removing keys.
    * **Tuples:** Immutable sequences and indexing.
    * **Sets:** Handling unique collections and adding items.

### 4. Functions
* **`functions.py`**
    * **Definitions:** Creating functions using `def`, handling parameters, and returning values.
    * **Arguments:** Using default argument values (e.g., `width=10`).
    * **Lambdas:** Introduction to anonymous functions (e.g., `lambda x: x ** x`).

### 5. Object-Oriented Programming (OOP)
* **`classes.py`**
    * **Classes & Objects:** Defining classes (e.g., `Cat`), constructors (`__init__`), and methods.
    * **Encapsulation:** Using protected attributes (like `_balance`) and getter/setter patterns in an `Account` class.
    * **Inheritance:** Creating child classes (e.g., `Mammal` inheriting from `Animal`) and using `super()`.
    * **Polymorphism:** Demonstrating method overriding and abstract concepts with `Shape`, `Circle`, and `Square`.

### 6. File Handling & Exceptions
* **`io.py`**
    * **File I/O:** Reading (`r`), writing (`w`), and appending (`a`) to text files.
    * **Context Managers:** Using the `with` statement to automatically close files.
    * **Error Handling:** Implementing `try` and `except` blocks to catch errors like `FileNotFoundError`.

---

## 🚀 How to Run

Ensure you have Python installed. You can run any of the scripts using your terminal or command prompt:

```bash
# Example: Run the basics script
python hello.py

# Example: Run the OOP examples
python classes.py
