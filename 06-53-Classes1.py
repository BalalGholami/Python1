# Classes1

#   class -> object
#   object = sample of a class

x = 1
print(type(x))

# result: <class 'int'>
# int is a class

print("-----------")
# Creating class:
# Start word with Uppercase


class MyPoint:
    def draw(self):  # all of the functions of class must have a parameter and its name is better been 'self'
        print("draw function")


point1 = MyPoint()
print(type(point1))
# output: <class '__main__.MyPoint'>
point1.draw()
print(isinstance(point1, MyPoint))
