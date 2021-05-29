from gpiozero import LED
from time import sleep

red = LED(2)

while True:
  red.on()
  print("red on")
  sleep(0.25)
  red.off()
  print("red off")
  sleep(0.25)
