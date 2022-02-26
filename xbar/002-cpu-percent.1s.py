#!/opt/homebrew/bin/python3

# <xbar.title>show cpu percent</xbar.title>
# <xbar.version>v0.0.1</xbar.version>
# <xbar.author>Gustavo Inacio</xbar.author>
# <xbar.author.github>gustavosinacio</xbar.author.github>
# <xbar.desc>Displays cpu usage</xbar.desc>

import subprocess


green = "\033[1;32m"
yellow = "\033[1;33m"
red = "\033[1;31m"
reset = "\033[0m"

cpuPercent = float(subprocess.getoutput(
    "top -F -R -o cpu -l 2 -s 1 | grep -E \"^CPU\" | tail -1 | awk '{ print $3 + $5 }'"
))

if cpuPercent <= 30:
    color = green
elif cpuPercent > 30 and cpuPercent <= 50:
    color = yellow
else:
    color = red

stringfiedCpuPercent = str(int(cpuPercent)).rjust(2)

config = " | ansi=true font='fira code' trim=false size=14"

print("{}💻{}%{}{}".format(color, stringfiedCpuPercent, reset, config))
