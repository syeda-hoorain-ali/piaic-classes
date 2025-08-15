# 🐍 Python Class 6 – 18 May 2025

---

## 🔁 Recap: Functions

A function lets you group code and use it again.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Hoorain"))  # Output: Hello, Hoorain!
```

---

## ➕ Add Types in Functions (Type Hints)

Type hints help you understand what type of data the function uses and returns.

```python
def add(x: int, y: int) -> int:
    return x + y

print(add(3, 5))  # Output: 8
```

---

## 📦 Dictionaries (key-value pairs)

### 💡 What is a Dictionary?

A dictionary stores data using **keys** and **values**.  
Think of it like a real-world dictionary:
**Word (key)** ➝ **Definition (value)**

```python
student = {
    "name": "Ali",
    "age": 13
}
```

---

### 🔑 Accessing and Using Dictionary

| Syntax                       | Description                              | Example                       |
| ---------------------------- | ---------------------------------------- | ----------------------------- |
| `dict["key"]`                | Get value using key                      | `student["name"]` → `"Ali"`   |
| `dict["key"] = new_value`    | Change or add a new value                | `student["age"] = 14`         |
| `dict.get("key", "default")` | Get value safely with a default fallback | `student.get("grade", "N/A")` |
| `dict.keys()`                | Get all keys                             | `student.keys()`              |
| `dict.values()`              | Get all values                           | `student.values()`            |
| `dict.pop("key")`            | Remove a key and return its value        | `student.pop("age")`          |

---

### 📘 Example

```python
info = {
    "name": "Ali",
    "course": "Python"
}

print(info["name"])              # Ali
info["course"] = "Gen-AI"        # update value
print(info.get("age", "N/A"))    # N/A
print(info.keys())               # dict_keys(['name', 'course'])
print(info.values())             # dict_values(['Hoorain', 'Gen-AI'])
info.pop("name")                 # remove key 'name'
print(info)                      # {'course': 'Gen-AI'}
```

---

## 🏠 Homework Assignments

### 1️⃣ Get Gemini API Key

* Open [Google Colab](https://colab.research.google.com/)
* Go to  `🔐 Secrets` (in sidebar or tools)
* Get your **Gemini API Key**
* Save it for future use

### 2️⃣ Learn Decorators

A **decorator** is a function that changes another function’s behavior.