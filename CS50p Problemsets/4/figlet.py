from pyfiglet import Figlet
from pyfiglet import FigletFont
import sys
import random

fonts = FigletFont.getFonts()

try:
    if len(sys.argv) <= 3:
        if len(sys.argv) == 3:
            if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                if str(sys.argv[2]) in fonts:
                    user_font = sys.argv[2]
        elif len(sys.argv) == 1:
            user_font = random.choice(fonts)
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

except IndexError:
    sys.exit("Invalid usage")
try:
    font = Figlet(font=user_font)
    input1 = input("Input: ")
    print("Output:\n", font.renderText(input1))
except NameError:
    sys.exit("Invalid usage")
