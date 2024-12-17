import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        text = input("Input: ")
        figlet.setFont(font=random.choice(figlet.getFonts()))
        print(figlet.renderText(text))

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        elif sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
        else:
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")

main()
