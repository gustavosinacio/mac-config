#!/bin/sh

WATCHMAN_LOCATION=/opt/homebrew/bin/watchman

echo "98210 Target watchman"
echo "98211 $(WATCHMAN_LOCATION -v)"

if [ -f WATCHMAN_LOCATION ]; then
  alias watchman=/opt/homebrew/bin/watchman
fi

echo "98212 $(watchman -v)"
