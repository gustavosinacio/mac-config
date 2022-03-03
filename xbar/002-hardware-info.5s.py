#!/opt/homebrew/bin/python3

from cgi import FieldStorage
from operator import ne
import subprocess

BUILTIN_GPU_ICON = (
    'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAWJ'
    'QAAFiUBSVIk8AAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD'
    '0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1'
    'sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAg'
    'ICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0ia'
    'HR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj'
    '4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkR'
    'GPgo8L3g6eG1wbWV0YT4KTMInWQAAA3JJREFUWAntlsmKFEEQhtt9X8cVlZHxKvgQend5HG+efAof'
    'QRS9ztw9DvgAIigqMrjv6/dV1+9kTVdXV40gDPjD3xkVGRkZERlZXaPRf3RXYFP3dOfsrLW/Oldvl'
    'MlZWXblsZfJn1MMNqN/P2WuU72egLbi8Tu8CV9Anz0efTka5FF4HcYWsR9cMBRJ4hgLv8Ft0CCi/4'
    'HsnIhu/NTjdz0BpVmf4v85bAsoRxnbHqGMTYZmoL10o9NjF5Vci9UQn094im3vwLK4dNhH3ofRHXg'
    'CfoXx48bb4TN4FQ5u7DhibS/sxMoj8hYtwC3QIOJH2Tl76xH06JQ/w16Ioy5jN9CxVVmC89DMrYwB'
    'tEG/VspXw2N4Eb6D8YU4DDa7lXDUiTgCDcQghtA1c1Doq/RdKcsfJ9vgeyYw2xyNWe6BizAvRucN0'
    'DFQ/gCtzNtaqQ8rXfqup1aHZK8mDt3Il94teAMuwHvwJLQfhFnvgG5iUmGePS6DFwbg2vvwHNSnvt'
    '3D5ET2rhyNVau/ZuEb2M29LQZ9FrppEriC/ADaV74IdZgqKVsdbYTPrp2vZX2qW4Hu1YCGbVBvD0k'
    '38pZkQ8QKVsmKtAXkXJBgv9SK+HV0roFk3FDy4ObSDFyUhW4uluAp6LFZ9l31uLuWPSJtRAKOj/h2'
    'nMC0CiWIOFm70P74CD1WbXRejiaaHkJsIL4byjzMqpB2yUjZIxL2h81qD1kVL4Kj1VJ2TXrINaWPU'
    'maqiWkV8qgsdcqd89ZZYAVMKDbOJfuyOtFnr/h1nECMygk38XvGT4i8M14hG2RuxSLyGeiRaZ9eQ6'
    'ywn19tLsGse13NjEbHGe0xK2cCDUwoGrPjBxcegm68DHV2Fx6Aa6uDqoJ+rdJl6DW/AK2UibVWBn0'
    'nrJzH5GggYg6+gToeQitzGAp9lb4rZfnjZBtyVM4lIHUvoVfc90yCQpxAesmmd03pr5RbF04oOxT2'
    'lu8ecRAm2EpR/Ng3Vkb4QjSoXujTQ22OvOK34bQPND9tr8FPcBCGBpSKOJ6Hjh5d/ES2Qg/rOYY/t'
    '1O5E9N6aNoiN3KNfZAbZPOrT1DeIq/2MowtYj8MDUiv2Xge2fVtAflqELEdP/X4XU9AHovwE8VPCH'
    '2srVCONraY9MPgDAq3/mcZSBv06zfRxsffVGjW2sHHtfHL+S8y+A3HDtV7aIFb0gAAAABJRU5ErkJ'
    'ggg==')


white = "\033[1;37m"
yellow = "\033[1;33m"
red = "\033[1;31m"
reset = "\033[0m"
config = " | ansi=true font='fira code' trim=true size=14 | templateImage={BUILTIN_GPU_ICON}"


topReturn = str(subprocess.getoutput(
    "top -F -R -s 1 -n 0 -o -cpu -l 2"
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
        field = separated[0].strip()
        data = separated[1:]
        top[field] = data


cpuPercent = 100 - float(top['CPU usage'][0].split(", ")[2].split("%")[0])

if cpuPercent <= 30:
    color = white
elif cpuPercent > 30 and cpuPercent <= 50:
    color = yellow
else:
    color = red

stringfiedCpuPercent = str(int(cpuPercent)).rjust(2)

print("{}{}%{}{}| templateImage={}".format(
    color, stringfiedCpuPercent, reset, config, BUILTIN_GPU_ICON))

# print('{}'.format(stringfiedCpuPercent))
# print('{}'.format(topReturn))
print('---')
print('Activity Monitor | shell="sh" param1="$MAC_CONFIG_HOME/scripts/open-activity-monitor.sh" terminal=true')
for each in top:
    print(each + ': ', top[each])
