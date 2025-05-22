def main():
    greeting = input("Hi! ")
    money_owed = value(greeting)
    print(f"${money_owed}")


def value(greeting):
    if greeting.strip().lower()[0:5] == "hello":
        return 0
    elif greeting.strip().lower()[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
