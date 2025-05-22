input = input("please provide a Var name in Camelcase\n").strip()

for letter in input:
    if letter.islower():
        print(letter, end="")
    else:
        print("_", letter.lower(), end="", sep="")
print()
