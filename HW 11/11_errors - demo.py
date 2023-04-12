
# for a in(1, 2):
#     print(a)

# if True:
#     print("This is true")
#     print("This is true")

# print("text" / 1)

# lst = [1, 2]
# print(lst[1])

# dct = {"test": 1}
# print(dct["test"])

# while True:
#     pass

# lst = [1, 2]
# lst_iter = iter(lst)
# print(next(lst_iter))
# print(next(lst_iter))

# int("test")

# lst = [1, 2]
# tpl = tuple(lst)
#
# lst.append(1)
# "asd".startswith("a")
#
# print(dir(lst))

# try:
#     print("This is try")
# except Exception:
#     print("Exception")

# try:
#     zero = 1 / 0
# except ZeroDivisionError:
#     print("Zero division is impossible")

# try:
#     zero = 1 / 0
# except TypeError:
#     print("Wrong type")

# dct = {"key": 1}
#
# try:
#     print(dct["key1"])
# except Exception:
#     print("Key does not exist")

# try:
#     print(1 / 0)
# except ZeroDivisionError as zde:
#     print(zde)
#     print("Zero division")

# try:
#     print(1 / 0)
# except Exception as e:
#     print(type(e).__name__, e)

import time
#
# phone_book = {"Andrii": +14039984704}
# counter = 5
#
# while counter:
#     name = input("Enter a name: ")
#     try:
#         print(phone_book[name])
#         break
#     except KeyError:
#         print(f"Key {name} does not exist")
#     finally:
#         time.sleep(3)
#         print("Try again")
#         counter -= 1
# print("You have reached the limit. Restart the program.")

# phone_book = {"Andrii": +14039984704}
# counter = 5
#
# while counter:
#     name = input("Enter a name: ")
#     try:
#         value = phone_book[name]
#         print(value)
#         break
#     except KeyError:
#         print(f"Key {name} does not exist")
#     else:
#         print(phone_book[value])
#     finally:
#         counter -= 1
# print("End of the program.")

# pin = 1234
# # max_tries = 3
# # permission = False
# #
# # while permission is False and max_tries > 0:
# #     try:
# #         user_pin = int(input("Enter a pin: "))
# #     except ValueError:
# #         print("Pin should contain only digits")
# #     else:
# #         if user_pin == pin:
# #             print("Pin is correct")
# #             permission = True
# #     finally:
# #         if permission:
# #             print("Permission granted")
# #             break
# #         max_tries -= 1
# #         print(f"{max_tries} attempts left. Permission denied")
# #         time.sleep(3)

class MyException(Exception):
    pass

raise MyException("This is a test for exception")