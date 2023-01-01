# touple
point = (1, 2)
print(type(point))
print(point)
# ----------------
point1 = tuple(list("tauple"))
print(point1)
# ----------------

# touple with just one element:
# we need comma after our element
point2 = 7,
print(point2)
# ----------------
# CONCATENATE:
point3 = point+point1
print(point3)
# ------------
# tekrar tauple
point = (1, 2)*3
print(point)
# ------------
# Convert list to tauple
print("Convert list to tauple:")
l1 = list("My string")
print(l1)
print(type(l1))
tauple1 = tuple(l1)
print(tauple1)
print(type(tauple1))
# element exist or not:
x = input("Enter a Character:")
if x in tauple1:
    print(f"{x} exists")
else:
    print(f"{x} not exists")
# --------------
