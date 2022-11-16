# Trick:had to seperate the fomts list condition line [13]

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
Fonts = figlet.getFonts()
if len(sys.argv) == 1:
    Rfont = random.choice(figlet.getFonts())
    figlet.setFont(font=Rfont)
    Text = input("Input: ")
    print(figlet.renderText(Text))
elif not sys.argv[2] in Fonts:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    Text = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(Text))
else:
    sys.exit("Invalid usage")
