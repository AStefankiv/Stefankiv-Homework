# Написати функцію, яка повертає тільки однакові елементи двох множин.
x = {1, 2, 3, 4, 5, 6, 7}
y = {4, 5, 6, 7, 8, 9, 10}
def coinside(x, y):
    print(x.intersection(y))
    return x.intersection(y)

coinside(x, y)

# Написати функцію, яка повертає тільки унікальні елементи двох множин.
def unique_items(x, y):
    print(x.symmetric_difference(y))
    return x.symmetric_difference(y)

unique_items(x, y)

# Перетворити всі елементи списку типу string в верхній регістр, використовуючи map.
class_names = ("Andrew", "Misha", "Tolik", "Olena", "Daryna")
def uppercase(name):
    print(name.upper())
    return name.upper()

for item in map(uppercase, class_names):
    print(item)

# Вивести всі елементу масиву, які є числом, використовуючи filter.
data = (1, 2, 3, "sweetapple", 4, 5, 6, 7, 8, 9, "cherry", "berry")

def numbs(number):
    return isinstance(number, (int))

only_numbers = filter(numbs, data)
for item in only_numbers:
    print(item)
print(filter(numbs, data))