Open Iterm
Preferences > Keys (or Preferences > Profiles > Keys)
Click the plus.

move forward one word

```option+right
send escape sequence
f
```

move back one word

```option+left
send escape sequence
b
```

delete to beginning of word (credit)

```option+delete
send hex code
0x1B 0x08
```

delete to end of word

```fn+option+delete
send escape sequence
d
```

move beggining of line

```command+left
send hex code
0x01
```

move end of line

```command+right
send hex code
0x05
```
