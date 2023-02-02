<<<<<<< HEAD
# import zipfiles
=======
# zip files
1
from pathlib import Path
>>>>>>> 1e9b676a7a3b878ca561f233878083b961d724d6

from zipfile import ZipFile

#zipfile : class
#ZipFile: module

with ZipFile("files.zip","w") as zip: # ghabeliate neveshtan ba 'W' ast
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)



#mikhahim mohtavaye directory 'ecommerce' ra zip konim.




