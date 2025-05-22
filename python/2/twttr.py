input1 = input("Input: ").strip()
List1 = ["a", "A", "O", "o", "E", "e", "I", "i", "U", "u"]
for i in input1:
    if i in List1:
        continue
    else:
        print(i, end="")
print()
