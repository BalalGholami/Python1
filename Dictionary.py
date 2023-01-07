# Dictionary

dictionary1 = {"x": 1, "y": 3, "z": 7}

dictionary2 = dict(x=1, y=5, z=9)

print(dictionary1)
print(dictionary2)
print(dictionary1["z"])
print(dictionary2.get("a", "Not Exists"))
print(dictionary1.get("x", "Not Exists"))
print(dictionary1.keys())
print(dictionary1.values())
print(dictionary1.items())
if "x" in dictionary1:
    print("Exists")
