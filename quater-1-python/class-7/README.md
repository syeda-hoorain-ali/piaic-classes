# 🐍 Python Class 7 – 25 May 2025

---

## 🔁 Callback Functions

A **callback function** is a function passed as an argument to another function — it is "called back" later.

### Example:

```python
def greet(name):
    print(f"Hello, {name}!")

def call_func(func):
    func("Ali")

call_func(greet)  # Output: Hello, Ali!
```

---

## 🎀 Decorators

A **decorator** lets you change or extend a function's behavior **without modifying it**.

### Example:

```python
def decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@decorator
def say_hi():
    print("Hi!")

say_hi()
```

🧠 Output:

```bash
Before the function runs  
Hi!  
After the function runs
```

---

## 🔁 For Loop

Used to run code **a fixed number of times** (like through a list or range).

### Example:

```python
for i in range(1, 6):
    print(i)
```

---

## 🔄 List Comprehension

A short way to create a list from another list or range.

### Example:

```python
squares = [x*x for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

---

## 🔁 While Loop

Runs the code **while the condition is true**.

### Example:

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

---

## 🎮 Number Guessing Game (Basic Idea)
We built this game in class:

* Store a secret number
* Let the player guess until correct
* Give hints like “too high” or “too low”

---

## 📝 Homework Assignments

---

### 1️⃣ Build a Login System with a Decorator

* Use a dictionary as a fake database:

  ```python
  users = {"user@example.com": "1234"}
  ```

* Create a `auth_checker` decorator that checks if the user is logged in before calling a function.
* Ask for email and password.
* If email exists and password matches → print `"Logged in"` and call a welcome function (decorated with `@login_required`).
* Else → print `"Incorrect email or password"`.


---

### 2️⃣ For Loop: Student List with Serial Numbers

```text
1. Okasha  
2. Ali  
3. Hamzah  
4. Abdul Aziz  
```

---

### 3️⃣ Table of 2 (using `range`)

```text
2 x 1 = 2  
2 x 2 = 4  
...  
2 x 10 = 20
```

---

### 4️⃣ Add More to Guessing Game

* Validate input: only numbers allowed
* Limit number of tries
* Add difficulty levels (easy = 5 tries, hard = 3 tries)
* Celebrate when guessed correctly 🎉
