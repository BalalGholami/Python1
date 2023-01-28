# Inheritence from Python embeded functions

class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")

print(text.duplicate())
print(text.lower())
# --------------
# Redefine one method from fathers'class


class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)


list = TrackableList()
list.append("1")
