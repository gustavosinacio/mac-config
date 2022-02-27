#!/opt/homebrew/bin/python3

import subprocess

config = "size=14"
bandwithLine = str(subprocess.getoutput(
    "/opt/homebrew/bin/ifstat -i en0 0.5 1 | tail -1"))
stripedInfo = []

for info in bandwithLine.split(" "):
    if info != "":
        stripedInfo.append(info)

download = float(stripedInfo[0])
downloadSuffix = ""
upload = float(stripedInfo[1])
uploadSuffix = ""

if(download >= 1000):
    download /= 1000
    downloadSuffix = "m"

if(upload >= 1000):
    upload /= 1000
    uploadSuffix = "m"

download = "{:.1f}".format(download).rjust(7)
upload = "{:.1f}".format(upload).rjust(7)

print("\033[1;32m▼\033[0m {}{} º {}{} \033[1;33m▲\033[0m | {}".format(
    download, downloadSuffix, upload, uploadSuffix, config))
