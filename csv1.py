# csv files

import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "phone"])
    writer.writerow(["1", "ali", "6354"])
    writer.writerow(["2", "mehdi", "543"])
    writer.writerow(["3", "sepehr", "153"])
    writer.writerow(["4", "samira", "453"])
