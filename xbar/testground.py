#!/opt/homebrew/bin/python3

import subprocess
from plistlib import loads


output = subprocess.check_output(
    ["system_profiler", "-xml"]
    # "echo test"
)
plist = loads(output)

print(output)
