#!/opt/homebrew/bin/python3

import os
import subprocess

battery = int(subprocess.getoutput(
    "pmset -g batt | grep -Eo \"\\d+%\" | cut -d% -f1"))
config = " | size=12 font='fira code'"
color = ''

green = "\033[1;32m"
yellow = "\033[1;33m"
red = "\033[1;31m"
reset = "\033[0m"

black = "\033[1;30m"
blue = "\033[1;34m"
magenta = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"


if battery >= 50:
    color = green
elif battery < 50 or battery >= 30:
    color = yellow
else:
    color = red

print("{}{}%{}{}".format(battery, color, reset, config))

print("---")
print("{}{}%{}{}".format(black, battery, reset, config))
print("{}{}%{}{}".format(red, battery, reset, config))
print("{}{}%{}{}".format(green, battery, reset, config))
print("{}{}%{}{}".format(yellow, battery, reset, config))
print("{}{}%{}{}".format(blue, battery, reset, config))
print("{}{}%{}{}".format(magenta, battery, reset, config))
print("{}{}%{}{}".format(cyan, battery, reset, config))
print("{}{}%{}{}".format(white, battery, reset, config))
print("{}{}%{}{}".format(reset, battery, reset, config))
print("--menu? {}{}%{}{}".format("\033[1;31m", battery, reset, config))
