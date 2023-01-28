# Unpacking Operator
# We can use * as a Unpacking Operator for Auspackung die charackters

values = list(range(20))
print(*values)

# --------------
values = [*range(20)]
print(values)

# ---------------
chars = [*"hello"]
print(chars)
# -------------------
first = [1, 2]
second = [3, 4]
values = [*first, *second, chars]
print(values)

# ---------------
# 1- in dictionary binding, the last item will be used
# 2- in dictionaries, we use 2 of * in unpacking operation
first = {"x": 1}
second = {"y": 5, "x": 6}
combined = {**first, **second}
print(combined)
