#!/bin/bash

# <xbar.title>show cpu percent</xbar.title>
# <xbar.version>v0.0.1</xbar.version>
# <xbar.author>Gustavo Inacio</xbar.author>
# <xbar.author.github>gustavosinacio</xbar.author.github>
# <xbar.desc>Displays cpu usage</xbar.desc>

cpu_percent=$(top -F -R -o cpu -l 2 -s 1 | grep -E "^CPU" | tail -1 | awk '{ print $3 + $5"%" }')
leftover_idle=$(top -l 2 -s 0 | grep -E "^CPU" | tail -1 | awk '{ print 100 - $7"%" }')

# echo -e "\e[92m$cpu_percent"
echo -en "\033[1;32m"
printf "$cpu_percent%"
echo -en "\033[0m"
echo " | ansi=true font='fira code' trim=false size=12";

echo "---"

echo -en "\033[1;31m$leftover_idle -> from idle\033[0m"
echo " | ansi=true font='fira code' trim=false";

echo "---"

echo "Refresh | refresh=true"
