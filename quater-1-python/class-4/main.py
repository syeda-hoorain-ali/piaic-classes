
#* ================================================== *#
#* =================== Data Types =================== *#
#* ================================================== *#

# first_name = "Hamzah"
# # print(id(first_name))
# print(type(first_name))


# number = 2.3
# print(type(number))



#* ================================================== *#
#* ========== Type Comparison with `type()` ========= *#
#* ================================================== *#

# first_name = "Hamzah"
#              str       == str
# print(type(first_name) == str)
# print(str)



#* ================================================== *#
#* ======== Input Validation with `isdigit()` ======= *#
#* ================================================== *#

# age = input("Enter your age: ")
# is_valid_age = age.isdigit()
# print(is_valid_age)



#* ================================================== *#
#* ========= Input Validation with `if-else` ======== *#
#* ================================================== *#

# age = input("Enter your age: ")

# if age.isdigit():
#     num_age = int(age)
#     print(f"Valid age: {num_age}")

# else:
#     print("Enter a valid age")



#* ================================================== *#
#* ========= Conditional Statements Example ========= *#
#* ================================================== *#

# bobzi_runs = 50

# if bobzi_runs >= 50:
#     print("👑 King")

# else:
#     print("🔔 King")



#* ================================================== *#
#* ========= Logical Operators in Conditions ======== *#
#* ================================================== *#

# bobzi_runs = 50
# total_balls = 50

# if bobzi_runs >= 50 and bobzi_runs > total_balls:
#     print("👑 King")

# else:
#     print("🔔 King")



#* ================================================== *#
#* ======= Complex Logical Conditions Example ======= *#
#* ================================================== *#

# bobzi_runs = 36
# total_balls = 20
# total_sixes = 5

# a = bobzi_runs >= 50 and total_balls
# b = total_balls < bobzi_runs
# c = total_sixes >= 5


# # 1.    False       and            True           or      True
# # 2.               False                          or      True
# # 3.                           True
# if bobzi_runs >= 50 and total_balls < bobzi_runs or total_sixes >= 5 :
#     print("👑 King")

# else:
#     print("🔔 King")



#* ================================================== *#
#* ======== Logical Operators with Variables ======== *#
#* ================================================== *#

# bobzi_runs = 36
# total_balls = 20
# total_sixes = 5


# a = bobzi_runs >= 50 and total_balls    # False
# b = total_balls < bobzi_runs            # True
# c = total_sixes >= 5                    # True


# if a and b or c:
#     print("👑 King")

# else:
#     print("🔔 King")



#* ================================================== *#
#* ========= List Example and Initialization ======== *#
#* ================================================== *#

# item1 = "Hara dhaniya"
# item2 = "Podina"
# item3 = "Dahi"
# item4 = "Andey"


# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]
# Real world example: discord tickets in forum

# print(items)
# print( type(items) )



#* ================================================== *#
#* ============= Accessing List Elements ============ *#
#* ================================================== *#

# #                0           1        2        3
# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

# print(items)
# print( items[2], items[0] )  # "Dahi Hara ghaniya"



#* ================================================== *#
#* ================ Length of a List ================ *#
#* ================================================== *#

# #                0           1        2        3
# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

# print(items)
# print( len(items) )



#* ================================================== *#
#* ============ List Methods with `dir()` =========== *#
#* ================================================== *#

# #                0           1        2        3
# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

# print(items)
# print( dir(items) )



#* ================================================== *#
#* ========= Removing Elements with `pop()` ========= *#
#* ================================================== *#

# #                0           1        2        3
# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

# print(items)
# items.pop() # remove "Andey"          # items = [ "Hara dhaniya", "Podina", "Dahi" ]
# items.pop() # remove "Dahi"           # items = [ "Hara dhaniya", "Podina" ]
# items.pop() # remove "Hara dhaniya"   # items = [ "Hara dhaniya" ]
# print(items)



#* ================================================== *#
#* ============ Removing Specific Element =========== *#
#* ================================================== *#

# #                0           1        2        3
# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

# print(items)
# items.pop(2) # remove "Dahi"    # [ "Hara dhaniya", "Podina", "Andey" ]
# print(items)



#* ================================================== *#
#* ========= Negative Indexing with `pop()` ========= *#
#* ================================================== *#

# #               -4           -3       -2      -1
# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

# print(items)
# items.pop(-2) # remove "Dahi"   # items = [ "Hara dhaniya", "Podina", "Andey" ]
# print(items)



#* ================================================== *#
#* ========= Adding Elements with `append()` ======== *#
#* ================================================== *#

# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

# print(items)
# items.append("Roti") # add "Roti"   # items = [ "Hara dhaniya", "Podina", "Dahi", "Andey", "Roti" ]
# print(items)



#* ================================================== *#
#* ========= Adding Elements with `insert()` ======== *#
#* ================================================== *#

# #                0           1        2        3
# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

# print(items)
# items.insert(3, "Aalo") # add "Aalo"    # [ "Hara dhaniya", "Podina", "Dahi", "Aalo", "Andey" ]
# print(items)



#* ================================================== *#
#* ========== Removing Elements with `remove()` ===== *#
#* ================================================== *#

# #                0           1        2        3
# items = [ "Hara dhaniya", "Podina", "Dahi", "Andey" ]

# print(items)
# items.remove("Dahi") # remove "Dahi"    # [ "Hara dhaniya", "Podina", "Aalo", "Andey" ]
# print(items)



