# Dictionary

dictionary1 = {"x1": 1, "y1": 3, "z1": 7}

dictionary2 = dict(x2=1, y2=5, z2=9)

print(f"Dictionary1: {dictionary1}")
print(f"Dictionary2: {dictionary2}")
print(dictionary1["z1"])
print(dictionary2.get("a", "a Not Exists"))
print(dictionary1.get("x", "x Not Exists"))
print(dictionary1.keys())
print(dictionary1.values())
print(dictionary1.items())
if "x" in dictionary1:
    print("x Exists")
else:
    print("x Not Existst")
del dictionary1["x1"]
for x in dictionary1.items():
    print(x)
print(f"Dictionary1: {dictionary1}")
