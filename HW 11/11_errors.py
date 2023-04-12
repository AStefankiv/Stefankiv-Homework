import time

phone_number_book = {
    "Mother": "403 123 45 67",
    "Father": "403 098 76 54",
    "Sister": "403 555 66 66",
    "Brother": "403 999 88 77",
    "Wife": "403 333 44 55",
    "Daughter": "403 990 00 11"
}
counter = 2
while counter:
    name = input("Enter a name: ")
    try:
        print(phone_number_book[name])
    except KeyError:
        print(f"Information about {name} wasn't found.")
    finally:
        time.sleep(2)
        print("Enter a name again")
        counter -= 1
print(f"Information about {name} and one's phone number -{phone_number_book[name]}- was found.")

# Teacher! I was searching for 2 names: Wife and Sister, but only the last name is outputted at the end. How can I make more than one name that I was searching be printed/outputted???