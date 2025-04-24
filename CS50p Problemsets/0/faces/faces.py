def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    text = convert(input("Hi, need pretty pics? "))
    print(text)


main()
