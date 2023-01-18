# inheritence1
class Animal:
    def __init__(self):
        self.age = 1

    def eat(slef):
        print("Animal Eat")


class Mammal(Animal):
    def Walk(self):
        print("Mammal Walk")


class Fish(Animal):
    def eat(slef):
        print("Fish Eat")


m1 = Mammal()
m1.eat()
m1.Walk()
m2 = Fish()
m2.eat()
print(m2.age)

print(isinstance(m2, object))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, Animal))
