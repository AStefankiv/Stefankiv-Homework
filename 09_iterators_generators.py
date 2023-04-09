# string = "I love Python"
# string_iterator = iter(string)
# print(type(string_iterator))
# print(next(iter(string_iterator)))
# print(next(iter(string_iterator)))
# print(next(iter(string_iterator)))
# print(next(iter(string_iterator)))
# print(next(iter(string_iterator)))
# print(next(string_iterator))
# print(next(string_iterator))
# print(next(string_iterator))
# print(next(string_iterator))
# print(next(string_iterator))
# print(next(string_iterator))
# print(next(string_iterator))
# print(next(string_iterator))

# for item in string:
#     print(item)

# my_list = [0, 1, 2, 3, 4, 5, 6, 7]
# my_list_iterator = iter(my_list)
# print(next(my_list_iterator))
# print(next(my_list_iterator))
# print(next(my_list_iterator))
# print(next(my_list_iterator))
# print(next(my_list_iterator))

# def my_generator_function(size):
#     value = 0
#     while value < size:
#         yield value
#         value += 1
#
# gen = my_generator_function(5)
#
# print(my_generator_function)
# print(gen)

# for item in gen:
#     print(item)

# class MyIterator:
#     value = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value == 6:
#             raise StopIteration()
#
#         result = self.value
#         self.value += 1
#         return result

# my_iterator_object = MyIterator()
# print(my_iterator_object)
#
# print(next(my_iterator_object))
# print(next(my_iterator_object))
# print(next(my_iterator_object))
# print(next(my_iterator_object))
# print(next(my_iterator_object))

# for item in my_iterator_object:
#     print(item)

# import os
#
# class FileIterator:
#
#     def __init__(self, path):
#         self.path
#         self.files = os.listdir(path)
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.files):
#             raise StopIteration
#
#         file_name = self.files[self.index]
#         self.index +=1
#         return file_name
#
# dir_iter = FileIterator("C:\Users\Hp\PycharmProjects")
# for file in dir_iter:
#     print(file)

# def my_function():
#     return 1

# import random
#
# def random_numbers():
#     while True:
#         yield random.randint(1, 100)
#
# rand_gen = random_numbers()
# for i in range(3):
#     print(next(rand_gen))

# def read_large_file(file_path):
#     with open(file_path) as f:
#         chunk = f.read(1024)
#         if not chunk:
#             break
#         yield chunk
#
# reader = read_large_file("largefile.txt")
# for i in range(5):
#     print(next(reader))

# lst = range(10)
# data = {"one": 1, "two": 2}
#
# gen_lst = [f for f in lst]
# gen = (f for f in lst)
# gen_set = {f for f in lst}
# gen_dict = {key: value for key, value in data.items() if value != 1}

# print(gen_lst)
# print(gen)
# print(gen_set)
# print(gen_dict)

# print(type(gen_lst))
# print(type(gen))
# print(type(gen_set))
# print(type(gen_dict))

# lst = range(2 ** 5)
# from sys import getsizeof
#
# print(getsizeof([f for f in lst]))
# print(getsizeof((f for f in lst)))
# print(getsizeof({f for f in lst}))
# print(getsizeof({f for f in lst}))

def sub_generator():
    for i in range(3):
        yield i

def main_generator():
    yield from sub_generator()
    yield "Done"

for val in main_generator():
    print(val)