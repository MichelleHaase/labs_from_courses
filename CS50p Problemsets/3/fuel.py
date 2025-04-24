def main():
    z = convert_to_int("How full is the Tank? ")
    if z <= 1:
        print("E")
    elif z >= 99:
        print("F")
    else:
        print(z, "%", sep="")


def convert_to_int(promt):
    while True:
        input1 = input(promt)
        try:
            x, y = input1.split("/")
            if int(x) <= int(y):
                z = (int(x) / int(y)) * 100
                return int(round(z))
        except ZeroDivisionError:
            pass
        except ValueError:
            pass


main()
