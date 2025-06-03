# 🏠 Homework Assignment

## 🚀 Goal

You're going to build **a smart command-line assistant** that performs multiple tasks using:

* Functions (basic and advanced)
* Type hints
* Decorators
* File handling
* Error handling
* `while` and `for` loops
* Dictionaries, recursion, lambda, and context managers

---

## ✅ Task Overview

You will create a Python script called `smart_assistant.py` that includes the following features:

---

### 1️⃣ **Login System with File Storage**

**Real-world agent logic:** Remember users between sessions.

✅ Features:

* Store users in a file (`users.txt`) as `email:password`
* Use a function to register and save new users
* Use a function to login existing users
* Validate email and password using conditions and try-except
* Use a `with` block to read/write the file safely
* Create and use a **custom error** like `InvalidLoginError`

💡 Bonus:

* Use `contextlib.contextmanager` to manage file operations

---

### 2️⃣ **Mini Data Assistant**

**Real-world agent logic:** Help users analyze text data.

✅ Features:

* Ask the user for a `.txt` filename and read the content
* Show:

  * Number of lines
  * Number of words
  * Number of characters
  * Top 5 most common words using dictionary

💡 Use:

* Functions with `return`
* Try-except for file not found
* Print results using formatted strings

---

### 3️⃣ **Table Generator with Logging**

**Real-world logic:** AI helps generate patterns or data and logs it.

✅ Features:

* User inputs a number (like 5)
* Your function generates a multiplication table and returns it
* Save the table to a file like `table-5.txt`
* Use `try-finally` to ensure file closes/log prints

---

### 4️⃣ **Recursive Menu Loop with AI Feel**

**Real-world logic:** Agent keeps asking for tasks until user exits.

✅ Features:

* Use a `while True` loop to present options like:

  * 1: Login
  * 2: Register
  * 3: Analyze text file
  * 4: Generate table
  * 5: Exit
* Wrap menu in try-finally (to say goodbye!)
* Add error messages for invalid input using `raise`

---

### 5️⃣ **Lambda Tools**

**Real-world logic:** Tiny agent tools for quick calculations.

✅ Create these:

* `add`, `subtract`, `multiply`, `divide`
* `is_even`
* `square`
* `reverse_string`
* `word_count`
* `filter_even_numbers`
* `is_palindrome`
* `calculate_area`
* Add type hints to all lambda tools for clarity and better code quality.
* Use these tools in your menu or assistant tools section.

---

## 🧠 Bonus Challenges (Optional)

* Add `asyncio` to fake a loading animation when logging in
* Create your own decorator for logging every function call
* Save all user activities in a `log.txt` file

---

## 💾 Files to Create

* `smart_assistant.py` (main code)
* `users.txt` (auto-generated)
* `log.txt` (optional)
* `table-<number>.txt` (auto-generated)

---

## 🧪 Skills You Will Practice

* Real world coding logic
* Function design and testing
* File and error handling
* Working with strings and loops
* Writing clean and reusable code like an AI system
