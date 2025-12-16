print("Welcome to the class!")


# This is a single-line comment. Python skips this line.
print("Hello, World!") # You can also put comments at the end of a line.

'''
This is a multi-line comment.
I can write a whole paragraph here explaining
that this program calculates the trajectory of a rocket.
'''


# Create a box named 'user_name' and put the text "Ayham" inside it
user_name = "Ayham"

# Create a box named 'score' and put the number 10 inside it
score = 10

# Look inside the box and print what is there
print(user_name)  # Output: Ayham

# CHANGE the value. Take 10 out, put 20 in.
score = 20
print(score)      # Output: 20


# String (str): Text. Must be surrounded by quotes ("Hello" or 'Hello').
#
# Integer (int): Whole numbers (1, 50, -10). No decimals.
#
# Float (float): Floating point numbers (decimals) (1.5, 3.14).
#
# Boolean (bool): Logic values. Only two exist: True or False.


name = "Sarah"       # String
age = 25             # Integer
height = 1.75        # Float
is_student = True    # Boolean

# You can check the type using the type() function
print(type(age))     # Output: <class 'int'>

##################################################################################
# We want to do complex math, but we don't know how to calculate Pi manually.
import math

# Now we can use the tools inside the 'math' toolkit.
print(math.pi)            # Output: 3.14159...
print(math.sqrt(16))      # Output: 4.0

# We can also import tools to pick random numbers
import random

print(random.randint(1, 10)) # Pick a random number between 1 and 10

my_none = None
print(my_none)

my_complex = 1 + 2j
print(my_complex)