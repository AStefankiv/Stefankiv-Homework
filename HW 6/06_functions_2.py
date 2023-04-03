# Task 2 - Create a function which sums all the arguments and returns the result
def sum_all(*args):
    return sum(args)
print(sum_all(9, 6, 66, 776))

user_data = input("Enter the number to sum: ")
numbers = [int(item) for item in user_data.split(", ")]
result = sum_all(*numbers)
print("Total: ", result)
