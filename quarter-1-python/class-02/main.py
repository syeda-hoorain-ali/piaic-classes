
# ==========================================
# 1. Variables
# ==========================================

# Creating variables
message = "Hello, World!!!"
print(message)

# Variable with same name (reassignment)
name = "Okasha Aijaz"
print("Original name:", name)
name = "John Doe"
print("Updated name:", name)

# ==========================================
# 2. Data Types
# ==========================================

# 1) String
name = "Okasha Aijaz"
print("Name:", name)
print("Type:", type(name))

# 2) Integer
age = 21
print("Age:", age)
print("Type:", type(age))

# 3) Boolean
isMarried = False
print("Married:", isMarried)
print("Type:", type(isMarried))

# 4) Float
height = 5.8
print("Height:", height)
print("Type:", type(height))

# ==========================================
# 3. String Concatenation
# ==========================================

firstName = "Okasha"
lastName = "Aijaz"
fullName = firstName + " " + lastName
print("Full name (concatenation):", fullName)

# ==========================================
# 4. f-strings (Formatted String Literals)
# ==========================================

firstName = "Okasha"
lastName = "Aijaz"
fullName = f"Hello {firstName} {lastName}"
print("Full name (f-string):", fullName)

# More f-string examples
_name = "Okasha"
name = "Okasha Aijaz"
age = 21
print(f"Hello {name}, you are {age} years old.")

# ==========================================
# 5. Checking Data Types and Memory
# ==========================================

name = "Okasha Aijaz"
print("Type of name:", type(name))
print("Memory location of name:", id(name))

# ==========================================
# 6. Operators
# ==========================================

print("\n=== Arithmetic Operators ===")
# + - * / % // **
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Modulus (remainder): {a} % {b} = {a % b}")
print(f"Floor division: {a} // {b} = {a // b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Order of operations example
print(f"\nOrder of operations: 10 + {b} - 2 * {a} + 10")
print(f"Result: {10 + b - 2 * a + 10}")
#     10 + 3    -20  + 10
#     10 + 3        -10
#        3

# ==========================================
# 7. Comparison Operators
# ==========================================

print("\n=== Comparison Operators ===")
# == != > < >= <=
a = 10
b = 10

print(f"a = {a}, b = {b}")
print(f"Equal to (==): {a} == {b} = {a == b}")
print(f"Not equal to (!=): {a} != {b} = {a != b}")
print(f"Greater than (>): {a} > {b} = {a > b}")
print(f"Less than (<): {a} < {b} = {a < b}")
print(f"Greater than or equal (>=): {a} >= {b} = {a >= b}")
print(f"Less than or equal (<=): {a} <= {b} = {a <= b}")

# ==========================================
# 8. Logical Operators
# ==========================================

print("\n=== Logical Operators ===")
x = True
y = False

print(f"x = {x}, y = {y}")
print(f"AND (x and y): {x and y}")
print(f"OR (x or y): {x or y}")
print(f"NOT (not x): {not x}")
print(f"NOT (not y): {not y}")

# ==========================================
# 9. Assignment Operators
# ==========================================

print("\n=== Assignment Operators ===")
num = 5
print(f"Original num: {num}")

num += 3  # Same as num = num + 3
print(f"After num += 3: {num}")

num -= 2  # Same as num = num - 2
print(f"After num -= 2: {num}")

num *= 4  # Same as num = num * 4
print(f"After num *= 4: {num}")

# ==========================================
# 10. Practice Exercises
# ==========================================

print("\n=== Practice Exercises ===")

# Exercise 1: Create variables for your information
my_name = "Your Name"
my_age = 25
my_city = "Your City"
my_hobby = "Your Hobby"

# Exercise 2: Use f-strings to create a personal introduction
introduction = f"Hi! I'm {my_name}, I'm {my_age} years old, I live in {my_city}, and I love {my_hobby}."
print("Personal Introduction:", introduction)

# Exercise 3: Calculate and display some math
num1 = 15
num2 = 7
print(f"Math operations with {num1} and {num2}:")
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
print(f"Remainder: {num1 % num2}")

