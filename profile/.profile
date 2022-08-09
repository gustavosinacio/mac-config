# This file is for the configuration of the PATH variable to add apropriate folders

# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

export git=$HOME/github
export GIT=$HOME/github
export MAC_CONFIG_HOME=$HOME/mac-config
export XBAR_PLUGINS="$HOME/Library/Application Support/xbar/plugins/"

export ANDROID_SDK_ROOT=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_SDK_ROOT/emulator
export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools

# set PATH so it includes user's private bin directories
PATH="$HOME/bin:$HOME/.local/bin:$PATH"

# these are configured by me to be universal
# If they exist in the computer, them i want them in my PATH
[ -d $HOME/github/bash-commands ] && PATH="$HOME/github/bash-commands:$PATH" || echo 'No bash-commands'
[ -d $HOME/mac-config/xbar ] && PATH="$HOME/mac-config/xbar:$PATH" || echo 'No xbar'

# Aliases call
[ -f $MAC_CONFIG_HOME/aliases/aliases ] && source $MAC_CONFIG_HOME/aliases/aliases || echo 'No mac config aliases'

# Source local files, if each is found
[ -f ~/.local_aliases ] && source ~/.local_aliases || echo "No local aliases"
[ -f ~/.local_profile ] && source ~/.local_profile || echo "No local profile"
[ -f $HOME/.local-commands ] && PATH="$HOME/.local-commands:$PATH" || echo 'No local commands'
