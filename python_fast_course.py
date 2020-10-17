# Python speed course
# My code repository for learning python
# Muhammad Adisatriyo Pratama - October 2020

# (1) Data Types : int (123123, -5452, etc), Float (421.0, -4.5, 53.4), String ("Hi", 'Hello'),
# Bool (True, False)

# (2) Output and Printing
print(5.4, "My name is roy", '4.5')
print("Babadaboobi", end=' | ')
print("Howdy")

# (3) Variables
word = 'Howdy Doody'
print(word)
# variable in python usually will use snake case e.g (data_science) NOT camel case (dataScience)
# cannot start variable with number or using (space bar char)

# (4) User Input
user_name = input('Name: ')
user_age = input('Age: ')
print("Hello", user_name, "you are", user_age, "years old")


# (5) Arithmetic Operator
# Note : both operands data type must be same
x = 12
y = 453

result_addition = x + y
result_subtraction = x - y
result_multiple = x*y
result_division = x/y
result_int_division1 = int(y/x)  # make result in int data types
result_int_division2 = y//x
result_exponent = x ** 3
result_modulus = y % x  # give the remaining division as a result

print(result_addition, result_subtraction, result_multiple,
      result_division, result_int_division1, result_int_division2, result_exponent, result_modulus)

# Orders of Operation : Bracket, Exponents, Division, Multiplication, Addition, Subtraction

user_num = input('Number: ')
# Python sees user input as a string so to do operation must change data types into int or float
print(int(user_num) - 5)


# (6) String Methods, and Operators

string_method = 'thiS Is String'

print(string_method.upper(), string_method.lower(),
      string_method.capitalize(), string_method.lower().count('i'))

x = 'Roy'
y = 4
z = 'Hello '

print(x * y)  # String multiplication
print(z + x)  # String addition

# (7) Conditional Operators
# == (equality), != (not equal), <=  (less than equal), >=  (greater than equal), <  (less than), >  (greater than)
string_one = 'babadaboopi'
string_two = 'babadaboopi'
string_three = 'Babadaboopi'

print(string_one == string_two, string_one !=
      string_two, string_one != string_three)

print(7.4 > 7, 7.4 == 4, 88 < 100.4, 67 <= 67)

# (8) Chained Conditional

variable_x = 7
variable_y = 8
variable_z = 0

result1 = variable_x == variable_y
result2 = variable_y > variable_x
result3 = variable_z < variable_x + 4


# boolean operator : and, or, not

print(result1 and result2)
print(result1 or result2)
print(result3 and result2)
