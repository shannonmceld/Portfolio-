import random
import sys
from pyfiglet import Figlet
from sys import argv

figlet = Figlet()
figlets = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Text: ")
    fonts = random.choice(figlets)
    figlet.setFont(font = fonts)
    print(figlet.renderText(text))


elif len(sys.argv) == 3:
    first_arg = argv[1]
    arg = ["-f", "--font"]
    word = argv[2]
    if first_arg in arg and word in figlets:
        text = input("Text: ")
        set = figlet.setFont(font = word)
        print(figlet.renderText(text))

    else:
        print("Invalid Usage")
        sys.exit(1)



else:
    print("Invalid Usage")
    sys.exit(1)