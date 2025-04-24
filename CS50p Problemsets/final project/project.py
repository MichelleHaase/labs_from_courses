from wonderwords import RandomWord
import sys


def main():
    level = get_level()
    word, tries = get_word(level)
    guessing(word, level, tries)


def get_level():
    print("\n--- This is Hangman ---\n")
    # while Loop reprompts till the input is Valid
    while True:
        # gets the Level from the user, the Level defines the lenght of the word that will be guessed in guessing()
        level = input(
            "Please choose your level\n\n1  for a four to five letter words\n2  for a six to eight letter words\n3  for a nine to twelve letter words\n"
        )
        # decides if the input is Valid
        if level in ["1", "2", "3"]:
            # returns Level to main
            return level
        # informs the user about the intentet input
        print("\n### please enter 1, 2 or 3 ###\n")


def get_word(l):
    # match case sets the word lenght according to the Level and how many tries will be allowed in guessing()
    match l:
        case "1":
            word_min = "4"
            word_max = "5"
            tries = 10
        case "2":
            word_min = "6"
            word_max = "8"
            tries = 12
        case "3":
            word_min = "9"
            word_max = "12"
            tries = 15
    # getting a random word of lenght word_lenght with wonderwords and return it and tries
    random = RandomWord()
    return (
        random.word(word_min_length=int(word_min), word_max_length=int(word_max)),
        tries,
    )


def guessing(word, level, tries):
    # initializing neccesary Vars
    list_guesses = []
    check = ["_ "] * len(word)
    count_guesses = 0
    # information for Useer
    print(
        f"Your Level is set to {level}\nYour word is set\nYou have {tries} Tries\nLet's Play\n"
    )
    while True:
        # prints "_ " for each letter in the searched word
        print("".join(check), "\n")
        # depicts the old guesses and left tries, for a better overview
        print(
            f"Already Guessed: {list_guesses}\nGuesses left {tries - count_guesses}\n"
        )
        # prompting the user for a letter or word to guess
        guess = input("which Letter do you choose? ")
        if guess not in list_guesses:
            # add letters to the list if they are new
            list_guesses.append(guess)
            # counter to track number of guesses if guessed wrong
            if guess not in word:
                count_guesses += 1
        # prints the graphics corresponding to how many tries are left
        print(graphics(count_guesses, level))
        if len(guess) == 1:
            # if the guess is a single char
            if guess in word:
                # if the guess is in the word
                for i in range(len(word)):
                    # overwrites the "_ " with the guessed letter, at the position its located in the word
                    if guess == word[i]:
                        check[i] = guess
        # joins everything in check to one string and checks if it's equal to the word or if the word was just guessed in one
        if "".join(check) == word or guess == word:
            # Message if win conditions are met
            sys.exit(f"{word} is right!!\n🎉🎉🎉 !!You Won!! 🥳 🎉🎉🎉")

        if count_guesses == tries:
            # Losing Message if the user guessed more times than tries allows
            sys.exit(
                f"guesses: {list_guesses}\nBad Luck 😭\nThe right guess would have been {word}"
            )


def graphics(count_guesses, level):
    match count_guesses:
        case 1:
            return """
    ____|_____"""
        case 2:
            return """
        |
    ____|_____"""
        case 3:
            return """
        |
        |
    ____|_____"""
        case 4:
            return """
        |
        |
        |
    ____|_____"""
        case 5:
            return """
        |
        |
        |
        |
    ____|_____"""
        case 6:
            return """
        |
        |
        |
        |
        |
    ____|_____"""
        case 7:
            return """
        ____
        |
        |
        |
        |
        |
    ____|_____"""
        case 8:
            return """
        ________
        |
        |
        |
        |
        |
    ____|_____"""
        case 9:
            return """
        ________
        |       |
        |
        |
        |
        |
    ____|_____"""
    if level == "1":
        match count_guesses:
            case 10:
                return """
        ________
        |       |
        |       0
        |      /|\\
        |       |
        |      / \\
    ____|_____ """
    else:
        match count_guesses:
            case 10:
                return """
        ________
        |       |
        |       0
        |
        |
        |
    ____|_____ """
            case 11:
                return """
        ________
        |       |
        |       0
        |      /|\\
        |
        |
    ____|_____ """
        if level == "2":
            match count_guesses:
                case 12:
                    return """
        ________
        |       |
        |       0
        |      /|\\
        |       |
        |      / \\
    ____|_____ """
        else:
            match count_guesses:
                case 12:
                    return """
        ________
        |       |
        |       0
        |      /|\\
        |
        |
    ____|_____ """
                case 13:
                    return """
        ________
        |       |
        |       0
        |      /|\\
        |       |
        |
    ____|_____ """
                case 14:
                    return """
        ________
        |       |
        |       0
        |      /|\\
        |       |
        |      /
    ____|_____ """
                case 15:
                    return """
        ________
        |       |
        |       0
        |      /|\\
        |       |
        |      / \\
    ____|_____ """


if __name__ == "__main__":
    main()
