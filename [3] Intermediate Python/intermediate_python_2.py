# Part 2 of my intermediate python practical learning source code


# (2) Counter, Named Tuples, and Deque (Python collection)

import collections
from collections import Counter
from collections import namedtuple
from collections import deque

# Counter

c1 = Counter('hello')  # string inside counter
c2 = Counter(['h', 'i'])  # list inside counter
c3 = Counter({'h': 1, 'i': 2})  # dict inside counter
c4 = Counter(car=5, bike=2, bicycle=3, truck=1)  # keyword inside counter
print(type(c1))  # class 'collection.Counter'

print(c1)
print(c2)
print(c3)
print(c4)
print("=======")

print(list(c3.elements()))  # print each elements in counter
print(list(c4.elements()))


print(c4.most_common(3))  # print n (3) most common keywords in counter

# create a list
list1 = ['car', 'car', 'truck', 'train']
# subtracting c4 with list1 (can be used with any container data types)
c4.subtract(list1)
print(c4)
# update c4 with list1
# (similar with subtracting but instead of subtract, update will add to counter)
c4.update(list1)  # similar with original data
print(c4)
c4.clear()  # clear counter (delete all data)
print(c4)  # counter empty


# Named Tuple
# named tuple can access element inside a tuple

# point tuple
Point = namedtuple('Point', ['car', 'truck', 'bike'])
new_p = Point(1, 2, 3)
print(new_p)
print(new_p.car, new_p.truck)  # access tuple element by index name
print("=======")

# Deque
# faster than list data types


dq = deque('hello world')
print(dq)
dq.append('a')  # add to deque
dq.appendleft('a')  # add to front of deque
print(dq)
dq.pop()  # remove last value in deque
dq.popleft()  # remove first value in deque
print(dq)

dq.clear()  # clear deque (empty)
print(dq)

dq.extend('doody')  # extend deque
dq.extendleft(' ydwoh')  # reverse order
print(dq)


dq2 = deque('howdy', maxlen=5)  # deque with maximum capacity of 5
print(dq2)
# every append that happen will remove left/popleft if the capacity reach maxlen
dq2.append(1)
print(dq2)
