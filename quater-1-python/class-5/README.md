# 🐍 Python Class 5 – 11 May 2025


## ✅ Function Basics

A **function** is a reusable block of code that runs only when you call it.

### 🔧 Function Syntax

```python
def function_name(param1, param2, param3 = default_value):
    # Code inside the function
    return something  # optional

# Calling the function
function_name(arg1, arg2)
function_name(arg1, arg2, arg3)
```

---

### 🧠 Key Terms (Easy Definitions)

- **Parameter:** A variable inside the function that accepts input
- **Argument:** The actual value you pass when calling the function
- **Positional Argument:** Values passed in the correct order (1st to 1st, 2nd to 2nd...)
- **Keyword Argument:** You mention the parameter name like `name="Ali"` while calling the function
- **Default Parameter:** If no value is given, a default value is used (`param="default"`)
- **Return Keyword:** Sends the result *back* to where the function was called


## ⚡ Lambda Functions

A **lambda function** is a short, one-line anonymous function.

```python
# Normal function
def add(x, y):
    return x + y

# Lambda version
add = lambda x, y: x + y

print(add(3, 5))  # Output: 8
```


## 📝 Mini Assignments
**Food Calories Calculator**  
Write lambda functions for:  
* Squaring a number
* Multiplying two numbers
* Checking if a number is positive

