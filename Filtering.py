# Filtering

items = [
    ("p1", 40),
    ("p4", 35),
    ("p3", 42)
]

x = list(filter(lambda item: item[1] > 36, items))
print(x)
