# Intermediate Programming in python
# This source code is my practical learning programming in python
# Muhammad Adisatriyo Pratama - October 2020


# (1) Import statement and working with dates (use and format date)

# import datetime module in python
from datetime import datetime
from datetime import date

import math  # import library in python
# another example
from math import pi  # (only import certain module)
string = 'Hello World'
print(string.upper())  # example of a built in function in python
print(math.pi, math.cos(1))  # usage of the math library in python


def area_of_circle(r):
    return r*r*pi  # using 'pi' instead of math.pi


print(f'Area of a circle with 10 radius = {area_of_circle(10)}')
print('================')


# Dates
print(datetime.now())  # print current date and time
print(date.today())  # print current date
print(datetime.now().time())  # print current time
print('================')


# Formatting dates
# %d = date of month, %m = month(num), %b = month name (short),
# %B = month name, %Y = year, %M = minutes, %S = seconds
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # dd/mm/YYYY HH:MM:SS
now2 = datetime.now().strftime("%d-%b-%Y %H:%M:%S")  # dd-bbb-YYYY HH:MM:SS
print(now)
print(now2)
