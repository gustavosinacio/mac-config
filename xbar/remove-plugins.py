#!/opt/homebrew/bin/python3

import os
import re
import sys


os.system("clear")
print("--------------------------------------------------")
print("removing ALL existing xbar plugins")
print("--------------------------------------------------")

try:
    xbarPluginsDirectory = os.environ["XBAR_PLUGINS"]
except:
    print("ERROR: XBAR_PLUGINS environment variable not set")
    sys.exit(1)

regexPattern = re.compile('^\d{3}-.+\.\d+[smhd]\.\w{2}')

for filename in os.listdir(xbarPluginsDirectory):
    filepath = os.path.join(xbarPluginsDirectory, filename)
    if os.path.isfile(filepath):
        if regexPattern.search(filename):
            os.unlink(filepath)
