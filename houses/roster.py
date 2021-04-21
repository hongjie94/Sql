import cs50 
from sys import argv, exit


if len(argv) != 2:
    print("ENTER STUDENT NAME!")
    exit(1)
 
db = cs50.SQL("sqlite:///students.db")
output = db.execute('SELECT * FROM students WHERE house = ? ORDER BY last, first', argv[-1])

for row in output: 
    print(row['first'] + ' ' + (row['middle'] + ' ' if row['middle'] else '') + row['last'] + ', born ' + str(row['birth']))