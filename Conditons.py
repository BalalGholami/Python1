x = int(input("Enter your number: "))
print(type(x))
if x < 10:
    print("Very cold")
elif x < 20:
    print("cool")
elif x < 30:
    print("good")
else:
    print("Warm")

print("-------------")
message = "warm" if x > 30 else "not warm"
print(message)
if 10 < x < 20:
    message = "Normal"
print(message)
y = range(3)
print(y)
