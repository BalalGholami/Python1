# Directories.py

from pathlib import Path

path = Path('ecommerce2')
if path.exists():
    print(path.rmdir())
print(path.mkdir())
print(path.iterdir())  # ADDRESS

path = Path('ecommerce')
print(path.iterdir())  # address
for p in path.iterdir():
    print(p)
print("----------")
py_files = [p for p in path.rglob("*.py")]
print(py_files)
print("------------")
for p in path.rglob("*.py"):
    print(p)
