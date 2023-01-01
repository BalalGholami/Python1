# Mapping

items = [
    ("p1", 40),
    ("p4", 35),
    ("p3", 42)
]

x = list(map(lambda item: item[1]*2, items))
x.sort()
print(x)
