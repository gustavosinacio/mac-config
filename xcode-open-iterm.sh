#!/bin/sh
dir="$PWD"
# remove a potential suffix in case Xcode shows a Swift Package
suffix="/.swiftpm/xcode"
dir=${dir//$suffix/}
open -a iterm "$dir"