def main():
    z = convert(input("How full is the Tank? "))
    print(gauge(z))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def convert(fraction):
    # while True:
        # try:
    x, y = fraction.split("/")
    # if int(x) <= int(y):
    z = (int(x) / int(y)) * 100
    return int(round(z))
        # except (ValueError, ZeroDivisionError):
        #     # fraction = input("How full is the Tank? ")
        #     break


if __name__ == "__main__":
    main()
