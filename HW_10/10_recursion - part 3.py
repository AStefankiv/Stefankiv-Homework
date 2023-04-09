# HW 3
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# print(factorial(4))

enter_factorial_num = int(input("Enter factorial number: "))
result = print(factorial(enter_factorial_num))