#!/bin/bash

echo $ANDROID_SDK_ROOT

NC='\033[0m' # No Color
BLACK='\033[0;30m'
GRAY='\033[1;30m'
RED='\033[0;31m'
LIGHT_RED='\033[1;31m'
GREEN='\033[0;32m'
LIGHT_GREEN='\033[1;32m'
BROWN='\033[0;33m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
LIGHT_BLUE='\033[1;34m'
PURPLE='\033[0;35m'
LIGHT_PURPLE='\033[1;35m'
CYAN='\033[0;36m'
LIGHT_CYAN='\033[1;36m'
LIGHT_GRAY='\033[0;37m'
WHITE='\033[1;37m'

if [ -d $ANDROID_SDK_ROOT/build-tools/33.0.1 ]; then
  echo -e "$GREEN\t--- Android SDK build tools 33.0.1 found. $WHITE"
  if [ -f $ANDROID_SDK_ROOT/build-tools/33.0.1/dx ]; then
    echo -e "$YELLOW\t\tdx file from build-tools 33.0.1 found. Skipping... $WHITE"
  else
    echo -e "$RED\t\tdx file from build-tools not found. Copyng d8 file $WHITE"
    cp $ANDROID_SDK_ROOT/build-tools/33.0.1/d8 $ANDROID_SDK_ROOT/build-tools/33.0.1/dx
  fi
else
  echo -e "$RED\t--- Android SDK build tools 33.0.1 not found. $WHITE"
fi

if [ -d $ANDROID_SDK_ROOT/build-tools/33.0.1/lib ]; then
  echo -e "$GREEN\t--- Android SDK build tools 33.0.1 lib found. $WHITE"
  if [ -f $ANDROID_SDK_ROOT/build-tools/33.0.1/lib/dx.jar ]; then
    echo -e "$YELLOW\t\tdx.jar file from build-tools 33.0.1 lib found. Skipping... $WHITE"
  else
    echo -e "$RED\t\tdx.jar file from build-tools not found. Copyng d8.jar file. $WHITE"
    cp $ANDROID_SDK_ROOT/build-tools/33.0.1/lib/d8.jar $ANDROID_SDK_ROOT/build-tools/33.0.1/lib/dx.jar
  fi
else
  echo -e "$RED\t--- Android SDK build tools 33.0.1 lib found. $WHITE"
fi
# console.log(9821, '\x1b[32m', value, '\x1b[0m')
