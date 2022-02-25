#!/opt/homebrew/bin/python3

import os
import subprocess

battery = int(subprocess.getoutput(
    "pmset -g batt | grep -Eo \"\\d+%\" | cut -d% -f1"))
config = " | size=12 font='quicksand'"
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
elif battery < 50 and battery >= 15:
    color = yellow
else:
    color = red

print("{}{}%{}{}".format(color, battery,  reset, config))

print("---")
print("{}{}%{}{}".format(blue, battery, reset, config))
print("--submenu {}{}%{}{}".format(white, battery, reset, config))
print("----subsubmenu {}{}%{}{}".format(white, battery, reset, config))
