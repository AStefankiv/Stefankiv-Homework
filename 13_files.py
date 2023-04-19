# HW 1

import json
import time

phone_number_book = {
    "Mother": "403 123 45 67",
    "Father": "403 098 76 54",
    "Sister": "403 555 66 66",
    "Brother": "403 999 88 77",
    "Wife": "403 333 44 55",
    "Daughter": "403 990 00 11"
}

json_data = json.dumps(phone_number_book)
with open("phone_book.json", "x") as file:
    file.write(json_data)
    print(json_data)

# HW 2
def decorator_time_name(func):
    def wrapper(*args, **kwargs):
        start_time = time.strftime('%d-%m-%Y %H:%M:%S')
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} was launched at {start_time}")
        log_entry = {"Function name": func.__name__, "Call time": start_time}
        with open("phone_book.json", "a") as log_file:
            log_file.seek(0, 2)
            log_json = json.dumps(log_entry)
            log_file.write(log_json)
            log_file.write("\n")
        return result
    return wrapper

@decorator_time_name
def simple_function():
    print("What's the time and function's name?")

simple_function()