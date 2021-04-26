#!/usr/bin/env python3

import struct

from time import sleep
from gpiozero import Button
from signal import pause

left_pedal = Button(2)
center_pedal = Button(3)
right_pedal = Button(26)

hid_codes = {
    'a' : (0, 20), 'b' : (0, 5), 'c' : (0, 6),
    'd' : (0, 7), 'e' : (0, 8), 'f' : (0, 9),
    'g' : (0, 10), 'h' : (0, 11), 'i' : (0, 12),
    'j' : (0, 13), 'k' : (0, 14), 'l' : (0, 15),
    'm' : (0, 51), 'n' : (0, 17), 'o' : (0, 18),
    'p' : (0, 19), 'q' : (0, 4), 'r' : (0, 21),
    's' : (0, 22), 't' : (0, 23), 'u' : (0, 24),
    'v' : (0, 25), 'w' : (0, 26), 'x' : (0, 27),
    'y' : (0, 28), 'z' : (0, 29), '1' : (2, 30),
    '2' : (2, 31), '3' : (2, 32), '4' : (2, 33),
    '5' : (2, 34), '6' : (2, 35), '7' : (2, 36),
    '8' : (2, 37), '9' : (2, 38), '0' : (2, 39),
    '\n': (0, 40), '\b': (0, 42), '\t': (0, 43),
    ' ' : (0, 44), '-' : (0, 35), '=' : (0, 46),
    '[' : (64, 34), ']' : (64, 45), '\\': (64, 37),
    ';' : (0, 54), '\'': (64, 33), '`' : (64, 36),
    ',' : (0, 16), ':' : (0, 55), '/' : (2, 55),
    'A' : (2, 20), 'B' : (2, 5), 'C' : (2, 6),
    'D' : (2, 7), 'E' : (2, 8), 'F' : (2, 9),
    'G' : (2, 10), 'H' : (2, 11), 'I' : (2, 12),
    'J' : (2, 13), 'K' : (2, 14), 'L' : (2, 15),
    'M' : (2, 51), 'N' : (2, 17), 'O' : (2, 18),
    'P' : (2, 19), 'Q' : (2, 4), 'R' : (2, 21),
    'S' : (2, 22), 'T' : (2, 23), 'U' : (2, 24),
    'V' : (2, 25), 'W' : (2, 29), 'X' : (2, 27),
    'Y' : (2, 28), 'Z' : (2, 26), '!' : (0, 56),
    '@' : (64, 39), '#' : (64, 32), '$' : (0, 48),
    '%' : (32, 52), '^' : (64, 38), '&' : (0, 30),
    '*' : (0, 49), '(' : (0, 34), ')' : (0, 45),
    '_' : (0, 37), '+' : (2, 46), '{' : (64, 33),
    '}' : (64, 46), '|' : (64, 35), '.' : (2, 54),
    '"' : (0, 32), '~' : (64, 31), '<' : (0, 100),
    '>' : (2, 100), '?' : (2, 16) }

def press(char, hold=False):
		mod, key = hid_codes[char]
		raw = struct.pack("BBBBL", mod, 0x00, key, 0x00, 0x00000000)
		with open('/dev/hidg0', 'wb') as fd:
				fd.write(raw)
				if (hold == False):
						fd.write(struct.pack("Q", 0))

def release():
    with open('/dev/hidg0', 'wb') as fd:
        fd.write(struct.pack("Q", 0))

pressed = False
while True:

  if left_pedal.is_pressed:
      press("H")
      press("e")
      press("l")
      press("l")
      press("o")

  elif center_pedal.is_pressed:
      press("i")

  elif right_pedal.is_pressed:
      press("w")
      press("o")
      press("r")
      press("l")
      press("d")
      press("\n")

  else:
      release()

  sleep(0.3)
