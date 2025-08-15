
#* ================================================== *#
#* ================ Simple Function ================= *#
#* ================================================== *#


# def greet(): # Define function
    
#     # Function body
#     print("Hello world")
#     print("Hello world")
#     print("Hello world")

# greet() # Function calling
# greet() # Function calling


#* ================================================== *#
#* ================== Print 2 + 2 =================== *#
#* ================================================== *#


# def sum():
#     print(2 + 2)

# sum()


#* ================================================== *#
#* =============== Keyword arguments ================ *#
#* ================================================== *#


# def sum( num1, num2 ):
#     print(num1 + num2)

# sum( num1=5, num2=10 )  # Output: 15
# sum( num1=45, num2=55 ) # Output: 100


#* ================================================== *#
#* ============== Positional Arguments ============== *#
#* ================================================== *#


# def sum( num1, num2 ):
#     print(num1 + num2)

# sum( 5, 10 )  # Output: 15
# sum( 45, 55 ) # Output: 100


#* ================================================== *#
#* =================== Calculator =================== *#
#* ================================================== *#


# def calculator( num1, num2, operator ):
#     if operator == '+':
#         print(num1 + num2)

#     elif operator == '-':
#         print(num1 - num2)

#     elif operator == '*':
#         print(num1 * num2)

#     elif operator == '/':
#         print(num1 / num2)

#     else:
#         print("Invalid operator")

# calculator(2, 2, '-') # Output: 0
# calculator(2, 2, '+') # Output: 4
# calculator(2, 2, '*') # Output: 4
# calculator(2, 2, '/') # Output: 1.0


#* ================================================== *#
#* =============== Dynamic Calculator =============== *#
#* ================================================== *#


# def calculator( num1, num2, operator='+' ):
#     if operator == '+':
#         print(num1 + num2)

#     elif operator == '-':
#         print(num1 - num2)

#     elif operator == '*':
#         print(num1 * num2)

#     elif operator == '/':
#         print(num1 / num2)

#     else:
#         print("Invalid operator")


# user_num1 = int(input("Enter first number: "))
# user_operator = input("Enter operator (+, -, *, /) : ")
# user_num2 = int(input("Enter second number: "))

# calculator(user_num1, user_num2, user_operator) 


#* ================================================== *#
#* =============== Default Parameter ================ *#
#* ================================================== *#


# def greet( name="User" ):
#     print(f"Hello, {name}!")

# greet("Okasha")  # Output: "Hello, Okasha"
# greet()          # Output: "Hello, User"
# greet("Hamzah")  # Output: "Hello, Hamzah"


#* ================================================== *#
#* ===============                    =============== *#
#* ================================================== *#


# def greet( age, name="User" ):
#     print(f"Hello, {name}! and you are {age} years old.")

# greet( "Okasha" )     # Output: "Hello, User! and you are Okasha years old."
# greet( 21, "Okasha" ) # Output: "Hello, Okasha! and you are 21 years old."


#* ================================================== *#
#* ================= Return Keyword ================= *#
#* ================================================== *#


# def calculator( num1, num2, operator ):
#     output = 0
#     if operator == '+':
#         output = num1 + num2
#     elif operator == '-':
#         output = num1 - num2
#     elif operator == '*':
#         output = num1 * num2
#     elif operator == '/':
#         output = num1 / num2
#     else:
#         output = "Invalid operator"
    
#     return output

# result = calculator(2, 2, '+')
# # print(output) # NameError: name 'output' is not defined
# print(result)   # Output: 4


#* ================================================== *#
#* ========= Return Keyword (simple example) ======== *#
#* ================================================== *#


# def add():
#     return 2 + 2

# result = add()
# print(result)


#* ================================================== *#
#* ==================== Acticity ==================== *#
#* ================================================== *#


# def catch(item):
#     print("TAPPING ...")
#     return f"Catched: {item}"

# bag = catch("⚾")
# print(bag)


#* ================================================== *#
#* =========== Code After Return Keyword ============ *#
#* ================================================== *#


# def catch(item):
#     print("TAPPING ...")
#     return "abc"
#     return f"Catched: {item}"
#     print("Done")
    
# bag = catch("⚾")
# print(bag)


#* ================================================== *#
#* ================ Lambda Function ================= *#
#* ================================================== *#

# def add(num1, num2):
#     return num1 + num2
# print(add(2, 2))

add = lambda num1, num2: num1 + num2
print(add(2, 2))
