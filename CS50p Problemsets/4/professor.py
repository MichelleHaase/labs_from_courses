import random

questions = {}


def main():
    score = 0
    level_input = get_level()
    for i in range(10):
        x, y = generate_integer(int(level_input))
        for i in range(4):
            if i < 3:
                try:
                    result1 = int(input(f"{x} + {y} = "))
                    if int(result1) == (x + y):
                        score += 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")
            if i == 3:
                print(f"{x} + {y} = :{(x+y)}", sep="")
    print(f"Score: {score}")


# def crating_questions():
#     level_input= get_level()
#     for i in range(11):
#         x,y = generate_integer(int(level_input))
#         questions.update({f"{x} + {y} = ":(x+y)})
#     return questions


def get_level():
    while True:
        level_input = input("Level: ")
        try:
            if int(level_input) in [1, 2, 3]:
                return int(level_input)
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10), random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100), random.randrange(10, 100)
    elif level == 3:
        return random.randrange(100, 1000), random.randrange(100, 1000)


if __name__ == "__main__":
    main()
