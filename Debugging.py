# Debugging

def f1(*items):
    total = 1
    for i in items:
        total += i
    return total


f = f1(1, 2, 3, 4, 5, 6)
print(f)
