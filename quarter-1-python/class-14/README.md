# 🐍 Python Class 14 – 27 July 2025 *(Last Class)*

[![Python Class 14](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TBqqfuiEwrFnLufvLRQzk3rWMp2zFmBP?usp=sharing)

---

## 📘 Topics Covered

### 🧱 Object-Oriented Programming: Final Concepts

---

### 🧮 Class Variables

- A variable shared by **all instances** of a class.
- Defined **outside `__init__`**, directly under the class.

```python
class Student:
    quarter = 1  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Hoorain")
s2 = Student("Hamzah")
print(s1.quarter)  # 1
print(s2.quarter)  # 1
```

---

### 🧰 Class Methods

* Methods that belong to the class **not just the object**
* Use the `@classmethod` decorator
* First parameter is always `cls` (class)

```python
class Student:
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    @classmethod
    def show_total(cls):
        print(f"Total students: {cls.total_students}")

Student("Hamzah")
Student("Hoorain")
Student.show_total()  # Total students: 2
```

---

## 📝 Final Quiz

* MCQs were based on:
  * Data types, operators, and control flow
  * Modules and functions
  * Errors and exceptions
  * File handling and decorators

---

## 🎓 Congratulations!

This was your **last Python class** of the quarter. You’ve learned:

* Programming fundamentals
* Real-world Python use
* Object-oriented design
* Tools like `mypy`, `colorama`, `inquirer`

---

## 🏁 What’s Next?

* Build mini projects (like your **University Management System**)
* Review all 14 class notes
* Keep practicing daily
* Explore topics like:

  * AI agents (OpenAI SDK)
  * APIs and automation
  * Python + web with FastAPI


