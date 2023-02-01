# randomize

import random
import string
x = random.random()
print(x)
x = random.choice([1, 2, 3, 4, 5, 6, 7])
print(x)
x = random.choices([1, 2, 3, 4, 5, 6, 7], k=12)
print(x)
x = random.choices(
    string.ascii_letters+string.digits+"!@#$%^&*()", k=10)
print(x)
x2 = "".join(x)
print(x2)
print(string.ascii_letters)
print(string.digits)
x = random.choices(
    string.ascii_letters+string.digits, k=10)  # tarkib digital and alphabet
x2 = "".join(x)
print(x2)
numbers = list(string.digits)
print(numbers)
random.shuffle(numbers)
print(numbers)
