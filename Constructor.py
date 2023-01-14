# Constructor


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
    default_color = "red"


point1 = MyPoint(2, 3)  # Creating an object
print(type(point1))  # output: <class '__main__.MyPoint'>
print(isinstance(point1, MyPoint))  # if point1 is a object of My point?
point1.draw()  # output: point(5,3)
point1.z = 15  # in python objects are dynamic and we should not set in 'class'
