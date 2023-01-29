# files1

from pathlib import Path
import shutil

path = Path('ecommerce\\__init__.py')

print(path.exists())
# path.unlink() -> delete file
print(path.stat())  # ettellate file
print(path.read_bytes())
print(path.read_text())

source = Path('ecommerce\\__init__.py')
target = Path() / "__init__.py"

shutil.copy(source, target)  # yek file jadid dar root ijad mikonim
