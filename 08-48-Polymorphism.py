# Polymorphism

from abc import ABC, abstractmethod


class UI_Control(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UI_Control):
    def draw(self):
        print("Text Box Drawing")


class DropDownList(UI_Control):
    def draw(self):
        print("Drop Down list Drawing")


def draw(control):
    control.draw()


ddl = DropDownList()
draw(ddl)

# Checking if ddl is an instance from top father class
print(isinstance(ddl, UI_Control))

txtBox = TextBox()
draw(txtBox)
