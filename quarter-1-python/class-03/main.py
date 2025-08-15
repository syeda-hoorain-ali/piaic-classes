
# ==========================================
# 1. Introduction to Control Flow
# ==========================================

print("=== Control Flow Introduction ===")
print("Control flow determines how your program makes decisions")
print("It allows your code to take different paths based on conditions")

# ==========================================
# 2. Basic if Statement
# ==========================================

print("\n=== Basic if Statement ===")

age = 18
print(f"Age: {age}")

if age >= 18:
    print("You are an adult")
    print("You can vote!")

# Another example
temperature = 25
print(f"\nTemperature: {temperature}°C")

if temperature > 30:
    print("It's hot outside!")

# ==========================================
# 3. if-else Statement
# ==========================================

print("\n=== if-else Statement ===")

temperature = 25
print(f"Temperature: {temperature}°C")

if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot")

# Another example
score = 75
print(f"\nScore: {score}")

if score >= 70:
    print("You passed!")
else:
    print("You need to study more")

# ==========================================
# 4. if-elif-else Statement
# ==========================================

print("\n=== if-elif-else Statement ===")

score = 85
print(f"Score: {score}")

if score >= 90:
    print("Grade: A")
    print("Excellent work!")
elif score >= 80:
    print("Grade: B")
    print("Good job!")
elif score >= 70:
    print("Grade: C")
    print("You passed")
elif score >= 60:
    print("Grade: D")
    print("You need improvement")
else:
    print("Grade: F")
    print("You failed")

# ==========================================
# 5. Multiple Conditions with Logical Operators
# ==========================================

print("\n=== Multiple Conditions ===")

age = 25
has_license = True
print(f"Age: {age}, Has License: {has_license}")

if age >= 18 and has_license:
    print("You can drive!")
elif age >= 18 and not has_license:
    print("You need to get a license first")
else:
    print("You're too young to drive")

# ==========================================
# 6. User Input with input() Function
# ==========================================

print("\n=== User Input ===")

# Basic input
name = input("What is your name? ")
print(f"Hello, {name}!")

# Input with type conversion
age_input = input("How old are you? ")
age = int(age_input)  # Convert string to integer
print(f"You are {age} years old")

# Input for calculations
num1_input = input("Enter first number: ")
num2_input = input("Enter second number: ")
num1 = int(num1_input)
num2 = int(num2_input)
sum_result = num1 + num2
print(f"{num1} + {num2} = {sum_result}")

# ==========================================
# 7. Interactive Program Examples
# ==========================================

print("\n=== Interactive Examples ===")

# Example 1: Simple Calculator
print("Simple Calculator")
operation = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Error: Invalid operation"

print(f"Result: {result}")

# ==========================================
# 8. Temperature Converter
# ==========================================

print("\n=== Temperature Converter ===")

temp_input = input("Enter temperature in Celsius: ")
celsius = float(temp_input)

if celsius < -273.15:
    print("Error: Temperature below absolute zero!")
else:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
    
    # Add some weather commentary
    if fahrenheit > 100:
        print("That's very hot!")
    elif fahrenheit > 80:
        print("That's warm")
    elif fahrenheit > 60:
        print("That's pleasant")
    elif fahrenheit > 32:
        print("That's cool")
    else:
        print("That's cold!")

# ==========================================
# 9. Grade Checker with Input
# ==========================================

print("\n=== Grade Checker ===")

score_input = input("Enter your test score (0-100): ")
score = float(score_input)

if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100")
elif score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Good job!")
elif score >= 70:
    print("Grade: C - You passed")
elif score >= 60:
    print("Grade: D - Needs improvement")
else:
    print("Grade: F - You failed")

# ==========================================
# 10. Simple Quiz Program
# ==========================================

print("\n=== Simple Quiz ===")

print("Question: What is the capital of France?")
print("A) London")
print("B) Paris")
print("C) Berlin")
print("D) Madrid")

answer = input("Enter your answer (A, B, C, or D): ").upper()

if answer == "B":
    print("Correct! Paris is the capital of France.")
elif answer in ["A", "C", "D"]:
    print("Incorrect! The correct answer is B) Paris")
else:
    print("Invalid input! Please enter A, B, C, or D")

# ==========================================
# 11. Nested if Statements
# ==========================================

print("\n=== Nested if Statements ===")

age = 25
income = 50000
print(f"Age: {age}, Income: ${income}")

if age >= 18:
    print("You are an adult")
    if income >= 50000:
        print("You have a good income")
        if income >= 100000:
            print("You are wealthy!")
        else:
            print("You are doing well")
    else:
        print("You might want to look for better opportunities")
else:
    print("You are a minor")

# ==========================================
# 12. Practice Exercises
# ==========================================

print("\n=== Practice Exercises ===")

# Exercise 1: Check if a number is positive, negative, or zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

# Exercise 2: Check if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Exercise 3: Simple password checker
password = input("Enter password: ")
if len(password) >= 8:
    print("Password is strong")
else:
    print("Password is too short")

# ==========================================
# 13. Next Steps Preview
# ==========================================

print("\n=== What's Next? ===")
print("In the next class, we'll learn about:")
print("- Built-in functions (len, type, id, dir)")
print("- String methods (isdigit, isnumeric)")
print("- Lists and indexing")
print("- List methods (append, pop, insert, remove)")

print("\n🎉 Excellent! You've mastered control flow and user interaction!")
