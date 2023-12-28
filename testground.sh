#!/bin/bash

CPU="$(sysctl -n machdep.cpu.brand_string)"

if [[ $CPU == *"Apple"* ]]; then
  echo "M1"
  if which watchman >/dev/null; then
    echo "9821 watchman installed"
  else
    echo "9821 watchman not found"
    export PATH="$PATH:/opt/homebrew/bin"
  fi
fi
