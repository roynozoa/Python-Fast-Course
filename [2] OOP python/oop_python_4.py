# Part 4 of my OOP python practical learning source code


# (5) Class instances and classmethod
# make Person class

class Person:
    person_counter = 0  # usually for a constant value inside of a class

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Person.add_person()  # call method inside of a Person class

    @classmethod
    def number_of_people(cls):
        return cls.person_counter

    @classmethod
    def add_person(cls):
        cls.person_counter += 1


p1 = Person(1, 'Roy')
p2 = Person(2, 'K')
p3 = Person(3, 'K')
p4 = Person(69, 'Roy KK')
print(Person.number_of_people())  # display number of people


# (6) Static method
# method that don't have an access to an instance
# static method will do something but don't change anything


# example
class Calculator:

    # define static method
    @staticmethod
    def add100(x):
        return x + 100

    @staticmethod
    def mul2(x):
        return x*2

    @staticmethod
    def pow2(x):
        return x*x


# don't need to create an object to call a method
print(Calculator.add100(1), Calculator.mul2(2), Calculator.pow2(23))
