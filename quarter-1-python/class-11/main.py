
#* ================================================== *#
#* =========== Object-Oriented Programming ========== *#
#* ================================================== *#

# class House:
#     def __init__(self):
#         # self = {}

#         self.address = "XYZ 123"
#         # self = { address: "XYZ 123" }

#         self.number_of_rooms = 4
#         # self = { address: "XYZ 123", number_of_rooms: 4 }

#         self.number_of_doors = 2
#         # self = { address: "XYZ 123", number_of_rooms: 4, number_of_doors: 2 }

# h1 = House()
# print( h1 )
# print( h1.address )

# h2 = House()
# print( h2.address )


#* ================================================== *#
#* =========== Constructor with Parameters ========== *#
#* ================================================== *#


# class House:
#     def __init__(self, addrs): 
#         self.address = addrs
#         self.number_of_rooms = 4
#         self.number_of_doors = 2

# h1 = House("A29")
# print( h1.address )


#* ================================================== *#
#* ==================== Methods ===================== *#
#* ================================================== *#


# class House:
#     def __init__(self, addrs): 
#         self.address = addrs
#         self.number_of_rooms = 4
#         self.number_of_doors = 2

#     def ring_bell(self):
#         print("Ding dong!")

# h1 = House("A29")
# print( h1.address )
# h1.ring_bell()


#* ================================================== *#
#* ============ Class Without Inheritance =========== *#
#* ================================================== *#


# class Appartment:
#     def __init__(self, addrs, flat_number): 
#         self.address = addrs
#         self.number_of_rooms = 4
#         self.number_of_doors = 2
#         self.flat_number = flat_number

# aprt1 = Appartment("ABC", 23)
# print( aprt1.flat_number )


#* ================================================== *#
#* =================== Inheritance ================== *#
#* ================================================== *#


# class House:
#     def __init__(self, addrs): 
#         self.address = addrs
#         self.number_of_rooms = 4
#         self.number_of_doors = 2

#     def ring_bell(self):
#         print("Ding dong!")


# class Appartment(House):
#     def __init__(self, addrs, flat_number):
#         super().__init__(addrs) 
#         self.flat_number = flat_number

# aprt1 = Appartment("ABC", 23)

# print( aprt1.address )
# print( aprt1.flat_number )
# print( aprt1.number_of_doors )
# print( aprt1.number_of_rooms )



#* ================================================== *#
#* ============== Multiple Inheritance ============== *#
#* ================================================== *#


# class House:
#     def __init__(self, addrs): 
#         self.address = addrs
#         self.number_of_rooms = 4
#         self.number_of_doors = 2

#     def ring_bell(self):
#         print("Ding dong!")


# class House1:
#     def __init__(self, color):
#         self.color = color


# class Appartment(House, House1):
#     def __init__(self, addrs, flat_number):
#         House.__init__(self, addrs) 
#         House1.__init__(self, 'red') 
#         self.flat_number = flat_number


# aprt1 = Appartment("ABC", 23)

# print( aprt1.address )
# print( aprt1.flat_number )
# print( aprt1.number_of_doors )
# print( aprt1.number_of_rooms )
# print( aprt1.color )


