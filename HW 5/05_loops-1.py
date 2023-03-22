text = input("Enter some text: ")

for char in text:
    if char.isdigit():
        if int(char) % 2 == 0:
            print(f"{char} is an even number")
        else:
            print(f"{char} is an odd number")
    elif char.isalpha():
        if char.isupper():
            print(f"{char} is an uppercase letter")
        else:
            print(f"{char} is a lowercase letter")
    else:
        print(f"{char} is a symbol")