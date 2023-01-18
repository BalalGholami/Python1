# AccessToFatherMethod


class Animal:
    def __init__(self):
        self.age = 1

    def eat(slef):
        print("Animal Eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2


m = Mammal()
print(m.weight)
print(m.age)  # Called with "super" method
