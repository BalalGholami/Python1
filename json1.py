# json1
from pathlib import Path
import json

users = [
    {"id": 1, "name": "pedram", "age": 25},
    {"id": 2, "name": "reza", "age": 27},
    {"id": 3, "name": "nahid", "age": 20},
    {"id": 4, "name": "mehrdad", "age": 34},
    {"id": 5, "name": "sima", "age": 18}
]


data = json.dumps(users)
Path("users.json").write_text(data)
data = Path("users.json").read_text()

users = json.loads(data)
# print satr be satr:
for x in users:
    print(x)
print("-------------")

# print mamooli:
print(users)
# type moteghayere users
print(type(users))
