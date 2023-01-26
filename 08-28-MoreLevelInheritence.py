# MoreLevelInheritence

class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("Fly")


class Chicken(Bird):
    pass


bird1 = Chicken()

bird1.eat()
