from gpiozero import Button
from signal import pause

left_pedal = Button(2)
center_pedal = Button(3)
right_pedal = Button(26)

while True:
  if left_pedal.is_pressed:
    print("Left Pedal was Pressed")
#left_pedal.when_released = print("Left Pedal was Released")
  if center_pedal.is_pressed:
    print("Center Pedal was Pressed")
#center_pedal.when_released = print("Center Pedal was Not Pressed")
  if right_pedal.is_pressed:
    print("Right Pedal was Pressed")
#right_pedal.when_released = print("Right Pedal was Released")

