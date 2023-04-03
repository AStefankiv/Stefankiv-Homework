# new_set = set()
# dict_not_set = {}
# print(f"set type: {type(new_set)}\n dict type: {type(dict_not_set)}")
#
# num_set = {1, 2, 3}
# print(num_set)

# num_set = set(range(10))
# num_set.add("asd")
# num_set.add("aaaaaaa")
# print(num_set)

# num_set.remove(1)
# num_set.remove(0)
# print(num_set)

# name_list = ["Ivan", "Oleg", "Andrii", "Linh", "Ivanna", "Volodymyr", "Volodymyr"]
# unique_names_list = list(set(name_list))
# print(unique_names_list)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print(set1 | set2)
# print(set1 & set2)
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1 - set2)
# print(set2 - set1)
# print(set2.difference(set1))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))
# print(set2.symmetric_difference(set1))

# duplicate_list = frozenset([1, 2, 3, 4, 4, 5, "asdedasd", "Andrii", (1, "123")])
# cortezh = tuple(duplicate_list)
# frozen_set = frozenset(duplicate_list)
# print(cortezh)
# print(frozen_set)
# print(type(frozen_set))
# print(len(frozen_set))

def power(number):
    print(f"Argument of function: {number}")
    return number ** 2

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in map(power, lst):
    print(item)