# print(tabulate(table, headers, tablefmt="grid"))
from tabulate import tabulate
import sys
import csv

table = []
if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for line in reader:
            table.append(line)
        # print(table[1])
        print(tabulate(table[1:], table[0], tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
