# Functions

def my_function():
    print("Hello World!")

# my_function()

def greet(name):
    message = "Hello " + str(name) + "!"
    print(message)

# greet(10)

def calculate_area(length, width=10):
    area = length * width
    return area

my_room = calculate_area(5, 6)
# print(f"The area of my room is {my_room} square meters.")
# print(type(my_room))


number_power_itself = lambda x: x ** x

print(number_power_itself(2))
