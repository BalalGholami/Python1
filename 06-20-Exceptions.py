# Exceptions

try:
    age = int(input("Age : "))
    file = open("file1.txt")
except (ValueError, ZeroDivisionError):
    # this is the error when use enter charackter will not number or zero
    print("you didn't enter valid age")
else:
    age += 1
    print(age)
finally:
    print("file yet not closed")
    file.close()  # closing file
    print("file now closed")
print("Done")
# ---------------------------
# second way for closing file:
with open("file1.txt") as file, open("file2.txt") as taret:
    print("file1 and file2 is Opened")
