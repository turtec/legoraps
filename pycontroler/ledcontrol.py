from lib.LED import LED
import time
import sys

import importlib.util
try:
    print("use1")
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    print("use Fake")
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """
    import FakeRPi.GPIO as GPIO

#EnableA = 21
#Input1 = 16
#Input2 = 20

  #  EnableA = 26
#Input1 = 19
#Input2 = 13

led = LED(2,GPIO)

def control(command):
  if command == "1":
    led.on()
  if command == "0":
    led.off()

try:
  while True:
    val = input('Choose a mode 1-on, 0-off: ')
    control(val)

except KeyboardInterrupt:
  GPIO.cleanup()
  #stop()
  print('stopped')
  #
