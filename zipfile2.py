from pathlib import Path
from zipfile import ZipFile

print ("Zip file reading start:")

with ZipFile("files.zip") as zip:
    name = zip.namelist()
    inf = zip.getinfo(zip.namelist()[1])
    print(inf.file_size)
    print(inf.compress_size)
    

