from tabulate import tabulate
import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a csv file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")



