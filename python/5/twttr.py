def main():
    input1 = input("Input: ").strip()
    short_input = shorten(input1)
    print(short_input)


def shorten(word):
    # exspects a string as input and returns the same str witout vowels
    List1 = ["a", "A", "O", "o", "E", "e", "I", "i", "U", "u"]
    result = ""
    for i in word:
        if i in List1:
            continue
        else:
            result = result + i
    return result


if __name__ == "__main__":
    main()
