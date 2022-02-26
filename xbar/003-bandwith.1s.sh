#!/usr/bin/env bash

# <xbar.title>Bandwidth (K or M)</xbar.title>
# <xbar.version>v0.0.2</xbar.version>
# <xbar.author>Gustavo Inacio</xbar.author>
# <xbar.author.github>gustavosinacio</xbar.author.github>
# <xbar.desc>Displays bandwidth usage for the primary interface</xbar.desc>
# <xbar.dependencies>ifstat</xbar.dependencies>
# <xbar.image>https://user-images.githubusercontent.com/13082464/113498791-ba3ef380-9542-11eb-82e4-76e78cac98b7.png</xbar.image>

# based on Bandwidth '(KB/s or MB/s)' by UyNguyen
INTERFACE="en0"

if [ ! -e /opt/homebrew/bin/ifstat ]; then
    echo "Please install ifstat or change the path to it in the script."
    exit 1
fi

function kilo_to_mega {
  # in networking 1 mbit is 1000 kilobits (not 1024)
  Kbps=${1}
  KBps=$Kbps/8 # Kilo Bytes 
  if [ "`echo "$KBps < 800.0" | bc`" -eq 1 ]; then
    printf "%0.1fk\n" "$(bc -q <<< scale=3\;"$KBps")"
  elif [ "`echo "$KBps < 1000000.0" | bc`" -eq 1 ]; then
    printf "%0.1fm\n" "$(bc -q <<< scale=3\;"$KBps"/1000)"
  else
    printf "%0.1fg\n" "$(bc -q <<< scale=3\;"$KBps"/1000000)"
  fi;
}

function get_ifstat {
    interface=$1
    # 1 sample for 0.5 second interval
    # outputs two values (in/out) in kilobits per second
    /opt/homebrew/bin/ifstat -n -w -i "${interface}" -b 0.5 1 | tail -n 1
}

function print_ifstat {
    kbits_in=$(echo "$1" | awk '{ print $1 }')
    kbits_out=$(echo "$1" | awk '{ print $2 }')
    mbits_in=$(kilo_to_mega "$kbits_in")
    mbits_out=$(kilo_to_mega "$kbits_out")
    echo -e "\033[1;32m▼\033[0m $mbits_in • $mbits_out \033[1;33m▲\033[0m | size=14"

}

print_ifstat "$(get_ifstat ${INTERFACE})"
echo "---"
