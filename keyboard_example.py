#!/usr/bin/env python3
NULL_CHAR = chr(0)
keys = {
  "a": NULL_CHAR*2+chr(4)+NULL_CHAR*5,
  "b": NULL_CHAR*2+chr(5)+NULL_CHAR*5,
  "c": NULL_CHAR*2+chr(6)+NULL_CHAR*5,
  "d": NULL_CHAR*2+chr(7)+NULL_CHAR*5,
  "e": NULL_CHAR*2+chr(8)+NULL_CHAR*5,
  "f": NULL_CHAR*2+chr(9)+NULL_CHAR*5,
  "g": NULL_CHAR*2+chr(10)+NULL_CHAR*5,
  "h": NULL_CHAR*2+chr(11)+NULL_CHAR*5,
  "i": NULL_CHAR*2+chr(12)+NULL_CHAR*5,
  "j": NULL_CHAR*2+chr(13)+NULL_CHAR*5,
  "k": NULL_CHAR*2+chr(14)+NULL_CHAR*5,
  "l": NULL_CHAR*2+chr(15)+NULL_CHAR*5,
  "m": NULL_CHAR*2+chr(16)+NULL_CHAR*5,
  "n": NULL_CHAR*2+chr(17)+NULL_CHAR*5,
  "o": NULL_CHAR*2+chr(18)+NULL_CHAR*5,
  "p": NULL_CHAR*2+chr(19)+NULL_CHAR*5,
  "q": NULL_CHAR*2+chr(20)+NULL_CHAR*5,
  "r": NULL_CHAR*2+chr(21)+NULL_CHAR*5,
  "s": NULL_CHAR*2+chr(22)+NULL_CHAR*5,
  "t": NULL_CHAR*2+chr(23)+NULL_CHAR*5,
  "u": NULL_CHAR*2+chr(24)+NULL_CHAR*5,
  "v": NULL_CHAR*2+chr(25)+NULL_CHAR*5,
  "w": NULL_CHAR*2+chr(26)+NULL_CHAR*5,
  "x": NULL_CHAR*2+chr(27)+NULL_CHAR*5,
  "y": NULL_CHAR*2+chr(28)+NULL_CHAR*5,
  "z": NULL_CHAR*2+chr(29)+NULL_CHAR*5,
  "enter": NULL_CHAR*2+chr(40)+NULL_CHAR*5,
  "space": NULL_CHAR*2+chr(44)+NULL_CHAR*5,
  "release_one": NULL_CHAR*8,
  "release_all": NULL_CHAR*8
}

def press(key, shift=False, hold=False):
    skip_release = ["release_one", "release_all"]
    if shift == True:
        NULL_CHAR = chr(32) 
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(keys[key].encode())
        if (hold == False and (key not in skip_release)):
            press("release_one")
 
# Type "hello"
press("h")
press("e")
press("l")
press("l")
press("o")
# Press SPACE key
press("space")
# Type "world"
press("w")
press("o")
press("r")
press("l")
press("d")

# Press RETURN/ENTER key
press("enter")
# Extra "kill" step
press("release_all")
