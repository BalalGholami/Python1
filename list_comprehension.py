# list comprehension

items = [
    ("p1", 40),
    ("p4", 35),
    ("p3", 42)
]

x = list(map(lambda item: item[1], items))
y = [item[1] for item in items]
print(x)
print(y)

# --------------------

x = list(filter(lambda item: item[1] > 36, items))
y = [item for item in items if item[1] > 36]
print(x)
print(y)
