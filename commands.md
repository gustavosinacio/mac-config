# Network commands

* find command using specific port

```sh
lsof -nP -iTCP -sTCP:LISTEN | grep [PORT]
```

---
# Miscellaneous

* Kill process by PID number
```
kill -9 [PID]
```
* show hidden files by default
```
defaults write com.apple.finder AppleShowAllFiles -boolean true; killall Finder;
```

---
# PSQL

* create database from command line
```
createdb [name]
```