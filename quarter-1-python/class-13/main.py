
#* ================================================== *#
#* =========== Object-Oriented Programming ========== *#
#* ================================================== *#

# class House:
#     def __init__(self):
#         # self = {}
#         self.address: str = "123"
#         self.no_of_doors: int = 2
#         self.no_of_rooms: int = 4
#         # self =  { address: "123 xyz", no_of_doors: 2, no_of_rooms: 4 }


# h1 = House()  #  { address, no_of_rooms, ... }
# h2 = House()  #  { address, no_of_rooms, ... }
# h3 = House()  #  { address, no_of_rooms, ... }

# print(h3.address)
# print(h1.address)


#* ================================================== *#
#* =========== Constructor with Parameters ========== *#
#* ================================================== *#


# class House:
#     def __init__(self, address):
#         # self = {}
#         self.address: str = address
#         self.no_of_doors: int = 2
#         self.no_of_rooms: int = 4
#         # self =  { address: "123 xyz", no_of_doors: 2, no_of_rooms: 4 }


# h1 = House(address = "xyz 123")  #  { address, no_of_rooms, ... }
# h2 = House("xyz 124")            #  { address, no_of_rooms, ... }
# h3 = House("xyz 125")            #  { address, no_of_rooms, ... }

# print(h3.address)
# print(h1.address)


#* ================================================== *#
#* == Constructor with default/optional parameters == *#
#* ================================================== *#


# class House:
#     def __init__(self, address = None): # give default 'None' value to make it optional
#         self.address: str | None = address
#         self.no_of_doors: int = 2
#         self.no_of_rooms: int = 4


# h1 = House(address = "xyz 123")
# h2 = House("xyz 124")
# h3 = House()

# print(h3.address)
# print(h1.address)


#* ================================================== *#
#* ============= Attributes and Methods ============= *#
#* ================================================== *#


# class House:
#     def __init__(self, address):
#         self.address: str = address
#         self.no_of_doors: int = 2
#         self.no_of_rooms: int = 4

#     def call_lift(self):
#         print(f"  {self.address} Lift is called")


# h1 = House(address = "xyz 123")
# h2 = House("xyz 124")
# h3 = House("xyz 125")

# h2.call_lift()


#* ================================================== *#
#* =========== Task to make a Student class ========= *#
#* ================================================== *#


# class Student:
#     def __init__(self, name, roll_no):
#         self.name: str = name
#         self.roll_no: str = roll_no
#         self.institute: str = "PIAIC"
    
#     def get_addmission(self):
#         print(f"{self.name} you addmission is final")
    
#     def pay_fee(self, fees: int):
#         print(f"Paying fees: {fees}")


# std1 = Student("Ali", '123')
# std2 = Student("Ahmad", '124')
# std3 = Student("Alishba", '125')

# std3.get_addmission()
# std3.pay_fee(1000)



#* ================================================== *#
#*  Task to make a Course class with list of Students *#
#* ================================================== *#


# class Course:
#     def __init__(self, course_name):
#         self.course_name = course_name
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)


# ai_course = Course("AI")
# ai_course.add_student(std1)

# print(ai_course.students)
# print(ai_course.students[0].name)


#* ================================================== *#
#* ================ With types hints ================ *#
#* ================================================== *#


# class Course:
#     def __init__(self, course_name):
#         self.course_name: str = course_name
#         self.students: list[Student] = []

#     def add_strudent(self, student: Student):
#         self.students.append(student)


# ai_course = Course("AI")
# ai_course.add_strudent(std1)

# print(ai_course.students)
# print(ai_course.students[0].name)


#* ================================================== *#
#* ================== Inheritance =================== *#
#* ================================================== *#


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def eat(self):
#         print("Eating...")


# class Student(Human):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no


# class Teacher(Human):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary


# std1 = Student("Okasha", 21, 12345)
# print(std1.name)



#* ================================================== *#
#* ================== Polymorphism ================== *#
#* ================================================== *#


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def eat(self):
#         print("Eating with right hand")


# class Student(Human):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no


# class Teacher(Human):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
    
#     def eat(self):
#         print("Eating with left hand")



# std1 = Student("Okasha", 21, 12345)
# std1.eat()

# teacher1 = Teacher("Ali", 22, 30000)
# teacher1.eat()



#* ================================================== *#
#* ================== Encapsulation ================= *#
#* ================================================== *#


# class BankAccount:
#     def __init__(self, name, account_no, balance):
#         self.name = name
#         self._account_no = account_no
#         self.__balance = balance
    
#     def get_balance(self, account_no):
#         if self._account_no == account_no:
#             return self.__balance
#         else:
#             return "Invalid account number"
    
#     def deposit(self, account_no, amount):
#         if self._account_no != account_no:
#             return "Invalid account number"
#         self.__balance += amount

#     def withdraw(self, account_no, amount):
#         if self._account_no != account_no:
#             return "Invalid account number"
#         self.__balance -= amount



# user1 = BankAccount("Okasha", 12345, 500)
# print(user1.name)
# print(user1._account_no)
# # print(user1.balance)

# print(user1.get_balance(68742))
# print(user1.get_balance(12345))

# user1.deposit(account_no=12345, amount=1000)
# print(user1.get_balance(12345))



#* ================================================== *#
#* ================== Abstraction =================== *#
#* ================================================== *#


from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod
    def payment_proccess(self):
        pass

    @abstractmethod
    def refund(self):
        ... # use `pass` keyword or three dots `...`


# payment = PaymentMethod()   #! TypeError: Can't instantiate abstract class PaymentMethod


class Stripe(PaymentMethod):
    def payment_proccess(self):
        print("Stripe Payment Process")

    def refund(self):
        print("Stripe Refund")


stripe = Stripe()
stripe.payment_proccess()
stripe.refund()

