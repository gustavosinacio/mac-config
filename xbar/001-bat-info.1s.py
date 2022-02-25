#!/opt/homebrew/bin/python3

import os
import subprocess

battery = int(subprocess.getoutput(
    "pmset -g batt | grep -Eo \"\\d+%\" | cut -d% -f1"
))
charging = subprocess.getoutput(
    "pmset -g batt | grep -Eo \"%;\\s\\w+\" | cut -d \" \" -f2"
)
therms = subprocess.getoutput(
    "pmset -g therm"
).splitlines()
sysload = subprocess.getoutput(
    "pmset -g sysload"
).splitlines()
adapter = subprocess.getoutput(
    "pmset -g adapter"
).splitlines()


config = " | size=12 font='quicksand'"
color = ''

white = "\033[1;37m"
green = "\033[1;32m"
yellow = "\033[1;33m"
red = "\033[1;31m"
reset = "\033[0m"

# black = "\033[1;30m"
# blue = "\033[1;34m"
# magenta = "\033[1;35m"
# cyan = "\033[1;36m"

if battery >= 50:
    color = white
elif battery < 50 and battery >= 15:
    color = yellow
else:
    color = red

charginSymbol = ""
if(charging == "charging"):
    charginSymbol = "ϟ"
    color = green


resultBatteryString = ""
resultBatteryString += color
resultBatteryString += charginSymbol + " "
resultBatteryString += str(battery) + "%"
resultBatteryString += " " + charginSymbol
resultBatteryString += reset
resultBatteryString += config
# Return on the top bar here ---------------------------------------------------
print(resultBatteryString)
# ------------------------------------------------------------------------------
print("---")

print("therm")
for line in therms:
    print("--{}".format(line))

print("sysload")
for line in sysload:
    print("--{}".format(line))

print("adapter")
for line in adapter:
    print("--{}".format(line))

print(charging)
