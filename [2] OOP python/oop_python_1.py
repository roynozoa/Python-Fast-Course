# Object Oriented Programming in python
# This source code is my practical learning for object oriented programming in python
# Muhammad Adisatriyo Pratama - October 2020


# (1) Objects

print(type('Hello World'))  # printing type for 'Hello World'
# 'Hello World' is an object of the 'str' class


print(type(1))  # 1 is an object of the 'int' class


def print_function():
    print('Print Function')


# print_function is an object of the 'function' class
print(type(print_function))

# Everything in python is an object of a specific class
# We can create a specific class in order to create a specific object with OOP concept
# Two type of class is 'built in class' and 'manually created class'


# (2) Methods
# method is a function that has a specific purpose to its own class
# method naming uses snake_case
# every class have its own method
# some methods has an arguments on it
# exemple of method .upper() in 'str' class

basic_str = 'lower'
print(basic_str.upper())  # make basic_str into upper case


# (3) Class
# Class is a blueprint for an objects
# class naming in python uses CamelCase with capital first word (PascalCase)
# multiple method can be defined inside of a class


# create a basic class called Cat
class Cat:

    # method meow inside of a Cat class
    # this method has a parameter called self
    def meow(self):
        print('meow')


kucing_garong = Cat()  # 'kucing_garong' now is an object from a class Cat

# 'kucing_garong' is a class Cat, __main__ is a default naming module
print(type(kucing_garong))

kucing_garong.meow()  # usage of meow() method in Cat class


# creating another clas
class Car:
    # special method
    # this method will be called whenever an object is creaeted
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    # getter method to access name or speed of a Car object
    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed

    # setter method to modify name or speed of a Car object
    def set_name(self, name):
        self.name = name

    def set_speed(self, speed):
        self.speed = speed

    # basic method that print specific value
    def vroom(self):
        print('VROOOOOM')


print('=======')


# create an object from Car class
car_example = Car('BMW', 180)
print(car_example.get_name(), f'{car_example.get_speed()} KM/hour')
