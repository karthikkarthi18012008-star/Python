# Python Exception Handling

A collection of Python programs demonstrating how to handle runtime errors using exception handling. These examples cover different exception handling techniques, including handling specific exceptions, multiple exceptions, the `finally` block, the `else` block, and file handling with exceptions.

---

## 📚 Concepts Covered

- Basic `try` and `except`
- Handling `ZeroDivisionError`
- Handling `ValueError`
- Handling `NameError`
- Handling `FileNotFoundError`
- Using multiple `except` blocks
- Using the generic `Exception` class
- `try` + `except` + `else`
- `try` + `except` + `finally`
- `try` + `except` + `else` + `finally`
- Exception handling during file operations
- Closing files safely using `finally`

---

## 📂 Program Overview

### 1. Basic Exception Handling
- Prevents program crashes caused by division by zero.
- Demonstrates handling `ZeroDivisionError`.

### 2. Handling Multiple Exceptions
- Handles both:
  - `ZeroDivisionError`
  - `ValueError`
- Ensures the program responds appropriately to different types of errors.

### 3. Using the `finally` Block
- Demonstrates that the `finally` block always executes.
- Useful for resource cleanup such as closing files or database connections.

### 4. Handling `NameError`
- Shows how Python raises a `NameError` when an undefined variable is accessed.
- Captures the exception object and displays the error message.

### 5. Exception Object (`as`)
- Demonstrates storing exception details using:
  ```python
  except Exception as ex:
  ```
- Prints the actual error message for easier debugging.

### 6. Generic Exception Handling
- Uses the base `Exception` class to catch unexpected runtime errors.

### 7. Using the `else` Block
- Executes only if no exception occurs.
- Keeps success logic separate from error handling.

### 8. Using `else` and `finally`
- Demonstrates complete exception handling flow:
  - `try`
  - `except`
  - `else`
  - `finally`

### 9. File Handling with Exceptions
- Opens and reads a file safely.
- Handles:
  - Missing files (`FileNotFoundError`)
  - Other unexpected errors
- Ensures the file is properly closed using the `finally` block.

---

## 📌 Sample Topics Demonstrated

- Safe division
- User input validation
- File handling errors
- Runtime error handling
- Cleanup using `finally`
- Exception hierarchy
- Generic exception handling

---

## 💡 Learning Outcomes

After completing these examples, you will understand how to:

- Prevent program crashes caused by runtime errors.
- Handle different types of exceptions effectively.
- Write cleaner and more robust Python programs.
- Use `else` and `finally` appropriately.
- Perform safe file operations.
- Debug programs using exception messages.




## 📖 Key Python Keywords

- `try`
- `except`
- `else`
- `finally`
- `raise`
- `Exception`
- `ZeroDivisionError`
- `ValueError`
- `NameError`
- `FileNotFoundError`

 
### 2. NumPy Operations
- Creating NumPy arrays.
- Performing arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Finding statistical values:
  - Minimum
  - Maximum
  - Sum
  - Mean
  - Standard deviation
- Array slicing.
- Reshaping arrays.

# Pandas
### 3. Pandas Operations
- Creating Pandas Series.
- Creating DataFrames.
- Creating DataFrames using NumPy arrays.
- Handling missing data:
  - Filling missing values.
  - Removing rows with missing values.
 
  # Python Conditional Statements Programs

## 📌 Description
This repository contains Python programs demonstrating the use of **conditional statements** such as:

- Nested `if-else` statements
- `if-elif-else` statements
- Decision-making logic in Python

The programs solve real-world problems like checking leap years, performing arithmetic operations, and calculating ticket prices based on conditions.

---

## 🛠️ Technologies Used

- Python 3.x

---

## 📂 Programs Included

### 4. Leap Year Checker (Nested If-Else)

### 📖 Problem Statement
Determine whether a given year is a leap year using nested conditional statements.

### 🔹 Logic Used
A year is a leap year if:
- It is divisible by 4
- If divisible by 100, it must also be divisible by 400


---

# 5. Simple Calculator (If-Elif-Else)

### 📖 Problem Statement
Perform arithmetic operations based on the user's selected operation.

Supported operations:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)


### Features
- Handles invalid operations
- Prevents division by zero errors

---

# 6. Ticket Price Calculator (Nested If-Else)

### 📖 Problem Statement
Determine ticket price based on:
- Age
- Student status

### Pricing Rules

| Age Group | Student | Price |
|-----------|---------|-------|
| Below 5 | Any | Free |
| 5 - 12 | Any | $10 |
| 13 - 17 | Yes | $12 |
| 13 - 17 | No | $15 |
| 18 - 64 | Yes | $18 |
| 18 - 64 | No | $20 |
| Above 64 | Any | $25 |


#7. Sum of Natural Numbers and Prime Numbers in Python

## Description
This project contains Python programs to:
1. Calculate the sum of the first **n natural numbers** using:
   - While loop
   - For loop
2. Display all **prime numbers between 1 and 100** using a for loop.

The project demonstrates the use of loops, conditional statements, and basic Python logic.

---

## Programs Included

### 1. Sum of First n Natural Numbers

#### Using While Loop
- Takes a positive integer `n` from the user.
- Uses a while loop to add numbers from `1` to `n`.
- Displays the total sum.


---

### 2. Prime Numbers Between 1 and 100

- Uses nested for loops to check whether a number is prime.
- A prime number is a number greater than 1 that has only two factors:
  - 1
  - Itself


---

## Concepts Used

- Python Input and Output
- Variables
- While Loop
- For Loop
- Nested Loops
- Conditional Statements (`if-else`)
- `range()` Function
- Prime Number Logic

# Python List Operations

A beginner-friendly Python program demonstrating various **list operations** and **list manipulation techniques**. This project covers list creation, slicing, comprehensions, sorting, matrix operations, zipping, reversing, rotating, and more.

## 📚 Topics Covered

- List creation using `range()`
- Accessing list elements
- List slicing
- List comprehension
- Filtering lists
- Random number generation
- Sorting lists (Ascending & Descending)
- Removing duplicate elements
- Counting total and unique elements
- Nested lists (Matrix)
- Matrix transpose
- Flattening a nested list
- List manipulation (`del`, `insert`)
- Zipping two lists
- List reversal
- List rotation
- List intersection

---

## 🛠️ Technologies Used

- Python 3.x
- `random` module

---

## 📂 Features

### 1. List Creation
Creates a list of numbers from 0 to 19 using `range()`.

### 2. Accessing Elements
Demonstrates how to access list elements using indexing.

### 3. List Slicing
Shows different slicing techniques:
- First five elements
- Last five elements
- Middle portion of the list

### 4. List Comprehension
Creates a new list containing the squares of all elements.

### 5. Filtering Lists
Filters only even numbers using list comprehension.

### 6. Random Number Operations
- Generates random integers
- Sorts them in ascending order
- Sorts them in descending order
- Removes duplicate values
- Counts total and unique elements

### 7. Matrix Operations
Creates a 3×3 matrix and:
- Accesses specific elements
- Computes the transpose

### 8. Flattening Nested Lists
Converts a 2D list into a 1D list.

### 9. List Manipulation
Demonstrates:
- Deleting elements
- Inserting new elements

### 10. List Zipping
Combines two lists into pairs using `zip()`.

### 11. List Reversal
Reverses a list using slicing.

### 12. List Rotation
Rotates a list to the left by a specified number of positions.

Example:

```
Original:
[1, 2, 3, 4, 5]

Rotate by 2:

[3, 4, 5, 1, 2]
```

### 13. List Intersection
Finds common elements between two lists.

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/python-list-operations.git
```

2. Navigate to the project directory

```bash
cd python-list-operations
```

3. Run the program

```bash
python list_operations.py
```

---

## 📖 Sample Concepts Demonstrated

- Indexing
- Slicing
- List Comprehension
- Conditional Comprehension
- Functions
- Nested Lists
- Matrix Operations
- Built-in Functions
- `zip()`
- `sorted()`
- `set()`
- `range()`

---

## 🎯 Learning Outcome

After completing this project, you will understand:

- How Python lists work
- Different ways to manipulate lists
- Working with nested lists (matrices)
- Common interview-oriented list operations
- Writing reusable Python functions

---

## 👨‍💻 Author

**Karthik T**

If you found this project helpful, consider giving it a ⭐ on GitHub!

## Python Tuples

### Concepts Covered
- Tuple creation
- Indexing and slicing
- Nested tuples
- Concatenation and repetition
- `count()` and `index()` methods
- Tuple unpacking
- List ↔ Tuple conversion
- Tuples with strings, dictionaries, and sets
- Nested tuple iteration

### Learning Outcomes
- Understand tuple operations and immutability.
- Access and manipulate tuple elements.
- Convert between tuples, lists, strings, and sets.
- Use tuples as dictionary keys.
- Iterate through nested tuples effectively.














