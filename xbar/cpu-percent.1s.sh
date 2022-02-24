#!/bin/bash

# <xbar.title>show cpu percent</xbar.title>
# <xbar.version>v0.0.1</xbar.version>
# <xbar.author>Gustavo Inacio</xbar.author>
# <xbar.author.github>gustavosinacio</xbar.author.github>
# <xbar.desc>Displays cpu usage</xbar.desc>

cpu_percent=$(top -l 2 -s 0| grep -E "^CPU" | tail -1 | awk '{ print $3 + $5"%" }')
leftover_idle=$(top -l 2 -s 0w| grep -E "^CPU" | tail -1 | awk '{ print 100 - $7"%" }')

# echo -e "\e[92m$cpu_percent"
echo -en "\033[1;36m"
# printf "%0.1f\n" "$(bc -q <<< scale=3\;"$cpu_percent")"
printf "$cpu_percent%"

echo -e "\033[0m"
echo " | ansi=true font='fira code' trim=false";
echo "---"

echo -en "\033[1;31m$leftover_idle -> from idle\033[0m"
echo " | ansi=true font='fira code' trim=false";

echo "---"
echo "Refresh | refresh=true"
