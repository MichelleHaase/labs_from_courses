import sys
import csv

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")
names = []
house = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] != "name":
                names.append(line[0])
                house.append(line[1].strip())
except FileNotFoundError:
    sys.exit("File does not exist")

lastname = []
firstname = []
for name in names:
    #  print(name)
    lastname.append(name.split(",")[0].strip())
    firstname.append(name.split(",")[1].strip())

with open(sys.argv[2], "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for i in range(len(firstname)):
        writer.writerow({"first": firstname[i], "last": lastname[i], "house": house[i]})
