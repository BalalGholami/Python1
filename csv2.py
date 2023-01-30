# reading csv

import csv


with open("data.csv") as file:
    reader = csv.reader(file)
    x = list(reader)
    print(x)
    print("------------")
    for row in x:
        print(row)
