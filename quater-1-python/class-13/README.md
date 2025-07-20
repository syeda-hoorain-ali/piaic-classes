# 🐍 Python Class 13 – 20 July 2025

[![Python Class 13](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/17FIczsa-zfChWqio5T6daI9ZHOMw_fhe?usp=sharing)

---

## 📘 Topics Covered

### 🧱 Object-Oriented Programming (OOP) in Python

---

### ✅ Attributes & Methods

- **Attributes** are variables that belong to an object.
- **Methods** are functions defined inside a class that operate on its attributes.

---

### 🏛️ 4 Pillars of OOP

#### 1️⃣ Inheritance
Allows a class to reuse code from another class (parent → child).

```python
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

car = Car()
car.start()  # from Vehicle
car.honk()   # from Car
```

---

#### 2️⃣ Polymorphism (Method Overriding)

Same method name behaves differently in different classes.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Dog()
a.speak()  # Dog barks
```

---

#### 3️⃣ Encapsulation

Hiding internal data using private variables and providing access via methods.

```python
class Account:
    def __init__(self):
        self.__balance = 0  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

---

#### 4️⃣ Abstraction (Abstract Classes & Methods)

Forcing subclasses to implement required methods using `abc` module.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Bark")
```

---

## 📝 Homework

### ✅ Learn

1. **Getters and Setters**

   * Access and update private attributes safely.
   * Learn using `@property` and `@<name>.setter`.

2. **Abstract Properties**

   * Create abstract attributes using `@abstractproperty` or `@property + @abstractmethod`.

---

### 🏗️ Project: University Management System

📁 Link: [Download Project Instructions](https://drive.google.com/file/d/1xFUYd6GW5U0tSQSN8_xi5QvFKrlxYfF0/view)

Build a mini management system using OOP concepts

* Use abstract base class for `Person`
* Create `Student` and `Instructor` classes
* Add methods for adding courses, showing info, etc.
* Use encapsulation for private data
* Use inheritance and polymorphism where needed

---
