
#* ================================================== *#
#* ================ Greeting Function =============== *#
#* ================================================== *#


def greet(name: str) -> str:
    return f"Hello, {name}"

print(greet("Hamzah"))


#* ================================================== *#
#* ================= Student Details ================ *#
#* ================================================== *#


student_details = {
    "name": "Hamzah",
    "age": 24,
    "address": "Karachi"
}

print(student_details)
print(student_details["name"])
print(student_details["age"])

print(f"""
Name = {student_details["name"]}
Age = {student_details["age"]}
Address = {student_details["address"]}
""")


#* ================================================== *#
#* =========== Accessing Dictionary Value =========== *#
#* ================================================== *#


print(student_details["address"])  # Access value by key


#* ================================================== *#
#* =========== Updating Dictionary Value ============ *#
#* ================================================== *#


student_details["age"] = 25  # Update value by key
print(student_details["age"])


#* ================================================== *#
#* ============= Get Value with Default ============= *#
#* ================================================== *#


print(student_details.get("email", "Not Provided"))  # Get with default


#* ================================================== *#
#* ================ Dictionary Keys ================= *#
#* ================================================== *#


print(student_details.keys())  # Get all keys


#* ================================================== *#
#* =============== Dictionary Values ================ *#
#* ================================================== *#


print(student_details.values())  # Get all values


#* ================================================== *#
#* =========== Remove Item from Dictionary ========== *#
#* ================================================== *#


removed_address = student_details.pop("address")
print(f"Removed address: {removed_address}")
print(student_details)


#* ================================================== *#
#* ================== LLM Function ================== *#
#* ================================================== *#


def llm(prompt: str) -> str:
    return "Hello, How can I help you today!"

response = llm(prompt="Hi")
print(response)

