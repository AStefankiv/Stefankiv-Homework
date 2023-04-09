# Homework 1
def recursion(n: int) -> None:
    print(n, end=" ")
    if n == 0:
        return None
    return recursion(n - 1)

enter = int(input("Enter any number: "))
result = recursion(enter)