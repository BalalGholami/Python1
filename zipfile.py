# zip files
1
from pathlib import Path

from zipfile import ZipFile

#zipfile : class
#ZipFile: module

with ZipFile("files.zip","w") as zip: # ghabeliate neveshtan ba 'W' ast
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)



#mikhahim mohtavaye directory 'ecommerce' ra zip konim.




