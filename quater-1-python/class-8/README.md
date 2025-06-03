# 🐍 Python Class 8 – 31 May 2025

<div style="display:flex;align-items:base-line;gap:35.5px;">
  <b>Functions: </b>

  <a target="_blank" href="https://colab.research.google.com/drive/1FTQCLa57BJchmIHBXwHDarBiuXxzb62O?usp=sharing">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
</div>

<div style="display:flex;align-items:base-line;gap:20px;">
  <b>Error handling: </b>

  <a target="_blank" href="https://colab.research.google.com/drive/1j0RDBrjVdBbAnmHv882YuYgvi3JJbzVW?usp=sharing">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
</div>



---

## 🔁 Recap of Previous Function Topics

* **Default Functions**: Functions with pre-defined parameter values
* **Return Functions**: Return a value using `return`
* **Non-return Functions**: Just do something, don’t return anything
* **Required Parameters**: You must pass a value
* **Optional Parameters**: Already have a default value
* **Positional Arguments**: Based on position
* **Keyword Arguments**: Use parameter names when calling
* **Unlimited Arguments (`*args`)**: For any number of values
* **Unlimited Keyword Arguments (`**kwargs`)**: For any number of named values
* **Lambda Function**: Short anonymous function
* **Type Hints**: Show expected types of parameters and return values
* **Decorator**: Modify behavior of functions without changing their code

---

## 🖨️ `print()` Function Advanced

```python
print("Hello", "World", sep="-", end="!", flush=True)
```

* `sep` → Separator between values (default is space)
* `end` → What to print at the end (default is newline `\n`)
* `flush` → Forces the output to be written immediately

---

## 🧱 Object Basics

* **Attributes** → Data/values stored in the object
* **Methods** → Actions/functions the object can perform

```python
name = "Qasim"
print(name.upper())  # upper is a method
print(name.isalpha())  # isalpha is a method
```

---

## 📄 Docstring

Multi-line string that describes what a function/class/module does.

```python
def greet():
    """
    This function prints a greeting message.
    """
    print("Hello!")
```

---

## ⚡ Lambda with Types

```python
from typing import Callable
add: Callable[[int, int], int] = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

---

## 🌱 Generators

Functions that yield values one by one using `yield`.

```python
from typing import Iterable

def count_up_to(n: int) -> Iterable[int]:
    for i in range(1, n+1):
        yield i

num3 = count_up_to(4):
print(next(num))
print(next(num))
print(list(num))
```

---

## 🔁 Recursion

A function that calls itself.

```python
def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)
```

---

## 📂 File Handling

### Reading a File

```python
with open("file.txt", "r") as file:
    print(file.read())
```

### Writing to a File

```python
with open("file.txt", "w") as file:
    file.write("Hello!")
```

---

## 🔄 With Block + `contextmanager`

### With Block
The with statement is used to open files safely. It automatically closes the file for you.

```python
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)
```

### Contexntmanager
You can also use `@contextmanager` to make your own `with` block.

```python
from contextlib import contextmanager

db = {}
@contextmanager
def connect_db():
    print("Data base connected")
    yield db
    print("Data connection close")
```

---

## ⚡ Sync vs Async

* **Synchronous**: Code runs line by line
* **Asynchronous**: Code can run while waiting (like downloads or APIs)

## Asynchronous

```python
import sleep

async def say_hello():
    time.sleep(3)
    print("Hello")

async def main():
    await say_hello()
```


### asyncio Library

```python
import asyncio

async def say_hello():
    print("Hello")

async def main():
    await asyncio.gather(say_hello(), say_hello())

asyncio.run(main())
```

---

## ❗ Error Handling

### Types of Errors

* **Logical Errors**:  Code runs but gives wrong output
* **Development Errors**: Bugs during writing code
* **Runtime Errors**: Crash while the program is running

### `try-except-finally`
A `try-except-finally` block lets you handle errors gracefully. Code in `try` runs first; if an error occurs, `except` handles it. The `finally` block always runs, whether or not there was an error.

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This runs no matter what")
```

### Multiple `except` Blocks
You can handle different types of errors with multiple `except` blocks.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e: # For every kind of error
    print(f"An unexpected error occurred: {e}")
```

### `raise` error

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

check_age(-1)  # Will raise error
```

### Custom error class
Define your own error types by creating a class that inherits from `Exception`.

```python
class LoginError(Exception):
    pass

def login(user):
    if user != "admin":
        raise LoginError("Only admin can login.")

login("guest")  # Will raise LoginError

```

---

## 📚 Tools Mentioned

* [`uml` diagram](https://www.google.com/search?q=uml+diagram) → Visual programming
* [`planttext.com`](https://planttext.com) → AI content
* [`notebooklm`](https://notebooklm.google) → Smart research assistant by Google

---



<font size=5 color="lightgreen"><b>📝 Homework Assignments </b> </font>

<font size=3>

- 1️⃣ **Login System with File Storage**
- 2️⃣ **Mini Data Assistant**
- 3️⃣ **Table Generator with Logging**
- 4️⃣ **Recursive Menu Loop with AI Feel**
- 5️⃣ **Lambda Tools**


For complete details, please refer to the [Homework Assignments](https://github.com/syeda-hoorain-ali/piaic-classes/blob/main/quater-1-python/class-7/HOMEWORK-ASSIGNMENTS.md)

</font>