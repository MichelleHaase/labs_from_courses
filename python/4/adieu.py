import sys

List1 = []


def concatanaiting_output():
    print(f"Adieu, adieu, to ", end="")
    if len(List1) == 1:
        print(List1[0])
    elif len(List1) == 2:
        print(f"{List1[0]} and {List1[1]}", end="")
    elif len(List1) >= 3:
        for i in range(len(List1)):
            if List1[i] != List1[-1]:
                print(f"{List1[i]}, ", sep="", end="")
            else:
                print(f"and {List1[i]}")


while True:
    try:
        input1 = input("Name: ").strip()
        List1.append(input1)
    except EOFError:
        if len(List1) == 0:
            break
        else:
            concatanaiting_output()
            break
