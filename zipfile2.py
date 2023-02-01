from pathlib import Path
from zipfile import ZipFile

print ("Zip file reading start:")

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    

