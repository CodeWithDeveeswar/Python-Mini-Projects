# CSV Data Reader (Basic)

import csv

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header

    for row in reader:
        print(f"{row[0]} scored {row[1]}")