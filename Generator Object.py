# Generator Object

from sys import getsizeof  # size of items will be readable


#Generator in array
values = [x*30 for x in range(100000000)]
print("generator:", getsizeof(values))

#Generator in list
values = (x*30 for x in range(100000000))
print("generator:", getsizeof(values))
