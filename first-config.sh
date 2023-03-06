#!/bin/bash

export MAC_CONFIG_HOME=$HOME/mac-config

cd $MAC_CONFIG_HOME

git pull origin master

./gitconfig/config
./zsh/config
./profile/config
./vim/config
./spaceship/config

sh ./install-packages.sh
