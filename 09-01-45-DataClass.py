# DataClass

from collections import namedtuple  # this import used in Soloution 2

# Soloution 1 for saving data in Class:


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
# location in RAM:
print(id(p1))
print(id(p2))
# if p1 and p2 about their data are equal:
print(p1 == p2)
# -----------------------
# Soloution2 for saving data in class:

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
