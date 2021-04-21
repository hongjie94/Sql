import cs50 
from sys import argv, exit
import csv

if len(argv) != 2:
    print("ENTER CSV FILE!")
    exit(1)

db = cs50.SQL("sqlite:///students.db")

with open(argv[1], "r") as characters:
    reader = csv.DictReader(characters)

    for row in reader:

        full_name = row["name"].split()
        first, middle, last = full_name[0], full_name[1] if len(full_name) == 3 else None, full_name[-1]
        house = row["house"]
        birth = row["birth"]
    
        db.execute("INSERT INTO students (first, middle , last, house, birth) VALUES(?, ?, ?, ?, ? )", first, middle, last, house, birth)