""" count lines in file ignore emptylines and comments output in terminal
    filename or path input sys argv [1] - more than one 'Too many command-line arguments ' 'Too few command-line arguments' sys.exit
    should only work on py files - 'Not a Python file ' sys.exit
    inexistnt filr - 'File does not exist' sys.exit
"""
import sys

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

count=0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            if not line.lstrip().startswith("#")  and not line.isspace() and not line.startswith("\t"):
                count = count + 1
except FileNotFoundError:
        sys.exit("File does not exist")

print(count)

# and not line.startswith('"""')
