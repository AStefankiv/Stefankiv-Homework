# - Task 1 - This is the function that allows to turn an input number into a prime number
def prime_power(a):
    return a*a

prime_number = int(input("Enter prime number: "))    #can also be float
result = prime_power(prime_number)
print("The prime number is: ", result)