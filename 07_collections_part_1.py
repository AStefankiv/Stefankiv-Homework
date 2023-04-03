# # Створити телефонну книгу, яка матиме наступні команди:
# phone_number_book = {
#     "Mother": "403 123 45 67",
#     "Father": "403 098 76 54",
#     "Sister": "403 555 66 66",
#     "Brother": "403 999 88 77",
#     "Wife": "403 333 44 55",
#     "Daughter": "403 990 00 11"
# }
# print(phone_number_book)
#
# # : кількість записів
# print(len(phone_number_book))
#
# #add: додати запис
# phone_number_book["My number"] = "403 998 4704"
# print(phone_number_book)
#
# # delete <name>: видалити запис за іменем (ключем)
# del phone_number_book["Brother"]
# print(phone_number_book)
#
# # list: список всіх імен в книзі
# print(list(phone_number_book)) #or
# print(phone_number_book.keys())
#
# # show <name>: детальна інформація по імені
# print(phone_number_book.items())

phone_number_book = {
    "Mother": "403 123 45 67",
    "Father": "403 098 76 54",
    "Sister": "403 555 66 66",
    "Brother": "403 999 88 77",
    "Wife": "403 333 44 55",
    "Daughter": "403 990 00 11"
}
while True:
    command = input("Enter command: ")
    if command == "stats":
        print("Number of records:", len(phone_number_book))
    elif command == "add":
        name = input("Enter name: ")
        number = input("Enter number: ")
        phone_number_book[name] = number
        print("Record added")
    elif command == "delete":
        remove = input("Enter the name to delete: ")
        del phone_number_book[remove]
        print(f"{remove} was deleted.")
    elif command == "list":
        print(list(phone_number_book))
    elif command == "show":
        all_info = input("Enter name in phonebook: ")
        phone_number = phone_number_book.get(all_info)
        if phone_number:
            print(f"The phone number of {all_info} is {phone_number}")
        else:
            print(f"Sorry, there is no information about {all_info}")
    else:
        print("Incorrect command")