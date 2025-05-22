""" L= avrg num of letters, not chars, per 100 words
    s= num of scentences per 100 words
        index = 0.0588 * L - 0296 * S - 15.8 """


def main():
    text = input("Text: ")
    words = get_words(text)
    letters = get_letters(text, words)
    sentences = get_sentences(text, words)
    index = round((0.0588 * letters - 0.296 * sentences - 15.8))
    # print(letters)

    # print grade according to index
    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


# get word count to calculate other meassures per 100 words
def get_words(text):
    # set to 1 since there is no space after the last word
    words = 1
    for i in range(len(text)):
        if text[i].isspace() == True:
            words += 1
    return words


# getting the amount of letters per 100 words in text
def get_letters(text, words):
    # initialise letter counter
    letters = 0
    # going thru every letter and count if alphanumeric
    for i in range(len(text)):
        if text[i].isalpha() == True:
            letters += 1
    # letters per word times 100
    letters = letters / words * 100
    return letters


# get number of sentences per 100 words
def get_sentences(text, words):
    # set counter
    sentences = 0
    # count every time a scentence ends with . ? !
    for i in range(len(text)):
        if text[i] in ".?!":
            sentences += 1
    # sentences per words times 100
    sentences = sentences / words * 100
    return sentences


if __name__ == "__main__":
    main()
