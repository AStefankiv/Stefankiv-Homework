# HW 2

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

n = int(input("Enter a position in Fibonacci sequence: "))
result = fibonacci(n)
print(f"The Fibonacci number at position {n} is {result}.")