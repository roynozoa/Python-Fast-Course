# Part 3 of my fast course in learning python

# (17) Function in python
# def keyword to define a function in python

def function_add(a, b):
    return a + b


def function_sub(a, b):
    return a - b


# return multiple values in function as a tuple
def tuple_calc(a=0, b=0):  # default value = 0
    return a + b, a - b, a * b, a / b


add = function_add(10, 19)
sub = function_sub(19, 10)

# put into a variable one by one
# tuple_add = tuple_calc(10, 10)[0]
# tuple_sub = tuple_calc(20, 10)[1]
# tuple_mul = tuple_calc(10, 10)[2]
# tuple_div = tuple_calc(100, 10)[3]

# put each index into a variable in order
tuple_add, tuple_sub, tuple_mul, tuple_div = tuple_calc(100, 10)

result = 'Result', str(tuple_add), str(
    tuple_sub), str(tuple_mul), str(tuple_div)


print('10 + 19 = ', add, '\n', '19 - 10 = ', sub)
print(str(result))
print('=======')

# (18) Unpack Operator / *args and **kwargs


# example how to call function inside a function
def func1(a):
    def func2():
        print(a)

    return func2


b = func1(100)
b()  # need to do this because b is a func2 and called it
# or
c = func1(200)()

# unpack with *
d = [561, 245, 3, 34, 95]
print(d)  # print d as a list data type
print(*d)  # print d individually (unpacking)


# unpack operator for function
def pair_func(x, y):
    print(x, y)


pairs = [(1, 2), (3, 4)]

for pair in pairs:
    pair_func(*pair)  # use the unpack operator for pairs


# use in dict
pair_func(**{'x': 2, 'y': 2})
print('=======')


# *args and **kwargs in function
def func_args(*args, **kwargs):
    print(args, kwargs)


func_args(1, 2, 3, 4, 5, 6, one=1, two=2, zero=0)
print('=======')


# (19) Scope and Globals

user_name = 'Roy'


def change_name(new_name):
    # global variable to access user_name outside the function but better not use it or create new variables instead
    global user_name
    user_name = new_name


print(user_name)
change_name('Name Changed')
print(user_name)
print('=======')


# (20) Exceptions
# example raise situation
# raise Exception('Data Not Found')
# raise FileExistsError('asd')


# (21) Handling Exceptions
# using try except finaly


# basic try except finally
try:
    x = 4/0
except Exception as e:
    print(e)
finally:  # finally block will run no matter what happen in exception
    print('Run no matter what happen')
print('=======')


# (22) Lambda
# lambda is one line anonymous function


# basic use of lambda
def lambda_function(x, y): return x + y


print(lambda_function(10, 10))
print('=======')


# (23) Map and Filter
# this feature make use of the lambda function


# make a list
list_one = [4, 34, 1324, 5, 6, 7, 34, 6, 7, 1, 3, 7,
            8, 2, 56745, 4, 6, 8, 8, 3, 5, 6, 8996, 56, 5, 6]


# create a variable with map function that multiply 2 to every single value in list_one
map_function = map(lambda i: i * 2, list_one)
print(list(map_function))
print('=======')

# filter function
# Filtering list_one that can be divided by two and put it into filter_function
filter_function = filter(lambda i: i % 2 == 0, list_one)
print(list(filter_function))


# (24) F strings
# new features in python 3.6


# F string uses
user_name = 'Roy'
# Put variables inside of strings
f_string = f'Hi {user_name}, how are you today? Did you know that 8 + 2 is {8+2}??'
print(f_string)


# That is the end of the basic tutorial for python
# Copyright (C) 2020 Muhammad Adisatriyo Pratama
