import random
import sys


def main():
    while True:
        input1 = input("Level: ").strip()
        try:
            if int(input1) > 0:
                target = random.randrange(1, (int(input1) + 1))
                Guessing_game(int(target))
                break
        except ValueError:
            continue


def Guessing_game(level):
    while True:
        guess = input("Guess: ")
        try:
            if int(guess) > 0:
                if int(guess) < level:
                    print("Too small!")
                elif int(guess) > level:
                    print("Too large!")
                else:
                    print("Just right!")
                    sys.exit()
        except ValueError:
            continue


main()
