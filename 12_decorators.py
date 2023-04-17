# HW - 1

import time

def decorator_time_name(func):
    def wrapper(*args, **kwargs):
        start_time = time.strftime('%d-%m-%Y %H:%M:%S')
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} was launched at {start_time}")
        return result
    return wrapper

@decorator_time_name
def simple_function():
    print("What's the time and function's name?")

simple_function()

@decorator_time_name
def multiply_add_function(a, b, c):
    return a * b + c

print(multiply_add_function(3, 4, 5))

# HW - 2

class MyManager:

    print("==========")
    def __enter__(self):
        print("Enter method")
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit method")

    print("==========")

# HW - 3

def decorator_time_name(func):
    def wrapper(times):
        start_time = time.strftime('%d-%m-%Y %H:%M:%S')
        result = func(times)
        for i in range(times):
            print(f"Function {func.__name__} was launched at {start_time}")
        return result
    return wrapper

@decorator_time_name
def simple_function(*args):
    print("What's the time and function's name?")

simple_function(6)