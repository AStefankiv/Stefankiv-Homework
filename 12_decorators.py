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
    def __enter__(self):
        print("==========")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("==========")
        if exc_type == KeyError:
            print(f"Key {exc_val} does not exist")


with MyManager():
    print("Something inside my context manager")

# HW - 3

def decorator_time_name(times):
    def wrapper_1(func):
        def wrapper_2(*args, **kwargs):
            for i in range(times):
                start_time = time.strftime('%d-%m-%Y %H:%M:%S')
                result = func(*args, **kwargs)
                print(f"Function {func.__name__} was launched at {start_time}")
            return result
        return wrapper_2
    return wrapper_1

@decorator_time_name(times=3)
def simple_function():
    print("What's the function's name and the time?")

simple_function()