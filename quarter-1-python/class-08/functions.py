
#* ================================================== *#
#* ============= sep and end in print() ============= *#
#* ================================================== *#


# print(1, 2, 3, 4, 5)             # default sep=' '   # space
# print(1, 2, 3, 4, 5, sep='**')   # default end='\n'  # next line
# print(1, 2, 3, 4, 5, sep='**', end='====')
# print(1, 2, 3, 4, 5, sep='++', end='====')


#* ================================================== *#
#* =============== flush in print() ================= *#
#* ================================================== *#

# import time


# text = """Python was created in the early 1990s by Guido van Rossum at Stichting
# Mathematisch Centrum (CWI, see https://www.cwi.nl) in the Netherlands
# as a successor of a language called ABC.  Guido remains Python's
# principal author, although it includes many contributions from others."""

# # Without flush
# print("Without flush")
# for i in text.split():
#   print(i, end=' ')
#   time.sleep(0.1) # to sleep for 0.1 second


# print('\n', '='*50)

# # With flush
# print("With flush")
# for i in text.split():
#   print(i, end=' ', flush=True)
#   time.sleep(0.1) # to sleep for 0.1 second


#* ================================================== *#
#* =============== Without type hints =============== *#
#* ================================================== *#


# def my_function(num1, num2):
#     return num1 + num2

# my_function(5, 3)


#* ================================================== *#
#* ================ With type hints ================= *#
#* ================================================== *#

# def my_function(num1: int | float, num2: int | float) -> int | float :
#     return num1 + num2

# my_function(5, 3)

#* ================================================== *#
#* ============ With doc string (pydoc) ============= *#
#* ================================================== *#

# def my_function(num1: int | float, num2: int | float) -> int | float :
#     """This function takes two number and return thier sum

#     Args:
#         num1 (int | float): 
#         num2 (int | float): 

#     Returns:
#         (int | float): sum of num1 and num2
#     """    
#     return num1 + num2

# my_function(5, 3)


#* ================================================== *#
#* =============== Default Function ================= *#
#* ================================================== *#

# def greet():
#     print("Hello! Welcome to PIAIC.")

# greet()

#* ================================================== *#
#* ============== Required Parameters =============== *#
#* ================================================== *#

# def multiply(a: int, b: int) -> int:
#     """Multiply two required parameters and return the result."""
#     return a * b

# result = multiply(4, 5)
# print(result)

#* ================================================== *#
#* ============== Optional Parameters =============== *#
#* ================================================== *#

# def greet(name: str, message: str = "Welcome!") -> None:
#     print(f"Hello, {name}! {message}")

# greet("Qasim")                # Uses default message
# greet("Hamzah", "Good day!")  # Custom message

#* ================================================== *#
#* =============== on-return Function =============== *#
#* ================================================== *#

# def print_introduction() -> None:
#     print("Welcome to the Python Class!")
#     print("In this session, we'll cover functions, decorators, error handling, and more.")
#     print("Let's get started and have fun learning Python!")

# print_introduction()


#* ================================================== *#
#* =================== Arguments ==================== *#
#* ================================================== *#

def add_numbers(
    num1: int,
    num2: int,
    num3: int = 0,
    num4: int = 0,
) -> int:
    return num1 + num2 + num3 + num4

add_numbers(4, 4)


#* ================================================== *#
#* ============== Positional Arguments ============== *#
#* ================================================== *#

# li = [10, 20, 40]  # List containing two numbers

# # Call add_numbers by passing elements individually
# add_numbers(li[0], li[1])

# # Call add_numbers by unpacking the list as arguments
# add_numbers(*li)

#* ================================================== *#
#* =============== Keyword Arguments ================ *#
#* ================================================== *#

# dt = {
#     'num1': 10,
#     'num2': 20,
# }

# # Call add_numbers using keyword arguments from dictionary values
# add_numbers(num1=dt['num1'], num2=dt['num2'])

# # Call add_numbers by unpacking the dictionary as keyword arguments
# add_numbers(**dt)


#* ================================================== *#
#* ========= Unlimited Positional Arguments ========= *#
#* ================================================== *#

# def sum_all(*args: int) -> int:
#     """Sums any number of integer arguments."""
    
#     print(args)        # (1, 2, 3, 4, 5)
#     print(type(args))  # <class 'tuple'>
#     return sum(args) 

# # Example usage
# result = sum_all(1, 2, 3, 4, 5)
# print(result)  # Output: 15


#* ================================================== *#
#* =========== Unlimited Keyword Arguments ========== *#
#* ================================================== *#

# def print_student_info(name: str, **info: str) -> None:
#     """
#     Prints student name and any additional keyword information.

#     Args:
#         name (str): The student's name.
#         **info (str): Arbitrary keyword arguments with additional info.
#     """
#     print(f"Name: {name}")
#     print(f"Info: {info}")
#     print(f"Type of info: {type(info)}")
    

# # Example usage
# print_student_info("Qasim", age="40", grade="A", city="Karachi")


#* ================================================== *#
#* ===== All type of arguments in one functions ===== *#
#* ================================================== *#

# def demo_args(
#     name: str,                # Positional argument
#     age: int = 1,         # Keyword argument with default value
#     *args: int,               # Unlimited positional arguments (tuple of ints)
#     **kwargs: str             # Unlimited keyword arguments (dict of str)
# ) -> None:

#     print(f"name: {name}")
#     print(f"age: {age}")
#     print(f"args: {args}")
#     print(f"kwargs: {kwargs}")

# # Example usage:
# demo_args(
#     "Qasim",                # name (as positional)
#     40,                     # age  (as positional)
#     1, 2, 3,                # *args
#     city="Karachi", country="Pakistan"  # **kwargs
# )

# print('='*50)

# demo_args(
#     "Qasim",                # name (as positional)
#     age=40,                 # age (as keyword)
#     # cannot use unlimited positional arguments after keyword arguments
#     city="Karachi", country="Pakistan"  # **kwargs
# )


#* ================================================== *#
#* ================= Lambda Function ================ *#
#* ================================================== *#

# add = lambda x, y: x + y
# print(add(2, 3))


#* ================= with type hints ================ *#

# from typing import Callable

# #    Callable[ [ x ,  y ], return type]
# add: Callable[ [int, int], int] = lambda x, y: x + y

# print(add(4, 4))

#* =========== use cases (sort / reverse) =========== *#

# data = {'c': 3, 'a': 1, 'b': 2}
# print(data.items())

# sorted_dict = dict(sorted(data.items(), key=lambda x: x[0]))
# print("Sorted dict:", sorted_dict)

# reversed_dict = dict(reversed(sorted_dict.items()))
# print("Reversed dict:", reversed_dict)


#* ================================================== *#
#* =============== Recursive Function =============== *#
#* ================================================== *#

# def my_fn(n):
#     print(f"\nStep 1: {n}")
#     if n == 0:
#         print("n is zero")
#         return 1
    
#     print(f"n is {n - 1}")    
#     return n * my_fn(n - 1)


# print(my_fn(5))
# print(1 * 2 * 3 * 4 * 5)


#* ================================================== *#
#* =============== Generator Function =============== *#
#* ================================================== *#

# def table_generator(number: int, upto: int = 10):
#     """Generator function to yield the multiplication table of a given number."""
#     for i in range(1, upto + 1):
#         yield f"{number} x {i} = {number * i}"


# # Example usage:
# table_of_2 = table_generator(2)

# print(next(table_of_2))
# print(next(table_of_2))
# print("Hello world")
# print(next(table_of_2))

#* ================ with type hints ================= *#

# from typing import Iterator

# def count_to(stop: int) -> Iterator[int]:
#     for i in range(1, stop + 1):
#         yield i

# l1 = count_to(10)
# print(list(l1))

#* =================== with loop ==================== *#

# from typing import Iterator
# def count_to(stop: int) -> Iterator[int]:
#     for i in range(1, stop + 1):
#         yield i

# l1 = count_to(3)
# for i in l1:
#     print(i)


#* ================================================== *#
#* =============== Callback Functions =============== *#
#* ================================================== *#

# def say_hello():
#     print("Hello")

# def my_func(func):
#     print("Pakistan")
#     func()
#     print("Zindabad")

# my_func(say_hello)

#* ================ with type hints ================= *#

# from typing import Callable

# def my_func(func: Callable):
#     print("Pakistan")
#     func()
#     print("Zindabad")

# my_func(say_hello)


#* ================================================== *#
#* =================== Decorators =================== *#
#* ================================================== *#

# from typing import Callable

# def my_dec(func: Callable):
#     def wrapper(): 
#         print('========== start =========')    
#         func()
#         print('==========  end  =========')
#     return wrapper

# @my_dec
# def say_hello():
#     print("Hello")

# say_hello()

#* ================================================== *#
#* ===== Decorator with parameters / arguments ====== *#
#* ================================================== *#

# from typing import Callable

# def my_dec(func: Callable):
#     def wrapper(*args, **kwargs): 
#         print('========== start =========')    
#         func(*args, **kwargs)  # msg will be passed here as a positional argument
#         print('==========  end  =========')
#     return wrapper

# @my_dec
# def print_msg(msg: str):
#     print(msg)

# # When print_msg("Hello") is called:
# # 1. The call is intercepted by wrapper.
# # 2. "Hello" is captured in *args.
# # 3. wrapper calls func(*args, **kwargs), so print_msg("Hello") runs with msg="Hello".

# print_msg("Hello")  # in background wrapper function is calling


#* ================================================== *#
#* =============== Create / Write file ============== *#
#* ================================================== *#

# from typing import TextIO

# file: TextIO = open('abc.txt', 'w') # write mode
# file.write("Hello world")
# file.close()


#* ================================================== *#
#* ================= Append in File ================= *#
#* ================================================== *#

# from typing import TextIO

# file: TextIO = open('abc.txt', 'a') # append mode
# file.write("\nAnother line")
# file.close()

#* ================================================== *#
#* =================== Read File ==================== *#
#* ================================================== *#

# from typing import TextIO

# file: TextIO = open('abc.txt', 'r') # read mode
# content = file.read()
# print(content)
# file.close()

#* ================================================== *#
#* =================== With block =================== *#
#* ================================================== *#

# with open('abc.txt', 'a') as file:
#     file.write("\nUsing with block")

#* ================================================== *#
#* ================ @contextmanager ================= *#
#* ================================================== *#

# from contextlib import contextmanager

# db = { 'users': [] } # Your database

# @contextmanager
# def connect_db():
#     try:
#         print("Data base connected")
#         yield db  # Provide the db dictionary to the with block
#     finally:
#         print("Data connection close")


# with connect_db() as database:
#     database['users'].append({'name': 'Qasim', 'email': 'qasim@example.com'})
#     print(database)


#* ================================================== *#
#* ============ Synchronous (one by one) ============ *#
#* ================================================== *#


# import time
# from typing import List

# def fetch_data(url: str) -> None:
#     print(f"\nFetching {url}")
#     time.sleep(2)
#     print(f"Done {url}")

# def main(urls: List[str]) -> None:
#     for u in urls:
#         fetch_data(u)

# main(["url_1", "url2", "url3"])
# # Each URL waits 2 seconds in order. Total time ≈ 6 seconds.


#* ================================================== *#
#* ============ Asynchronous (parallel) ============= *#

import asyncio

async def fetch(id: int) -> str:
    print(f"Task {id} start")
    await asyncio.sleep(2)  # Doesn’t block others
    print(f"Task {id} done")
    return f"T-{id}"

#* ================ Run single task ================= *#

# asyncio.run(fetch(5))

#* =============== Run multiple tasks =============== *#

# async def main() -> None:
#     r1 = await fetch(1) # this will take 2 seconds
#     r2 = await fetch(2) # this will take 2 seconds
#     r3 = await fetch(3) # this will take 2 seconds
#     # total = 2 + 2 + 2 = 6 seconds
    
#     print(f"\nResult 1: {r1}")
#     print(f"Result 2: {r2}")
#     print(f"Result 3: {r3}")

# asyncio.run(main())


#* ============== with asyncio.gather() ============= *#

# async def main() -> None:
#     results: tuple[str, str, str] = await asyncio.gather(
#         fetch(1), 
#         fetch(2), 
#         fetch(3)
#     ) # return the result of fetch in tuple, in order
#     print("Results:", results)

# asyncio.run(main())


#* ================================================== *#
#* ================ Another example ================= *#
#* ================================================== *#


# import asyncio

# async def fn(n: int):
#     await asyncio.sleep(n)
#     return f"Message: {n}"

# async def main():
#     result = await asyncio.gather(fn(2), fn(5), fn(7))
#     print(result)

# asyncio.run(main())




#* =============== Create / Write file ============== *#
# from typing import TextIO

# file: TextIO = open('abc.txt', 'w') # write mode
# file.write("Hello world")
# file.close()


#* ================= Append in File ================= *#
# from typing import TextIO

# file: TextIO = open('abc.txt', 'a') # append mode
# file.write("\nAnother line")
# file.close()

#* =================== Read File ==================== *#
# from typing import TextIO

# file: TextIO = open('abc.txt', 'r') # read mode
# content = file.read()
# print(content)
# file.close()

#* =================== With Block =================== *#
with open('abc.txt', 'r') as file:
    print(file.read())
