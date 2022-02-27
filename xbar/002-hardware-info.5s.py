#!/opt/homebrew/bin/python3

from cgi import FieldStorage
from operator import ne
import subprocess


green = "\033[1;32m"
yellow = "\033[1;33m"
red = "\033[1;31m"
reset = "\033[0m"
config = " | ansi=true font='fira code' trim=false size=14"


topReturn = str(subprocess.getoutput(
    "top -F -R -s 1 -n 5 -stats pid,command,cpu,mem,state,power -o -cpu -l 2"
)).splitlines()
# Remove date line
topReturn.pop(0)

isSecond = False
top = {}

for line in topReturn:
    if line.startswith("Processes: "):
        isSecond = True
    if isSecond == True and line != '':
        separated = line.split(": ")
        if len(separated) > 1:
            field = separated[0].strip()
            data = separated[1:]
            top[field] = data
        else:
            proccess = line.split(" ")
            field = proccess[0].strip().ljust(6)
            proccess.pop(0)
            data = proccess[1:]
            newData = ""
            for dataField in data:
                if dataField != '':
                    newData += dataField.rjust(20)
            top[field] = newData


cpuPercent = 100 - float(top['CPU usage'][0].split(", ")[2].split("%")[0])

if cpuPercent <= 30:
    color = green
elif cpuPercent > 30 and cpuPercent <= 50:
    color = yellow
else:
    color = red

stringfiedCpuPercent = str(int(cpuPercent)).rjust(2)

print("{}💻{}%{}{}".format(color, stringfiedCpuPercent, reset, config))

# print('{}'.format(stringfiedCpuPercent))
# print('{}'.format(topReturn))
print('---')
for each in top:
    print(each + ': ', top[each])
