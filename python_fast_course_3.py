# Part 3 of my fast course in learning python

# (14) Sets, very similar with list and tuple
x = set()  # this is set but it's empty
s = {3, 123, 545, 323, 5}  # this is also set
s.add(5)  # you can add an elemet into the set
print(s)
print(123 in s)  # Return a boolean value (check if 123 is in set s)
x.add(1)
x.add(5)
print(x)

# you can do UNION/INTERSECT operation with sets
print('Intersect of set s and x', s.intersection(x))
print('Union of set s and x', s.union(x))
print('=====')


# (15) Dictionaries
# similar to hash table in other programming languages

dictionaries1 = {'key': 'value'}  # Dict variable need key and value in it
print(dictionaries1['key'])  # how to print key dictionaries

dictionaries1[2] = ['Dictionaries 2', 2, "two", 222]  # add key to dicts
dictionaries1['three'] = 3  # key do not have to be the same data type
print(dictionaries1)

print(list(dictionaries1.values()))  # put dictionaries into a list datatypes
print(list(dictionaries1.keys()))  # put dict keys into a list
print('key' in dictionaries1)  # check if key is in a dictionaries
print('=======')

# for loop using dicts
i = 0
for dict_key, dict_value in dictionaries1.items():
    i += 1
    print(i, '|', dict_key, '|', dict_value)
    print('=======')


print('Another for loop approach')
j = 0
for dict_key in dictionaries1:
    j += 1
    print(j, '|', dict_key, '|', dictionaries1[dict_key])
    print('=======')

del dictionaries1['key']  # detele key in dict
print(dictionaries1)
print('=======')


# (16) Comprehensions
# only python have comprehensions

list_x = [x for x in range(100)]  # put for loop into a list
print(list_x)
list_zero = [0 for x in range(100)]
print(list_zero)
print('=======')

# 2 dimensional list with for loops
list_2d = [[1 for x in range(5)] for x in range(5)]
print(list_2d)
print('=======')

# dict using comprehensions
comp_dict = {j: 'val' for j in range(100)}
print(comp_dict)
print('=======')

# tuple using comprehensions
comp_tuple = tuple('tuple' for j in range(10))
print(comp_tuple)
