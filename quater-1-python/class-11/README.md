# 🐍 Python Class 11 – 29 June 2025

<div style="display:flex;align-items:base-line;gap:20px;">
    <b>Quiz Prepration: </b>
    <a target="_blank" href="https://colab.research.google.com/drive/1f1J0op53l_P8RBwQPTSt_w5-vDdIQ4lX?usp=sharing">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
    </a>  
</div>

<div style="display:flex;align-items:base-line;gap:20px;">
    <b>Object-Oriented Programming (OOP): </b>
    <a target="_blank" href="https://colab.research.google.com/drive/1uZeW8VB997neRDOp2JhgRn27HmmlCx11?usp=sharing">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
    </a>
</div>

---

## 📘 Topics Covered

---

### 🧠 Quiz Preparation

- Discussed tricky MCQs
- Review past class topics (Classes 1–10)
- Practice logic-based and syntax-based questions

---

## 🧪 Type Checking with `mypy`

### ✅ What is `mypy`?

- A tool to **check for type errors** in Python code (without running it)
- Helps catch bugs early

### 🧾 Example

```python
def add(x: int, y: int) -> int:
    return x + y

# Save this in a file, then run:
# mypy filename.py
```

---

## 🧵 Interning of Strings

* Python stores some strings in a shared space (memory optimization)
* Interned strings with same value share the same memory

```python
a = "hello"
b = "hello"
print(a is b)  # True (same memory)
```

---

## 🧹 Garbage Collection in Python

* Unused memory is **automatically freed**
* Python uses **reference counting** + garbage collector

---

## 📤 Pass by Value vs Pass by Reference

### ✅ Pass by Value

* Used with immutable types (e.g., `int`, `str`)
* Function gets a **copy**, not original

### ✅ Pass by Reference

* Used with mutable types (e.g., `list`, `dict`)
* Function can **modify original object**

```python
def update(x):
    x.append(5)

nums = [1, 2]
update(nums)
print(nums)  # [1, 2, 5]
```

---

## 🧱 Object-Oriented Programming (OOP)

---

Python supports Object-Oriented Programming. Let’s explore it with real examples:

---

### 🏗️ Constructor (`__init__`)

A **constructor** is a special method that runs automatically when an object is created using a class. We define it with `__init__()`.

```python
class House:
    def __init__(self):
        self.address = "XYZ 123"
        self.number_of_rooms = 4

h1 = House()
print(h1.address)  # XYZ 123
```

---

### 🎯 Constructor with Parameters

```python
class House:
    def __init__(self, addrs): 
        self.address = addrs
        self.number_of_rooms = 4

h1 = House("A29")
print(h1.address)  # A29
```

---

### 📦 Attributes and Methods

* **Attributes** are variables inside a class.
* **Methods** are functions inside a class.

```python
class House:
    def __init__(self, addrs): 
        self.address = addrs
        self.number_of_rooms = 4

    def ring_bell(self):
        print("Ding dong!")

h1 = House("A29")
print(h1.address)
h1.ring_bell()  # Ding dong!
```

---

### 🏛️ 4 Pillars of OOP 

1. **Inheritance**
2. **Polymorphism**
3. **Encapsulation**
4. **Abstraction**

---

### 🧬 Inheritance

Inheritance allows a class (child) to reuse the attributes and methods of another class (parent).

```python
class Appartment(House):
    def __init__(self, addrs, flat_number):
        super().__init__(addrs)  # calls House's constructor
        self.flat_number = flat_number

aprt1 = Appartment("ABC", 23)
print(aprt1.address)         # ABC
print(aprt1.flat_number)     # 23
print(aprt1.number_of_rooms) # 4
```

🔑 `super()` is used to call the parent class’s `__init__()` without writing the class name manually.

---

### 🌐 Multiple Inheritance

A class can inherit from **more than one parent class**.

```python
class House1:
    def __init__(self, color):
        self.color = color

class Appartment(House, House1):
    def __init__(self, addrs, flat_number):
        House.__init__(self, addrs)
        House1.__init__(self, 'red')
        self.flat_number = flat_number

aprt1 = Appartment("ABC", 23)
print(aprt1.address)         # ABC
print(aprt1.flat_number)     # 23
print(aprt1.number_of_rooms) # 4
print(aprt1.color)           # red
```

---

## 📝 Homework

- Try creating a class with a constructor, attributes, and methods
- Implement an example of inheritance and multiple inheritance
- Make notes on the 4 pillars of OOP (we will cover them in detail later)
- Revise for the upcoming quiz: step 01 to 09

---
