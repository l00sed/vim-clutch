#!/usr/bin/env python3
NULL_CHAR = chr(0)
keys = {
  "a": NULL_CHAR*2+chr(4)+NULL_CHAR*5,
  "b": NULL_CHAR*2+chr(5)+NULL_CHAR*5,
  "c": NULL_CHAR*2+chr(6)+NULL_CHAR*5,
  "d": NULL_CHAR*2+chr(7)+NULL_CHAR*5,
  "e": NULL_CHAR*2+chr(8)+NULL_CHAR*5,
  "f": NULL_CHAR*2+chr(9)+NULL_CHAR*5,
  "enter": NULL_CHAR*2+chr(40)+NULL_CHAR*5,
  "space": NULL_CHAR*2+chr(44)+NULL_CHAR*5,
  "one": NULL_CHAR*8,
  "all": NULL_CHAR*8
}

def press(key, shift=False):
    if shift == True:
      NULL_CHAR = chr(32) 
    with open('/dev/hidg0', 'rb+') as fd:
      fd.write(keys[key].encode())

def release(key):
    with open('/dev/hidg0', 'rb+') as fd:
      if key == "one":
        fd.write(keys[key].encode())
      if key == "all":
        fd.write(keys[key].encode())
 
# Press a
press("a")
# Release keys
release("one")

# Press SHIFT + a = A
press("a", True)
release("one") 

# Press SHIFT + b = B
press("b", True)
release("one") 

# Press SPACE key
press("space", True)
release("one")
 
# Press c key
press("c")
# Press d key
press("d")
 
# Press RETURN/ENTER key
press("enter")
 
# Press e key
press("e")
# Press f key
press("f")
 
# Release all keys
release("all")

