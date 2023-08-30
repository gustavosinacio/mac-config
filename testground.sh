#!/bin/bash

CPU="$(sysctl -n machdep.cpu.brand_string | grep Intel)"

echo $CPU
if [[ $CPU == *"Intel"* ]]; then
  echo "intel"
else
  echo "M1"
fi
