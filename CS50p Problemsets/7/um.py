import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # um = re.findall(r"(^um$|^um[^a-zA-Z]{1}\s*|[^a-zA-Z]{1}\s*um[^a-zA-Z]{1}\s*|[^a-zA-Z]{1}\s*um$)",s, re.IGNORECASE)
    um = re.findall(r"(\bum\b)", s, re.IGNORECASE)
    return len(um)


if __name__ == "__main__":
    main()
