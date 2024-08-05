from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        text = input("Input: ")
        fonts = figlet.getFonts()
        f = Figlet(font = 'slant')
        print(f.renderText(f'{text}'))

    elif len(sys.argv) == 3:
        text = input("Input: ")
        f = Figlet(font = f"{sys.argv[2]}")

    else:
        sys.exit("Invalid Input")

main()
