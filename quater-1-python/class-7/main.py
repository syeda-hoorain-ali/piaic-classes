
#* ================================================== *#
#* =============== Callback Function ================ *#
#* ================================================== *#


# def fn1( func2 ):
#     print("inside of fn1: Hello")
#     func2()

# def fn2():
#     print("inside of fn2: world")


# fn1( fn2 )


#* ================================================== *#
#* =================== Decorators =================== *#
#* ================================================== *#


# def auth_checker( fn ):
#     def wrapper(*args): # Getting unlimited arguments
#         print("\nChecking...")
#         fn(*args) # Passing arguments to function
#     return wrapper


# @auth_checker
# def access_dashboard():
#     print("Open portal")


# @auth_checker
# def get_addmission():
#     print("Registered")


# access_dashboard()
# get_addmission()


#* ================================================== *#
#* =============== Multiple Decorators ============== *#
#* ================================================== *#


# def auth_checker( fn ):
#     def wrapper(*args): # Getting unlimited arguments
#         print("\nChecking...")
#         fn(*args) # Passing arguments to function
#     return wrapper


# def is_admin( fn ):
#     def wrapper(*args): # Getting unlimited arguments
#         print("User is admin")
#         fn(*args) # Passing arguments to function
#     return wrapper


# @auth_checker # Check if user is logged in
# @is_admin     # Check if user is admin
# def access_dashboard():
#     print("Open portal")


# @auth_checker # Check if user is logged in
# def get_addmission():
#     print("Registered")


# access_dashboard()
# get_addmission()


#* ================================================== *#
#* ============== Problem without loop ============== *#
#* ================================================== *#

# names_of_students = ["Okasha", "Ali", "Hamzah", "Abdul Aziz"]

# print(names_of_students[0])
# print(names_of_students[1])
# print(names_of_students[2])
# print(names_of_students[3])


#* ================================================== *#
#* ==================== For Loop ==================== *#
#* ================================================== *#


# names_of_students = ["Okasha", "Ali", "Hamzah", "Abdul Aziz"]

# print("Hello before")
# for name in names_of_students:
#     print(f"Hello {name}")

# print("Hello after")


#* ================================================== *#
#* ===============                    =============== *#
#* ================================================== *#


# names_of_students = ["Okasha", "Ali", "Hamzah", "Abdul Aziz"]
# count = 1

# for name in names_of_students:
#     print(f"{count}. {name}")
#     count += 1


#* ================================================== *#
#* =========== range ( start, end, step ) =========== *#
#* ================================================== *#


# # range ( start, end, step )
# # range(1, 10, 2) = [1, 3, 5, 7, 9]
# for num in range(1, 100, 2):
#     print(num)


#* ================================================== *#
#* =========== Without list comprehension =========== *#
#* ================================================== *#


# root_list = []

# for num in range(1, 11):
#     root_list.append(num ** 2)

# print(root_list)


#* ================================================== *#
#* =============== List Comprehension =============== *#
#* ================================================== *#


# num_list = [ num for num in range(1, 11) ]
# root_list = [ num**2 for num in range(1, 11) ]
# print(root_list) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#* ================================================== *#
#* ======== List comprehension with if-else ========= *#
#* ================================================== *#


# even_root_list = []

# for num in range(1, 11):
#     if num % 2 == 0:
#         even_root_list.append(num ** 2)

# print(even_root_list)

# even_root_list = [ num**2 for num in range(1, 11) if num % 2 == 0]
# print(even_root_list)


#* ================================================== *#
#* ===== List comprehension with existing list ====== *#
#* ================================================== *#
     
     
# names = ["Okasha", "Ali"]
# updated_names = [ name.upper() for name in names ]     
# print(updated_names)


#* ================================================== *#
#* =================== While Loop =================== *#
#* ================================================== *#

# count = 1

# while count <= 10:
#     print(f'{count}, Hello')
#     count += 1


#* ================================================== *#
#* ============== Number Guessing Game ============== *#
#* ================================================== *#


import random

secret_number = random.randint(1, 100)
count = 0

while True:
    user_num = int(input("\nGuess the number: "))
    count += 1

    if user_num < secret_number:
        print("Your number is too low")

    elif user_num > secret_number:
        print("Too high")

    else:
        print("You won")
        print(f"You guessed number in {count} attempts")
        break

