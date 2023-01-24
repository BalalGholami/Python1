# Polymorphism2

# در این مثال، بدون اینکه کلاس وارد تعریف کرده باشیم، می توانیم چند ریختی را داشته باشیم
# صرفا با توجه به اینکه هر دو کلاس تعریف شده، دارای یک متد یک نام هستند، چند ریختی انجام شد
from abc import ABC, abstractmethod


class TextBox:
    def draw(self):
        print("Text Box Drawing")


class DropDownList:
    def draw(self):
        print("Drop Down list Drawing")


def draw(control):
    control.draw()


ddl = DropDownList()
draw(ddl)


txtBox = TextBox()
draw(txtBox)
