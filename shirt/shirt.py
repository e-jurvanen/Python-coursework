import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments")

elif sys.argv[1].endswith(".jpg") == False and sys.argv[1].endswith(".png") == False:
    sys.exit("Invalid output")

elif sys.argv[1].endswith(".jpg") != sys.argv[2].endswith(".jpg") or sys.argv[1].endswith(".png") != sys.argv[2].endswith(".png"):
    sys.exit("Input and Output have different extensions")

shirt = Image.open("shirt.png")
size = shirt.size

try:
    photo = Image.open(sys.argv[1])
    photo = ImageOps.fit(photo, size)

except FileNotFound:
    sys.exit("Input does not exist")

photo.paste(shirt, shirt)
photo.save(sys.argv[2])
