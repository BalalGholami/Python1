# Scope

m = 1


def f1(n):
    global m
    n = m
    m += 1
    print(f"in function: n= {n}")
    print(f"in function: m= {n}")


f1(4)
print(f"out of function: {m}")
