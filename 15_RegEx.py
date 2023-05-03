import re

# HW 1

phone_number_book = {
    "Mother": "+380111222333",
    "Father": "380444555666",
    "Sister": "0777888999",
    "Brother": "4039998877",
    "Wife": "403333",
    "Daughter": "41399111111"
}
new_phone_list = []
for phone_number in phone_number_book.values():
    validate = re.search(r"(\+?3?8)?(0\d{9})", phone_number)
    if validate:
        new_phone_list.append(validate.group(0))

print(new_phone_list)


# HW 2

with open("text_emails.txt", 'r') as edit_emails:
    change = edit_emails.read()

new_replace = change.replace("email", "@")

with open("text_emails.txt", 'w') as edit_mail:
    edit_mail.write(new_replace)