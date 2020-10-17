# Part 2 of my fast course in learning python


# (9) if/else/if conditional statement

user_name = input('Name: ')

if user_name == 'Roy':
    print('That is my name, Roy!')
elif user_name == 'Tim':
    print('That is a good name')
elif user_name == 'Joe':
    print('That is also a good name')

else:
    print('Not my name bruh')

# if user_name == 'Tim':


# (10) Collection(list and tuples)

list_in_python = [12, False, 'Hello World']  # this is list
print(len(list_in_python))
list_in_python.append('Add elements to the end of the list')
print(list_in_python)
# Remove last element in the list,
# you can add index to remove specific element on the list
list_in_python.pop()  # .pop(0) : remove at index 0
print(list_in_python)

print(list_in_python[1])

list_in_python2 = list_in_python  # copy reference to the list

print(list_in_python2 == list_in_python)

# tuples is similar to list but immutable
tuple_x = (12, 2, 3, 4)
# tuple_x[0] = 20 you cannot do this because of immutable but can access it
# You can put list and/or tuple inside of a list

# (11) For loops
# while loop is running indifine ammount of time
# For loop running specific ammount of time

# input in range : start, stop, step
for i in range(10):  # 1 argument stop at 10
    print(i)

print('=====')

for j in range(2, 10):  # 2 arguments start at 2 stop at 10
    print(j)

print('=====')

for k in range(20, 9, -1):  # 3 arguments start at 20, stop at 9, -1 step
    print(k)

# the loop immediately stop when condition in range already happened

print('=====')

# for loop in the list
for list_num in [32, 541, 1, 9, 100, 99]:
    print(list_num)

print('=====')
# or you can to this
random_list = [32, 541, 1, 9, 100, 99]

for list_1 in range(len(random_list)):
    print(random_list[list_1])
print('=====')

# (12) While loops
loop = 0
while True:
    loop += 1
    print('Hello loop', loop)
    if loop == 10:
        break

# (13) Sliced Operator
# sliced = [start:stop:step], similar to range in for loops
# also can be used in tuple

list_of_num = [0, 1, 2, 3, 4, 5, 53, 32, 123, 431, 23]
list_of_string = ['Hello', 'World', 'Roy', 'Haia', 'Howdy', 'Doody', 'Alright']
string_s = "Babadaboobi"

sliced = list_of_string[0:5:1]
print(sliced)

sliced_2 = list_of_num[::-1]  # Reverse list order
print(sliced_2)
