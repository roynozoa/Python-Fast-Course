# Part 3 of my OOP python practical learning source code


# (4) Inheritance
# 2 class that is simmilar this class will inherit from parent class
# example are class Car and Motorcycle that inherit from Vehicle class
# Vehicle is general class, Car and Motorcycle are specific class


# Parent class Vehicle
class Vehicle:
    def __init__(self, name, max_speed, brand):
        self.name = name
        self.max_speed = max_speed
        self.brand = brand

    def show(self):
        print(
            f'Name      :{self.name}\nMax Speed :{self.max_speed}\nBrand     :{self.brand}')


# Car class inherit some attributes from Vehicle class
class Car(Vehicle):
    def __init__(self, name, max_speed, brand, color):
        super().__init__(name, max_speed, brand)
        self.tire = 4
        self.color = color

    def sound(self):
        print('Vroom')

    def show(self):
        print(
            f'Name      :{self.name}\nMax Speed :{self.max_speed}\nBrand     :{self.brand}\nColor     :{self.color}')


# Motorcycle class also inherit some attributes from Vehicle class
class Motorcycle(Vehicle):
    def __init__(self, name, max_speed, brand, color):
        super().__init__(name, max_speed, brand)
        self.tire = 2
        self.color = color

    def sound(self):
        print('Broom')

    def show(self):
        print(
            f'Name      :{self.name}\nMax Speed :{self.max_speed}\nBrand     :{self.brand}\nColor     :{self.color}')


# Truck class
class Truck(Vehicle):
    def __init__(self, name, max_speed, brand):
        super().__init__(name, max_speed, brand)


# Bike class
class Bike(Vehicle):
    def __init__(self, name, max_speed, brand):
        super().__init__(name, max_speed, brand)
        self.tire = 2


# creating an object
print("===== VEHICLE AUTOMOTIVE SHOW =====")
v = Vehicle("Combine Harvester", 50, "John Deere")
v.show()

print("===================================")
c = Car("BMW i3", 360, "BMW", "Black")
c.show()
c.sound()

print("===================================")
m = Motorcycle("Honda CBR250RR", 100, "Honda", "Red")
m.show()
m.sound()
