import time

# print("--- 1. THE CONCEPT: FUNCTIONS ARE OBJECTS ---")


# Before understanding decorators, you must know that functions
# can be passed around just like variables.
def greet():
    return "Hello!"


def shout(func_argument):
    # We execute the function passed in, then modify the result
    message = func_argument()
    return message.upper()


# print(f"Function output: {greet()}")
# print(f"Passed into another function: {shout(greet)}")

# print(f"\n--- 2. BUILDING A DECORATOR MANUALLY ---")


# A decorator is just a function that takes a function and returns a NEW function (the wrapper).
def simple_logger(original_func):
    # The 'wrapper' adds functionality before/after the original function
    def wrapper():
        print(f"LOG: About to run '{original_func.__name__}'...")
        original_func()
        print(f"LOG: Finished running '{original_func.__name__}'.")

    return wrapper


def do_task():
    print(">> I am doing the task.")


# The manual way to apply a decorator (what Python does behind the scenes):
# do_task = simple_logger(do_task)
# do_task()

# print(f"\n--- 3. THE SYNTAX SUGAR (@) ---")


# This does EXACTLY the same thing as step 2, but it's cleaner.
@simple_logger
def do_another_task():
    print(">> I am doing another task.")


# do_another_task()

# print(f"\n--- 4. HANDLING ARGUMENTS (*args, **kwargs) ---")


# If the original function has arguments (a, b), the wrapper needs them too.
# We use *args and **kwargs to accept ANY arguments.

def smart_divide_decorator(func):
    def wrapper(a, b):
        print(f"Checking if {b} is zero...")
        if b == 0:
            print("Error: Cannot divide by zero!")
            return None  # We intercept the crash
        return func(a, b)  # We pass the arguments to the original function

    return wrapper


@smart_divide_decorator
def divide(x, y):
    return x / y


# Testing safe division
# print("Result 10/2:", divide(10, 2))
# print("Result 5/0:", divide(5, 0))

print(f"\n--- 5. THE 'REAL WORLD' TEMPLATE ---")


# A robust decorator must:
# 1. Accept any arguments (*args, **kwargs).
# 2. Return the value of the original function (result).

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        # EXECUTE the original function and capture the result
        result = func(*args, **kwargs)

        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")

        # RETURN the result back to the caller
        return result

    return wrapper


@timer_decorator
def complex_calculation(n):
    total = 0
    for i in range(n):
        total += i
    return total


# Run calculation
calc_result = complex_calculation(100000)
print(f"Calculation Result: {calc_result}")