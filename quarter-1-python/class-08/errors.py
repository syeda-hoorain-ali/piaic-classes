
#* ================================================== *#
#* ================= Runtime Errors ================= *#
#* ================================================== *#

# name = "Qasim"
# print(Name)

#* ================================================== *#

# while True:
# print("Hello")

#* ================================================== *#

# int("Hello")

#* ================================================== *#

# l1 = ['a', 'b', 'c']
# print(l1[10])

#* ================================================== *#

# print(8/0)

#* ================================================== *#

# print("Line 1")
# print("Line 2")
# print("Line 3")
# print(8 / 0)    # Error in Line 4
# print("Line 5") # This line will not run due to error
# print("Line 6") # This line will not run due to error


#* ================================================== *#
#* =============== try-except-finally =============== *#
#* ================================================== *#


# print("Line 1")
# print("Line 2")
# print("Line 3")

# try:
#     print(8 / 0) # Line 4, where error could come
# except ZeroDivisionError:
#     print("You cannot divide by zero")

# # Remaing logic
# print("Line 5")
# print("Line 6")


#* ================================================== *#

# try:
#     print(8/1)
# except ZeroDivisionError:
#     print("You cannot divide by zero")

# l1 = ['a', 'b', 'c']


#* ================================================== *#

# try:
#     print(7/1)
#     print(l1[10])
# except ZeroDivisionError: # You handled ZeroDivisionError but not IndexError
#     print("You cannot divide by zero")


#* ================================================== *#


# l1 = ['a', 'b', 'c']

# try:
#     print(7/1)
#     print(l1[10])
# except (ZeroDivisionError, IndexError): # multiple error classes
#     print("You cannot divide by zero")

# # Issue: weather its ZeroDivisionError or IndexError, it will always show "You cannot divide by zero"


#* ================================================== *#
#* ================ Multiple excepts ================ *#
#* ================================================== *#


# l1 = ['a', 'b', 'c']

# try:
#     print(7/1)
#     print(l1[10])

# except ZeroDivisionError:
#     print("You cannot divide by zero")

# except IndexError:
#     print("List index is out of range")


#* ================================================== *#

# l1 = ['a', 'b', 'c']

# try:
#     print(7/1)
#     # print(l1[10])
#     print(int("Hello"))

# except ZeroDivisionError:
#     print("You cannot divide by zero")

# except IndexError:
#     print("List index is out of range")

# except ValueError:
#     print("Cannot convert alphabats to integer")


#* ================================================== *#
# What if you handle all errors but an expected error comes?

# l1 = ['a', 'b', 'c']

# try:
#     print(7/1)
#     # print(l1[10])
#     # print(int("Hello"))
#     print(age)

# except ZeroDivisionError:
#     print("You cannot divide by zero")

# except IndexError:
#     print("List index is out of range")

# except ValueError:
#     print("Cannot convert alphabats to integer")


#* ================================================== *#
#* =================== Exception ==================== *#
#* ================================================== *#

# l1 = ['a', 'b', 'c']

# try:
#     print(7/1)
#     # print(l1[10])
#     # print(int("Hello"))
#     print(age)

# except ZeroDivisionError:       # handle ZeroDivisionError
#     print("You cannot divide by zero")

# except IndexError:              # handle IndexError
#     print("List index is out of range")

# except ValueError:              # handle ValueError
#     print("Cannot convert alphabats to integer")

# except Exception as e:          # handle remaining all errors
#     print(f"An unexcepted error: {e}")


#* ================================================== *#

# l1 = ['a', 'b', 'c']

# try:
#     print(8 / 0) # Error in this line
#     print(l1[1]) # Interpreter ignore all code beyond this line

# except ZeroDivisionError:
#     print("You cannot divide by zero")

# except IndexError:
#     print("List index is out of range")


#* ================================================== *#
#* =============== Multiple try-except ============== *#
#* ================================================== *#


# l1 = ['a', 'b', 'c']

# try:
#     print(8 / 0)
# except ZeroDivisionError:
#     print("You cannot divide by zero")

# try:
#     print(l1[1])
# except IndexError:
#     print("List index is out of range")


#* ================================================== *#
#* ================== Raise Errors ================== *#
#* ================================================== *#

# raise Exception("Your error message")

#* ================================================== *#


# age = -5
# if age < 0:
#     raise ValueError("Age cannot be negative")


#* ================================================== *#
#* ============== Custom Error Classes ============== *#
#* ================================================== *#


# class InvalidAgeError(Exception):
#     pass

# age = -5
# if age < 0:
#     raise InvalidAgeError("Age cannot be negative")


