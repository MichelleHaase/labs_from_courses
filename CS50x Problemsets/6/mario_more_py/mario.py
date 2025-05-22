def main():
    while True:
        # getting positive int between 1 and 8
        try:
            height = int(input("Height? ").strip())
        except ValueError:
            continue
        if height > 0 and height < 9:
            # break out of loop when conditions are met
            break

    for row in range(height):
        for columns in range(height - row - 1):
            print(" ", end="")
        for hash in range(row + 1):
            print("#", end="")

        print(end="  ")

        for hash2 in range(row + 1):
            print("#", end="")
        # for col2 in range(height-row-1):
        #     print(" ", end="")

        print()


if __name__ == "__main__":
    main()
