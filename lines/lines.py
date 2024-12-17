import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()

except FileNotFoundError:
    sys.exit("File does not exist")

rows = 0

for line in lines:
    if line.lstrip().startswith("#") == False and line.isspace() == False:
        rows += 1

print(rows)
