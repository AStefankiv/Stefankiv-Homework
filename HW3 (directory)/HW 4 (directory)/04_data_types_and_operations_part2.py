input_text = input("Enter some text: ")

if input_text.isdigit():
    number = int(input_text)
    if number % 2 == 0:
        print("The input is a number and it's even")
    else:
        print("The input is a number and it's odd")
elif input_text.isalpha():
    print("The input is a word and it's length is", len(input_text), "letters")
else:
    print("The input is neither a number nor a word")