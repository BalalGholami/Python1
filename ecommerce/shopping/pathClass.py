# pathClass.py
from pathlib import Path
path = Path(r"d:\learning\SD\Programming\Python1")
# r for not \\ using


path = Path("ecommerce/__init__.py")

path = Path() / Path("ecommerce")
print(path.absolute())
print(path.exists())
print(path.is_file())
print(path.is_dir())
path2 = path.with_name("file.txt")
print("path2:")
print(path2)
path3 = path.with_suffix(".txt")
print("path3:")
print(path3)
