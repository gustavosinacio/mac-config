#!/opt/homebrew/bin/python3

import os
import sys
import re

os.system("clear")

try:
    xbarPluginsDirectory = os.environ["XBAR_PLUGINS"]
except:
    print("ERROR: XBAR_PLUGINS environment variable not set")
    sys.exit(1)


try:
    macConfigHome = os.environ["MAC_CONFIG_HOME"]
except:
    print("ERROR: MAC_CONFIG_HOME environment variable not set")
    sys.exit(1)

customPluginsDirectory = os.path.join(macConfigHome, "xbar")
customPlugins = []
regexPattern = re.compile('^\d{3}-.+\.\d+[smhd]\.\w{2}')

for filename in os.listdir(customPluginsDirectory):
    filepath = os.path.join(customPluginsDirectory, filename)
    if os.path.isfile(filepath):
        if regexPattern.search(filename):
            customPlugins.append(filename)

print("--------------------------------------------------")
for filename in customPlugins:
    originPath = os.path.join(customPluginsDirectory, filename)
    destinationPath = os.path.join(xbarPluginsDirectory, filename)

    print("--------------------------------------------------")
    if os.path.isfile(destinationPath):
        print("Plugin " + filename + " exists")
    else:
        print("Adding " + filename + " to plugins")
        os.system("ln '" + originPath + "' '" + destinationPath + "'")

print("--------------------------------------------------")
