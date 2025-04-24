""" input is a amount of money in cents the smallest amount of coins should be returned
optiona are 25 10 5 1 cent; if statements in while loop as long as != 0 one counter for
all if statements and each statement substracts their amount and increments the counter """


def main():
    # get change and try to convert to float
    while True:
        change = input("Change? ").strip()
        try:
            change = float(change)*100
        except ValueError:
            continue
        # break out of Loop if positive float
        if change >= 0:
            break

    # initialise counter to keep track of amount of coins
    counter = 0
    # subtract the coin amount of the highest legal coin until change is 0
    while change != 0:

        if change >= 25:
            change -= 25
            counter += 1

        elif change >= 10:
            change -= 10
            counter += 1

        elif change >= 5:
            change -= 5
            counter += 1

        elif change >= 1:
            change -= 1
            counter += 1

    # print optimal amount of coins for given change
    print(counter)


if __name__ == "__main__":
    main()
