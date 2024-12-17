import csv
import sys

students = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1]) as before:
        reader = csv.DictReader(before)

        for row in reader:
            last, first = row["name"].split(",")
            students.append({"first": first.strip(), "last": last.strip(), "house": row["house"] })

except FileNotFoundError:
    sys.exit("File does not exist")

with open(sys.argv[2], "w") as after:
    writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in students:
        writer.writerow(row)



