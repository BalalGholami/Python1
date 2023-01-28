# Objects Comparation

# classes contains ATTRIBUTE and FUNCTION (METHOD)
class MyPoint:
    def __init__(self, x, y):  # constructor , with a MAGIC FUNCTION
        # self: is a location in RAM that contains object
        self.x = x
        # or: input("Enter x: ")  # we do not want use x from main function
        self.y = y
        # or: input("Enter y: ")  # we do not want use y from main function

    def draw(self):  # all of the functions of class must have a parameter and its name is better been 'self'
        print(f"point({self.x},{self.y})")

    def __eq__(self, other):  # baz nevisi nahveye moghayeseye "barabari"
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):  # baz nevisi nahveye moghayeseye "bozorgtar"
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):  # baz nevisi nahveye moghayeseye "bozorgtar"
        return self.x < other.x and self.y < other.y


point1 = MyPoint(3, 4)
point2 = MyPoint(1, 2)
print(point1 == point2)
print(point1 > point2)
print(point1 < point2)
