input1 = 0

while input1 < 50:
    input2 = int(input("Amount Due: 50\n"))
    if input2 == 5 or input2 == 10 or input2 == 25:
        input1 = input1 + input2
        if input1 < 50:
            print(f"Amount Due: {50 - input1}")
        elif input1 >= 50:
            print(f"Change Owed: {input1 - 50}")
