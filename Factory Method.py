# Factory Method


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

    @classmethod  # ghabl as yek factory method
    def zero(cls):  # Yani class ra daryaft mikonad
        return MyPoint(0, 0)


point1 = MyPoint(0, 0)  # Creating an object
point1.draw()  # output: point(0,0)
point2 = MyPoint.zero()  # creating a new object with factory method
point2.draw()
