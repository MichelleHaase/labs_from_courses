import sys
from PIL import Image
from PIL import ImageOps

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) or not sys.argv[
    2
].lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Not a Image file")

if sys.argv[1].lower()[-3:-1] != sys.argv[2].lower()[-3:-1]:
    sys.exit("Input and output must have same file extension")

try:
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

shirt = Image.open("shirt.png")
shirt_size = shirt.size

input_image = ImageOps.fit(input_image, size=shirt_size)
input_image.paste(shirt, box=(0, 0), mask=shirt)
input_image.save(sys.argv[2])

print(input_image)
