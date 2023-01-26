# Majic Methods

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

    def __str__(self):  # changing default __str__
        return f"({self.x},{self.y})"


point1 = MyPoint(1, 2)
print(point1)     # method __str__ farakhani mishavad
print(str(point1))  # method str be shekl digari farakhani mishavad
