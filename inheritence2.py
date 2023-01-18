# inheritence2
# some other functions
class Animal:
    def __init__(self):
        self.age = 1

    def eat(slef):
        print("Animal Eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 2


class Fish(Animal):
    def eat(slef):
        print("Fish Eat")


m = Mammal()
print(m.weight)
# print(m.age) : cannot execute. because __init__ has been override on father class
