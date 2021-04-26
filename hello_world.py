#!/usr/bin/env python3
from gpiozero import Button
from signal import pause

left_pedal = Button(2)
center_pedal = Button(3)
right_pedal = Button(26)

def buildKeyboard(shift=False):
    multiplier = 2
    null_chr = chr(0) # Standard character set
    if shift == True:
        null_chr = chr(32)+chr(0) # Shift character set
    keys = {
      "a": null_chr*multiplier+chr(4)+null_chr*5,
      "A": null_chr+chr(4)+chr(0)*5,
      "b": null_chr*multiplier+chr(5)+null_chr*5,
      "B": null_chr+chr(5)+chr(0)*5,
      "c": null_chr*multiplier+chr(6)+null_chr*5,
      "C": null_chr+chr(6)+chr(0)*5,
      "d": null_chr*multiplier+chr(7)+null_chr*5,
      "D": null_chr+chr(7)+chr(0)*5,
      "e": null_chr*multiplier+chr(8)+null_chr*5,
      "E": null_chr+chr(8)+chr(0)*5,
      "f": null_chr*multiplier+chr(9)+null_chr*5,
      "F": null_chr+chr(9)+chr(0)*5,
      "g": null_chr*multiplier+chr(10)+null_chr*5,
      "G": null_chr+chr(10)+chr(0)*5,
      "h": null_chr*multiplier+chr(11)+null_chr*5,
      "H": null_chr+chr(11)+chr(0)*5,
      "i": null_chr*multiplier+chr(12)+null_chr*5,
      "I": null_chr+chr(12)+chr(0)*5,
      "j": null_chr*multiplier+chr(13)+null_chr*5,
      "J": null_chr+chr(13)+chr(0)*5,
      "k": null_chr*multiplier+chr(14)+null_chr*5,
      "K": null_chr+chr(14)+chr(0)*5,
      "l": null_chr*multiplier+chr(15)+null_chr*5,
      "L": null_chr+chr(15)+chr(0)*5,
      "m": null_chr*multiplier+chr(16)+null_chr*5,
      "M": null_chr+chr(16)+chr(0)*5,
      "n": null_chr*multiplier+chr(17)+null_chr*5,
      "N": null_chr+chr(17)+chr(0)*5,
      "o": null_chr*multiplier+chr(18)+null_chr*5,
      "O": null_chr+chr(18)+chr(0)*5,
      "p": null_chr*multiplier+chr(19)+null_chr*5,
      "P": null_chr+chr(19)+chr(0)*5,
      "q": null_chr*multiplier+chr(20)+null_chr*5,
      "Q": null_chr+chr(20)+chr(0)*5,
      "r": null_chr*multiplier+chr(21)+null_chr*5,
      "R": null_chr+chr(21)+chr(0)*5,
      "s": null_chr*multiplier+chr(22)+null_chr*5,
      "S": null_chr+chr(22)+chr(0)*5,
      "t": null_chr*multiplier+chr(23)+null_chr*5,
      "T": chr(0)+chr(23)+null_chr*5,
      "u": null_chr*multiplier+chr(24)+null_chr*5,
      "U": chr(0)+chr(24)+null_chr*5,
      "v": null_chr*multiplier+chr(25)+null_chr*5,
      "V": chr(0)+chr(25)+null_chr*5,
      "w": null_chr*multiplier+chr(26)+null_chr*5,
      "W": chr(0)+chr(26)+null_chr*5,
      "x": null_chr*multiplier+chr(27)+null_chr*5,
      "X": chr(0)+chr(27)+null_chr*5,
      "y": null_chr*multiplier+chr(28)+null_chr*5,
      "Y": chr(0)+chr(28)+null_chr*5,
      "z": null_chr*multiplier+chr(29)+null_chr*5,
      "Z": chr(0)+chr(29)+null_chr*5,
      "enter": null_chr*multiplier+chr(40)+null_chr*5,
      "space": chr(0)*multiplier+chr(44)+null_chr*5,
      "release_one": chr(0)*8,
      "release_all": chr(0)*8
    }
    return keys

def press(key, shift=False, hold=False):
    skip_release = ["release_one", "release_all"] # Break infinite loop by releasing keypress
    keys = buildKeyboard(shift)
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(keys[key].encode())
        if (hold == False and (key not in skip_release)):
            press("release_one")
 
# Type "hello"
press("H", True)
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
