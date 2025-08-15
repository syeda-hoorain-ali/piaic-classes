# 🐍 Python Class 9 – 15 June 2025

<a target="_blank" href="https://colab.research.google.com/drive/1mSNrsoXx6WFD1qwJ68HBl7fJIX4GIvf0?usp=sharing">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

---

## 📦 Modules in Python

### ✅ Custom Modules
You can create your own `.py` files (e.g. `auth.py`) and import them.

```python
# auth.py
def login():
    print("User logged in")

# main.py
from auth import login
login()
````

---

### ✅ Built-in Modules

Python already includes useful modules like `random`.

```python
import random
print(random.randint(1, 10))  # Random integer between 1–10
```

---

### ✅ External Modules

These are installed using pip. Example: `colorama`

```bash
pip install colorama
```

```python
from colorama import Fore, Style
print(Fore.RED + "This is red text" + Style.RESET_ALL)
```

---

## 📁 File Handling

### ✅ With Block (Safe Open & Close)

```python
with open("file.txt", "r") as file:
    print(file.read())
```

---

### ✅ Write, Append, Read Modes

```python
# Write to file (overwrite)
with open("file.txt", "w") as file:
    file.write("Hello\n")

# Append to file
with open("file.txt", "a") as file:
    file.write("Another line\n")

# Read file
with open("file.txt", "r") as file:
    print(file.read())
```

---

### ✅ Cursor Control

```python
with open("file.txt", "r") as file:
	print(file.tell())      # Current position
	file.seek(10)           # Move to 10 index
	print(file.read())
```

---

### ✅ r+ vs w+ Mode

| Mode | Description                                            |
| ---- | ------------------------------------------------------ |
| `r+` | Read + Write. File **must exist**.                     |
| `w+` | Write + Read. Overwrites existing file or creates new. |

---

## 🧱 Tuples

* Tuples are immutable (cannot be changed).
* Faster and memory-efficient compared to lists.
* Use `()` instead of `[]`.

```python
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  # banana
```

📚 [All tuple methods → w3schools](https://www.w3schools.com/python/python_tuples.asp)

---

## 🌿 Sets

* Unordered and do not allow duplicates.
* Use `{}` instead of `[]`.

```python
my_set = {"apple", "banana", "apple"}
print(my_set)  # Output: {'apple', 'banana'}
```

📚 [All set methods → w3schools](https://www.w3schools.com/python/python_sets.asp)

---

## 📝 Homework Assignment

---

### ✅ Tasks

1. **Understand CSV Format**

   * Learn what a `.csv` file is (comma-separated values)
   * Example:

     ```
     name,contact
     Hoorain,03001234567
     ```

2. **Contact Manager Tool (CLI)**

   * Create a Python script with two options:

     * `Read contacts from CSV`
     * `Add new contact to CSV`
   * Ask user for name and contact number
   * Save it to `contacts.csv`

3. **Use `inquirer` Module**

   * Show user a list of options like:

     * Add Contact
     * View All
     * Exit  
       📦 Install with:

   ```bash
   pip install inquirer
   ```

4. **Learn**

   * What are **sets** and **tuples**
   * When to use which one
   * Practice methods from [W3Schools](https://www.w3schools.com/python/python_sets.asp)

---

### 🧠 Bonus Challenge (Optional)

* Add validation (don’t allow duplicate names using sets)
* Add colors using `colorama` for better UI
* **Build something new using your own creativity** — apply what you’ve learned so far in a fun or useful way (e.g., a quiz app, task manager, or mini chatbot)
